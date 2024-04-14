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

UPDATE
mv hello-world helm
helm/Chart.yaml
helm/templates/deployment.yaml
helm/templates/service.yaml
helm/values.yaml

curl http://192.168.15.50:30088
curl: (7) Failed to connect to 192.168.15.50 port 30088: Connection refused

helm install hello-world --namespace hello-world --create-namespace ./helm

curl http://192.168.15.50:30088
curl: (7) Failed to connect to 192.168.15.50 port 30088: Connection refused

Get the application URL by running these commands:
export NODE_PORT=$(kubectl get --namespace hello-world -o jsonpath="{.spec.ports[0].nodePort}" services hello-world)
export NODE_IP=$(kubectl get nodes --namespace hello-world -o jsonpath="{.items[0].status.addresses[0].address}")
echo http://$NODE_IP:$NODE_PORT


NOTE
first time did not work because the appVerion in Chart.yaml did not match
so get ImagePullBackOff
Failed to pull image "hello-world:1.16.0": rpc error:

RETRY
helm install hello-world --namespace hello-world --create-namespace ./helm

export NODE_PORT=$(kubectl get --namespace hello-world -o jsonpath="{.spec.ports[0].nodePort}" services hello-world)
export NODE_IP=$(kubectl get nodes --namespace hello-world -o jsonpath="{.items[0].status.addresses[0].address}")
echo http://$NODE_IP:$NODE_PORT

curl http://192.168.15.50:30088
Hello World (Python)! (up 0:00:32)