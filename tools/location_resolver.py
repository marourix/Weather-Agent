import requests
from config import OPENWEATHER_API_KEY
from agents import function_tool
from typing import Dict

@function_tool
def resolve_location(location_query: str) -> Dict:
    """Resolve location name into standardized name and coordinates."""

    url = f"http://api.openweathermap.org/geo/1.0/direct?q={location_query}&limit=1&appid={OPENWEATHER_API_KEY}"
    response = requests.get(url)
    data = response.json()

    if not data:
        raise ValueError("Location not found.")

    loc = data[0]
    return {
        "name": loc["name"],
        "country": loc.get("country", ""),
        "latitude": loc["lat"],
        "longitude": loc["lon"]
    }
