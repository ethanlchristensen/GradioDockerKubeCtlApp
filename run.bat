@echo off
echo building docker image
docker build --tag app:latest .
echo running image on kubectl
kubectl run app --image=app:latest --image-pull-policy=Never --port=7860
sleep 1
echo fowarding the kubectl port to 7860
kubectl port-forward pods/app 7860:7860