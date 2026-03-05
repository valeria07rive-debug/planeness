import requests

BASE_URL = "https://restcountries.com/v3.1/name/"

def get_country_data(country_name):
    url = BASE_URL + country_name
    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()[0]

    country_info = {
        "name": data["name"]["official"],
        "capital": data.get("capital", ["Unknown"])[0],
        "region": data.get("region", "Unknown"),
        "subregion": data.get("subregion", "Unknown"),
        "population": data.get("population", 0),
        "currencies": list(data.get("currencies", {}).keys()),
        "languages": list(data.get("languages", {}).values()),
        "timezone": data.get("timezones", []),
        "flag": data["flags"]["png"]
    }

    return country_info
def format_country_info(country):
    text = f"""
Country: {country['name']}
Capital: {country['capital']}
Region: {country['region']}
Subregion: {country['subregion']}
Population: {country['population']}
Currencies: {', '.join(country['currencies'])}
Languages: {', '.join(country['languages'])}
Timezones: {', '.join(country['timezone'])}
"""
    return text
