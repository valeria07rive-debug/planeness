import requests

BASE_URL = "https://api.open-meteo.com/v1/forecast"

countries_coords = {
    "spain": (40.4168, -3.7038),
    "france": (48.8566, 2.3522),
    "japan": (35.6762, 139.6503),
    "usa": (38.9072, -77.0369)
}

countries_info = {
    "spain": {
        "capital": "Madrid",
        "language": "Spanish",
        "currency": "Euro"
    },
    "france": {
        "capital": "Paris",
        "language": "French",
        "currency": "Euro"
    },
    "japan": {
        "capital": "Tokyo",
        "language": "Japanese",
        "currency": "Yen"
    },
    "usa": {
        "capital": "Washington, D.C.",
        "language": "English",
        "currency": "US Dollar"
    }
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


def get_country_data(country):
    return countries_info.get(country.lower())


def format_country_info(data):
    if not data:
        return "Country information not found"

    text = f"""
Capital: {data['capital']}
Language: {data['language']}
Currency: {data['currency']}
"""
    return text