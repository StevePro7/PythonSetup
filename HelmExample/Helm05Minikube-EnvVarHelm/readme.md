readme
19-Apr-2023

https://stackoverflow.com/questions/56003777/how-to-pass-environment-variable-in-kubectl-deployment

pip install -r requirements.txt
Run
curl localhost:8080

docker build --pull --rm -f "Dockerfile" -t helloworldpython:latest "."
docker run --rm -d -p 8080:8080/tcp helloworldpython:latest

minikube docker-env
eval $(minikube -p minikube docker-env)

01.
kubectl apply -f k8s-namespace.yml
kubectl apply -f k8s-deployment.yml
kubectl apply -f k8s-service.yml
k exec testwebapi-899d5985c-pdc8f -- printenv
MY_VATS=MY_VALUES

minikube service testwebapi-service -n env-vars --url
http://192.168.15.50:30245

curl http://192.168.15.50:30245
Hello World 'MY_VALUES'! (up 0:01:10)

02. Helm

