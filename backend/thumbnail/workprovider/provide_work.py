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
    s3 = boto3.resource('s3', use_ssl=False, endpoint_url='http://minio:9000/')
    first = True
    while True:
        for fname in os.listdir('imgsrc'):
            s3name = fname
            if first:
                with open('imgsrc/' + fname, "rb") as f:
                    s3.Object('image', s3name).put(Body=f)
            thumbnail.thumbnailify.delay(s3name, (200, 200))
        first = False
