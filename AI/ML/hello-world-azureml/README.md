Hello World Azure ML
28-Oct-2025
Linux
delete .venv
delete pyproject.toml

uv init --python 3.12.3
uv sync
source .venv/bin/activate

which python
~/GitHub/StevePro9/PythonSetup/ML/hello-world-azureml/.venv/bin/python --version

Python | No interpreter
Select existing
uv
~/GitHub/StevePro9/PythonSetup/ML/hello-world-azureml/.venv/bin/python

sudo fuser -k 5001/tcp
01. localhost
Run local_inference_server
python local_inference_server.py
curl -X POST http://localhost:5001/score -H 'Content-Type: application/json' -d '{"name": "Alice"}'
curl -X POST http://localhost:5001/score -H 'Content-Type: application/json' -d '{"features": [[5, 2, 3]]}'
curl -X POST http://localhost:5001/score -H 'Content-Type: application/json' -d '{"instances": [[5, 2, 3]]}'

02. Docker
docker build -t azure-ml-local .
docker run -p 5001:5001 azure-ml-local

# Health check
curl http://localhost:5001/health

# Score endpoint - using name
curl -X POST http://localhost:5001/score \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice"}'

# Score endpoint - using features
curl -X POST http://localhost:5001/score \
  -H "Content-Type: application/json" \
  -d '{"features": [[5, 2, 3]]}'

Kill port-forward   if running
pkill -f "kubectl port-forward"
kill $(sudo lsof -t -i:5001)


03. KinD cluster
kind create cluster --name flask-cluster
kubectl create ns test-ns
kubectl config set-context --current --namespace=test-ns
kind load docker-image azure-ml-local:latest --name flask-cluster
kubectl apply -f Kubernetes.yaml
kubectl port-forward service/azure-ml-service 5001:5001
kubectl delete -f Kubernetes.yaml


28-Sep-2025
MacOS
python --version
Python 3.12.3

pyenv global 3.12.3
pyenv versions

cd /Users/stevepro/Github/StevePro7/PythonSetup/ML/
mkdir hello-world-azureml
cd hello-world-azureml
uv init
uv venv
source .venv/bin/activate
OR
.venv\Scripts\activate

pyenv version
* 3.12.3 (set by /Users/stevepro/Github/StevePro7/PythonSetup/ML/hello-world-azureml/.python-version)

Add New Interpreter | Add Local Interpreter | Existing
/Users/stevepro/Github/StevePro7/PythonSetup/ML/hello-world-azureml/.venv/bin/python

uv sync

curl -X GET http://localhost:5001/ -H 'Content-Type: application/json'
curl -X GET http://localhost:5001/health -H 'Content-Type: application/json'

curl -X POST http://localhost:5001/score -H 'Content-Type: application/json' -d '{"sleep": 5}'
