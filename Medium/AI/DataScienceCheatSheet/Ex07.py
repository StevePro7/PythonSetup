# 7. Working with APIs
import requests
import http

# GET Request
response = requests.get("https://api.example.com/data")
if response.status_code == http.HTTPStatus.OK:
    data = response.json()

# POST Request
payload = {"key": "value"}
response = requests.post("https://api.example.com/data", json=payload)