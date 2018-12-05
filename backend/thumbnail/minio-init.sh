#!/bin/sh
# Make default buckets if don't exist
mkdir -p data/thumb
mkdir -p data/image

minio server /data
