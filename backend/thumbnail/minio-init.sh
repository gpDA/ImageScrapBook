#!/bin/sh
# Make default buckets if don't exist
mkdir -p data/thumb
mkdir -p data/image

minio server /data &

# Set policy
wget https://dl.minio.io/client/mc/release/linux-amd64/mc
chmod +x mc
./mc config host add minio http://localhost:9000 $MINIO_ACCESS_KEY $MINIO_SECRET_KEY
./mc policy download minio/image/
./mc policy download minio/thumb/

wait
