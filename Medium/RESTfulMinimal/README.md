A minimal RESTful API in Python
15-Sep-2024

https://medium.com/@johnidouglasmarangon/a-minimal-restful-api-in-python-2c316bd2c0c3

pip install -r requirements.txt

pip install --upgrade pip


uvicorn main:app --reload


docker build -t myminimalapi .

docker run -e APP_WORKERS=8 -p 8000:8000 myminimalapi


curl -X 'POST' \
  'http://0.0.0.0:8000/filesize/url' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "url": "https://pdfobject.com/pdf/sample.pdf"
}'