import requests

RESTCOUNTRIES_URL = "https://restcountries.com/v3.1/name/"
OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"


def safe_get(url, params=None):
    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None


def search_country(country_name):
    """
    Searches a country by name using REST Countries.
    Returns a formatted dictionary with the main fields needed by the project.
    """
    data = safe_get(f"{RESTCOUNTRIES_URL}{country_name}")

    if not data or not isinstance(data, list):
        return None

    country = data[0]

    name_data = country.get("name", {})
    currencies_data = country.get("currencies", {})
    languages_data = country.get("languages", {})
    capital_list = country.get("capital", [])
    timezones = country.get("timezones", [])
    latlng = country.get("latlng", [])
    capital_info = country.get("capitalInfo", {})

    currency_list = []
    for code, info in currencies_data.items():
        currency_name = info.get("name", "Unknown")
        currency_symbol = info.get("symbol", "")
        if currency_symbol:
            currency_list.append(f"{currency_name} ({code}, {currency_symbol})")
        else:
            currency_list.append(f"{currency_name} ({code})")

    languages_list = list(languages_data.values()) if languages_data else []

    capital_latlng = capital_info.get("latlng", [])

    result = {
        "common_name": name_data.get("common", "Unknown"),
        "official_name": name_data.get("official", "Unknown"),
        "capital": capital_list[0] if capital_list else "Unknown",
        "region": country.get("region", "Unknown"),
        "subregion": country.get("subregion", "Unknown"),
        "population": country.get("population", "Unknown"),
        "currencies": currency_list if currency_list else ["Unknown"],
        "languages": languages_list if languages_list else ["Unknown"],
        "timezones": timezones if timezones else ["Unknown"],
        "country_code": country.get("cca2", "Unknown"),
        "location": latlng if len(latlng) == 2 else None,
        "capital_location": capital_latlng if len(capital_latlng) == 2 else None,
        "flag": country.get("flags", {}).get("png", "Not available")
    }

    return result


def get_weather(latitude, longitude):
    """
    Gets current weather from Open-Meteo using coordinates.
    """
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m"
    }

    data = safe_get(OPEN_METEO_URL, params=params)

    if not data:
        return None

    current = data.get("current")
    if not current:
        return None

    return {
        "temperature": current.get("temperature_2m", "Unknown"),
        "wind_speed": current.get("wind_speed_10m", "Unknown"),
        "time": current.get("time", "Unknown")
    }


def get_country_weather(country_data):
    """
    Uses capital coordinates if available, otherwise country coordinates.
    """
    coords = country_data.get("capital_location") or country_data.get("location")

    if not coords:
        return None

    lat, lon = coords
    return get_weather(lat, lon)


def format_country_info(country_data):
    if not country_data:
        return "Country information not found."

    languages = ", ".join(country_data["languages"])
    currencies = ", ".join(country_data["currencies"])
    timezones = ", ".join(country_data["timezones"])

    location_text = "Unknown"
    if country_data["location"]:
        location_text = f"Latitude {country_data['location'][0]}, Longitude {country_data['location'][1]}"

    text = (
        f"\nOfficial Name: {country_data['official_name']}\n"
        f"Common Name: {country_data['common_name']}\n"
        f"Capital: {country_data['capital']}\n"
        f"Region: {country_data['region']}\n"
        f"Sub-region: {country_data['subregion']}\n"
        f"Population: {country_data['population']}\n"
        f"Currency: {currencies}\n"
        f"Languages: {languages}\n"
        f"Time zone(s): {timezones}\n"
        f"Country Code: {country_data['country_code']}\n"
        f"Location: {location_text}\n"
        f"Flag URL: {country_data['flag']}\n"
    )

    return text


def format_weather_info(weather_data, capital_name):
    if not weather_data:
        return "Weather information not available."

    return (
        f"\nCurrent weather for {capital_name}:\n"
        f"Temperature: {weather_data['temperature']} °C\n"
        f"Wind Speed: {weather_data['wind_speed']} km/h\n"
        f"Time of report: {weather_data['time']}\n"
    )