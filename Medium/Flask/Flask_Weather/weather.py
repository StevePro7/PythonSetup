import requests
from http import HTTPStatus

def get_weather(city):
    api_key = "your_api_key_here"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}"

    response = requests.get(complete_url)
    if response.status_code == HTTPStatus.OK:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather_description = data['weather'][0]['description']

        return {
            'temperature': main['temp'],
            'pressure': main['pressure'],
            'humidity': main['humidity'],
            'wind_speed': wind['speed'],
            'description': weather_description
    else:
        return None

if __name__ == "__main__":
    city = input("Enter city name: ")
    weather = get_weather(city)
    if weather:
        print(f"Temperature: {weather['temperature']}")
        print(f"Pressure: {weather['pressure']}")
        print(f"Humidity: {weather['humidity']}")
        print(f"Wind Speed: {weather['wind_speed']}")
        print(f"Description: {weather['description']}")
    else:
        print("City not found!")
