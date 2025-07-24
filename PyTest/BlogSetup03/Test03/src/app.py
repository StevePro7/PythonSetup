import http
import requests

def get_user_name(user_id: int) -> str:
    url: str = f"https://api.example.com/users/{user_id}"
    response = requests.get(url)
    if response.status_code == http.HTTPStatus.OK:
        return response.json()['name']
    else:
        return None
