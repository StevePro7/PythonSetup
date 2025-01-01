# 15. Automate Weather Updates
import requests


def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    return requests.get(url).json()
