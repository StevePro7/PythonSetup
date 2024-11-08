Everything You Need to Know About Domain-Driven Design with Python Microservices!
08-Nov-2024

https://medium.com/@nomannayeem/everything-you-need-to-know-about-domain-driven-design-with-python-microservices-2c2f6556b5b1


pip install fastapi uvicorn sqlalchemy
pip install sqlalchemy

pip freeze > requirements.txt
pip install --upgrade pip


uvicorn order_service.main:app --reload
http://0.0.0.0:8000


Sales Microservice
POST    /orders
GET     /orders/{id}

Shipping Microservice
POST /shipments
GET /shipments/{id}


sales_service
uvicorn main:app --reload

POST    http://127.0.0.1:8000/orders
GET     http://127.0.0.1:8000/orders/{order_id}


tests
python -m unittest tests/test_order.py