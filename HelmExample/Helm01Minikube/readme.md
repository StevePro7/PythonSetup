readme
14-Apr-2023

GOAL
do org. python flask app
run local, docker, in k8s [minikube]
finally use Helm to replace manual k8s

Reference:
https://siweheee.medium.com/deploy-your-programs-onto-minikube-with-docker-and-helm-a68097e8d545

minikube start --driver=none


Python app
https://github.com/StevePro7/PythonSetup/tree/master/ThirdParty/hello-world-python
https://github.com/StevePro7/CloudTesting/tree/main/KubernetesCheatSheet/01-Example


pip install -r requirements.txt
Run
curl localhost:8080

docker build --pull --rm -f "Dockerfile" -t helloworldpython:latest "."
docker run --rm -d -p 8080:8080/tcp helloworldpython:latest 


IMPORTANT
these next 2x commands do not work because of the  --driver=none arguments
fortunately can still complete the example! 

minikube docker-env
eval $(minikube -p minikube docker-env)

kubectl apply -f Kubernetes.yaml
minikube service testwebapi-service --url

curl http://192.168.15.50:32168
