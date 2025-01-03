Integrating FastAPI with MongoDB
03-Jan--2025
https://blog.devgenius.io/integrating-fastapi-with-mongodb-a5f539331043


Already installed mongoDB and mongoSH
VS Code | right click mongo
Run
OR
docker run --rm -d -p 27017:27017/tcp mongo:latest 


python -m venv .venv
source .venv/bin/activate

pip install fastapi uvicorn motor
pip install --upgrade pip


uvicorn app.main:app --reload
http://127.0.0.1:8000/docs


docker run --rm -d -p 27017:27017/tcp mongo:latest
mongosh "mongodb://localhost:27017/mydatabase"

show tables
OR
db.getCollectionNames()
["items""]
db.items.find()


could not debug
curl -X 'GET' \
  'http://0.0.0.0:8000/items/?skip=0&limit=10' \
  -H 'accept: application/json'