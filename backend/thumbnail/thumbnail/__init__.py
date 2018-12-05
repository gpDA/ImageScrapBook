import celery
import psycopg2
import boto3
import botocore
import io
from PIL import Image
import os

app = celery.Celery("thumbnail",
                    broker='amqp://user:pass@rabbit:5672/vhost')


def fail_task(task, meta=''):
    task.update_state(state='FAILURE', meta=meta)


@app.task(bind=True)
def thumbnailify(self, imageid, s3url, thumbdim):
    # Get img from S3
    s3 = boto3.resource('s3', endpoint_url="http://minio:9000/")

    try:
        f = io.BytesIO()
        s3.Bucket('image').download_fileobj(s3url, f)
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            fail_task(self, "S3 object 404")
            return

    try:
        img = Image.open(f)  # PIL-friendly format
        img.thumbnail(thumbdim)  # resize
    except ValueError as e:
        fail_task(self, f"PIL error: {str(e)}")
        return
    fout = io.BytesIO()  # output pixel buffer
    fout.name = s3url  # PIL autodetects format from ext

    try:
        img.save(fout)
        fout.seek(0)
    except ValueError as e:
        fail_task(self, f"PIL Image save fail: {str(e)}")
        return
    thumbname = f"{thumbdim[0]}x{thumbdim[1]}_{s3url}"
    try:
        s3.Object('thumb', thumbname).put(Body=fout)
    except:
        fail_task(self, "S3 upload fail")
        return

    conn = psycopg2.connect(os.environ['DATABASE_URL'])
    cur = conn.cursor()
    cur.execute('UPDATE main_image SET thumbnail_url=%s WHERE id=%s', [thumbname, imageid])
    conn.commit()
    return True
