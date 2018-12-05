FROM minio/minio

COPY minio-init.sh /minio-init.sh
ENTRYPOINT ["/minio-init.sh"]
