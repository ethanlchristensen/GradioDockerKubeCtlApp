@echo off
echo building docker image
docker build --tag app-client:latest .
echo running image on kubectl
kubectl run app-client --image=app-client:latest --image-pull-policy=Never --port=7861
timeout 5
echo fowarding the kubectl port to 7861
kubectl port-forward pods/app-client 7861:7861