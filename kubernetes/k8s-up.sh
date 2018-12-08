# Foundational services
kubectl create -f minio-deployment.yaml
kubectl create -f rabbit-deployment.yaml
kubectl create -f postgres-deployment.yaml
kubectl create -f minio-service.yaml
kubectl create -f rabbit-service.yaml
kubectl create -f postgres-service.yaml

# Client services
kubectl create -f celeryworker-deployment.yaml
kubectl create -f flowerbox-deployment.yaml

# Migrate django before appserver up
kubectl create -f appserver-init.yaml

# Appserver
kubectl create -f appserver-deployment.yaml

# Expose to outside world
kubectl create -f flowerbox-service.yaml
kubectl create -f appserver-service.yaml
