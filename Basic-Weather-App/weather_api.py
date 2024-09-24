import requests

API_KEY = 'e89156462c6ae7c9615dc0fceda2d571'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'


def fetch_weather_data(city, units='metric'):
    """Fetch weather data from OpenWeather API"""
    params = {
        'q': city,
        'appid': API_KEY,
        'units': units
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an error if the status code is not 200
        return response.json()
    except requests.exceptions.HTTPError as err:
        return None
