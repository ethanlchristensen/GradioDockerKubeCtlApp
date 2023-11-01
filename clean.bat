@echo off
echo deleting the kubectl pod
kubectl delete pod app
echo deleting the docker image
docker rmi app:latest
