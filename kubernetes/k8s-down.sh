# services deleted
kubectl delete service appserver flowerbox minio postgres rabbit

# delete deployments
kubectl delete deployment appserver celeryworker flowerbox

# stateful sets
kubectl delete statefulset minio postgres rabbit
