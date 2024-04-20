readme
19-Apr-2023

pip install -r requirements.txt
Run
curl localhost:8080

docker build --pull --rm -f "Dockerfile" -t helloworldpython:latest "."
docker run --rm -d -p 8080:8080/tcp helloworldpython:latest 

minikube docker-env
eval $(minikube -p minikube docker-env)

kubectl apply -f Kubernetes.yaml
minikube service testwebapi-service --url

curl http://192.168.15.50:32168


TODO couldn't get env vars passed into endpoint
Reference
https://stackoverflow.com/questions/31964031/using-environment-variables-in-curl-command-unix

curl localhost:8080 -d '{"TEST_INPUT":"splat"}'

curl -k -X GET -H 'Content-Type: application/json' -d '{"TEST_INPUT":"splat"}' 
