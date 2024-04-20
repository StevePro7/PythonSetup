readme
14-Apr-2023

follow on from previous example but use their YAML files then replace with Helm
https://siweheee.medium.com/deploy-your-programs-onto-minikube-with-docker-and-helm-a68097e8d545    

Follow on from Helm05

HELM
kubectl delete namespace hello-world
helm create hello-world

//Creates hello-world direhectory with all the corresponding Helm files

UPDATE
mv hello-world helm
helm/Chart.yaml
helm/templates/deployment.yaml
helm/templates/service.yaml
helm/values.yaml

curl http://192.168.15.50:30088
curl: (7) Failed to connect to 192.168.15.50 port 30088: Connection refused

COMMAND
helm install hello-world --namespace hello-world --create-namespace ./helm

Error: INSTALLATION FAILED: YAML parse error on hello-world/templates/deployment.yaml: error converting YAML to JSON: yaml: invalid map key: map[interface {}]interface {}{".Values.env.value":interface {}(nil)}
SOLN
value: {{ .Values.env.value }}


curl http://192.168.15.50:30088
curl: (7) Failed to connect to 192.168.15.50 port 30088: Connection refused

Get the application URL by running these commands:
export NODE_PORT=$(kubectl get --namespace hello-world -o jsonpath="{.spec.ports[0].nodePort}" services hello-world)
export NODE_IP=$(kubectl get nodes --namespace hello-world -o jsonpath="{.items[0].status.addresses[0].address}")
echo http://$NODE_IP:$NODE_PORT


curl http://192.168.15.50:30088
Hello World 'MY_VALUE_ABC'! (up 0:00:38)
