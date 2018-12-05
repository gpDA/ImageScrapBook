# Destroy services
kubectl delete service flowerbox minio rabbit

# Destroy stablesets
kubectl delete statefulset minio rabbit

# Destroy others
kubectl delete deployment celeryworker flowerbox workprovider
