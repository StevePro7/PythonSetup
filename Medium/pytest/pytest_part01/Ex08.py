from unittest.mock import MagicMock


def test_weather_service() -> None:
    spy_weather_api = MagicMock()
    weather_service = WeatherService(spy_weather_api)
    weather_service.get_weather()
    spy_weather_api.get_weather_data.assert_called_once()