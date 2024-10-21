Creating a Complete RESTful API with FastAPI
20-Oct-2024

https://jnikenoueba.medium.com/creating-a-complete-restful-api-with-fastapi-79edf7afeef8

python -m venv .venv
source venv/bin/activate
`
pip install fastapi uvicorn sqlalchemy databases

pip install -r requirements.txt

pip install sqlalchemy
pip install pydantic
pip install fastapi

TEST
uvicorn app.main:app --reload


http://127.0.0.1:8000

http://127.0.0.1:8000/docs

GET
http://127.0.0.1:8000/items/1

POST
curl -X 'POST' \
  'http://127.0.0.1:8000/items/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": 1,
  "title": "test",
  "description": "hello world"
}'


01. Environment
python -m venv .venv
source venv/bin/activate

02. DB Models
SQLAlchemy	define database Models

03. Pydantic
Pydantic schemas	ensure data validation

04. CRUD Operations

05. DB Configuration

06. Fast API application