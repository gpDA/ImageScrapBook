# Foundational services
kubectl create -f minio-deployment.yaml
kubectl create -f rabbit-deployment.yaml
kubectl create -f minio-service.yaml
kubectl create -f rabbit-service.yaml

# Client services
kubectl create -f celeryworker-deployment.yaml
kubectl create -f flowerbox-deployment.yaml
kubectl create -f workprovider-deployment.yaml

# Expose to outside world
kubectl create -f flowerbox-service.yaml
kubectl create -f minio-service.yaml
