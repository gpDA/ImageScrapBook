# Takes example images, uploads to S3, then queues thumbnail tasks

import celery
import thumbnail
import boto3
import os
import uuid
import random
import string


if __name__ == "__main__":
    from time import sleep
    prefix = ''.join(random.choices(string.digits, k=8))
    s3 = boto3.resource('s3', use_ssl=False, endpoint_url='http://minio:9000/')
    for fname in os.listdir('imgsrc'):
        ext = fname.split(".")[-1]
        imguid = uuid.uuid4()
        s3name = f"{prefix}-{str(imguid)}.{ext}"
        with open('imgsrc/'+ fname, "rb") as f:
            s3.Object('image', s3name).put(Body=f)
        thumbnail.thumbnailify(s3name, (200, 200))
