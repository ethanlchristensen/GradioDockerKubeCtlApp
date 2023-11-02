@echo off
echo building docker image
docker build --tag app-server:latest .
echo running image on kubectl
kubectl run app-server --image=app-server:latest --image-pull-policy=Never --port=7860
timeout 5
echo fowarding the kubectl port to 7860
kubectl port-forward pods/app-server 7860:7860