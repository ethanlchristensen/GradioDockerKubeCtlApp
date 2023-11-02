@echo off
echo deleting the kubectl pod
kubectl delete pod app-server
echo deleting the docker image
docker rmi app-server:latest
