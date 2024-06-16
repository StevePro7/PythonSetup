Hello World Kind
15-Jun-2024

Reference;
https://github.com/datawire/hello-world-python

Terminal
kind create cluster --name flask-cluster


Launch PyCharm
New project
hello-world-python-kind
/home/stevepro/GitHub/StevePro9/PythonSetup/ThirdParty

pip install -r requirements.

Run program
curl http://localhost:8080

DOCKER
docker build --pull --rm -f "Dockerfile" -t flask-api:latest "."
docker run --rm -d -p 8080:8080/tcp flask-api:latest

KUBERNETES
kind load docker-image flask-api:latest --name flask-cluster
kubectl apply -f Kubernetes.yaml

kubectl port-forward service/flask-api-service 8080:80
curl http://localhost:8080

kubectl delete -f Kubernetes.yaml
kind delete cluster --name flask-cluster


sudo fuser -k 8080/tcp


DOCKER HUG
docker build --pull --rm -f "Dockerfile" -t flask-api:latest "."

docker tag flask-api:latest steveproxna/flask-api:1.0
docker push steveproxna/flask-api:1.0

kubectl create ns test-ns
kubectl config set-context --current --namespace=test-ns

kubectl apply -f Kubernetes02.yaml

kubectl port-forward service/flask-api-service 8080:80
curl http://localhost:8080
