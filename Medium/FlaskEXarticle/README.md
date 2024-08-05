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
curl -X GET "http://localhost:5000/api/items" -H "accept: application/json"
curl -X GET "http://localhost:5000/api/stores" -H "accept: application/json"