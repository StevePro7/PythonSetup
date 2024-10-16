README.md
05-Aug-2024

Building REST APIs using Flask-RESTPlus, SQLAlchemy & Marshmallow
https://medium.com/analytics-vidhya/building-rest-apis-using-flask-restplus-sqlalchemy-marshmallow-cff76b202bfb

python-sample-flask-application
https://github.com/sumanentc/python-sample-flask-application?tab=readme-ov-file


Notesoverer
FlaskEX.txt
~/Bitbucket/SteveProXNA/actionstuff/MediumDigest/2023/Python


python app.py

Swagger UI
http://127.0.0.1:5000/api/doc


requirements.txt
OVERRLAP

flask-marshmallow==0.14.0       1.2.1
flask-sqlalchemy==2.4.4         3.1.1
flask==1.1.2                    2.3
marshmallow-sqlalchemy==0.24.1  1.0.0

NO 
Pydantic
pytest


CHECK
models
@classmethod

schema
SQLAlchemyAutoSchema

Marshmallow
Nested(ItemSchema, many=True)

Blueprints
but are set direct in app.py

from marshmallow import ValidationError

app.config['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

@app.before_first_request
@api.errorhandler(ValidationError)


TEST
curl -X GET "http://localhost:8080/api/items" -H "accept: application/json"
curl -X GET "http://localhost:8080/api/stores" -H "accept: application/json"


https://gitlab.com/SteveProXNA/gitlabcheatsheet

Docker
docker build --pull --rm -f "Dockerfile" -t flask-api:latest "."
docker run --rm -it -p 8080:8080/tcp flask-api:latest
docker logs -f <conteinar_id>

docker logs -f <conteinar_id>
curl http://localhost:8080/api/items
curl http://127.0.0.1:8080/api/items
curl -X GET "http://127.0.0.1:8080/api/items" -H "accept: application/json"
curl -X GET "http://localhost:8080/api/stores" -H "accept: application/json"
docker stop <conteinar_id>


K8s
kind create cluster --name flask-cluster
kubectl create ns test-ns
kubectl config set-context --current --namespace=test-ns
kind load docker-image flask-api:latest --name flask-cluster
kubectl apply -f Kubernetes.yaml
kubectl logs -f pod/flask-api-deployment-<pod_id>
kubectl port-forward service/flask-api-service 8080:80
curl -X GET "http://127.0.0.1:8080/api/items" -H "accept: application/json"
curl -X GET "http://localhost:8080/api/stores" -H "accept: application/json"
kubectl delete -f Kubernetes.yaml
kind delete cluster --name flask-cluster
