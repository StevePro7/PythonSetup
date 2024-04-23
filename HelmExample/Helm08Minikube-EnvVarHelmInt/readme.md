readme
14-Apr-2023

helm environment variables integer example
https://github.com/helm/helm/issues/4775

follow on from previous example but use their YAML files then replace with Helm
https://siweheee.medium.com/deploy-your-programs-onto-minikube-with-docker-and-helm-a68097e8d545    

Follow on from Helm05

HELM
kubectl delete namespace hello-world
helm create hello-world

OUTPUT
create top-level directory 'hello-world'

curl http://192.168.15.50:30088
curl: (7) Failed to connect to 192.168.15.50 port 30088: Connection refused

COMMAND
helm install hello-world --namespace hello-world --create-namespace ./helm

IMPORTANT - here is where the namespace is created!!
--namespace hello-world


NAME: hello-world
LAST DEPLOYED: Sat Apr 20 13:33:36 2024
NAMESPACE: hello-world
STATUS: deployed
REVISION: 1
TEST SUITE: None


kubectl get events
18s         Warning   FailedCreate        replicaset/hello-world-57f6d8f5dd   Error creating: pods "hello-world-57f6d8f5dd-" is forbidden: error looking up service account hello-world/hello-world: serviceaccount "hello-world" not found

Obv. must need serviceaccout


curl http://192.168.15.50:30088
curl: (7) Failed to connect to 192.168.15.50 port 30088: Connection refused

Get the application URL by running these commands:
export NODE_PORT=$(kubectl get --namespace hello-world -o jsonpath="{.spec.ports[0].nodePort}" services hello-world)
export NODE_IP=$(kubectl get nodes --namespace hello-world -o jsonpath="{.items[0].status.addresses[0].address}")
echo http://$NODE_IP:$NODE_PORT


curl http://192.168.15.50:30088
Hello World 'STEVEPRO_STUDIOS'! (up 0:00:38)



values.dev
HELM
kubectl delete namespace hello-world
helm create hello-world

curl http://192.168.15.50:30088
curl: (7) Failed to connect to 192.168.15.50 port 30088: Connection refused

COMMAND
helm install hello-world -f helm/values.dev.yaml --namespace hello-world --create-namespace ./helm

curl http://192.168.15.50:30088
Hello World 'STEVEPRO_STUDIOS_DEVELOPMENT'! (up 0:00:39)

So takes all values from values.yaml but overrides in helm/values.dev.yaml where it can!
Success
