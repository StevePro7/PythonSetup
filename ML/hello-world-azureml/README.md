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
