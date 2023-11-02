@echo off
echo deleting the kubectl pod
kubectl delete pod app-client
echo deleting the docker image
docker rmi app-client:latest
