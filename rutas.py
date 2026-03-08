import requests

BASE_URL = "https://api.open-meteo.com/v1/forecast"

countries_coords = {
    "spain": (40.4168, -3.7038),
    "france": (48.8566, 2.3522),
    "japan": (35.6762, 139.6503),
    "usa": (38.9072, -77.0369)
}


def get_coordinates(country):

    return countries_coords.get(country.lower())


def get_weather(latitude, longitude):

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current_weather": True
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        return None

    data = response.json()

    return data["current_weather"]


def format_weather(weather):

    temp = weather["temperature"]
    wind = weather["windspeed"]

    text = f"""
Current Temperature: {temp}°C
Wind Speed: {wind} km/h
"""

    return text


def get_weather_summary(lat, lon):

    weather = get_weather(lat, lon)

    if weather:
        return format_weather(weather)

    return "Weather data unavailable"