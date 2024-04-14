readme
14-Apr-2023

follow on from previous example but use their YAML files then replace with Helm
https://siweheee.medium.com/deploy-your-programs-onto-minikube-with-docker-and-helm-a68097e8d545    

IMPORANT - this article prefers
minikube start — vm-driver=virtualbox


Run locally as before

Docker
docker build -t hello-world:0.1.0 -f Dockerfile .
docker run --rm -d -p 8080:8080/tcp hello-world:0.1.0


kubectl apply -f k8s-namespace.yml
kubectl apply -f k8s-deployment.yml
kubectl apply -f k8s-service.yml

minikube service hello-world -n hello-world
curl http://192.168.15.50:30088


HELM
kubectl delete namespace hello-world
helm create hello-world

Creates hello-world direhectory with all the corresponding Helm files
