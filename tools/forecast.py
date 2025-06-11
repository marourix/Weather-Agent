import requests
from config import OPENWEATHER_API_KEY
from agents import function_tool
from typing import List, Dict, Optional

@function_tool
def get_weather_forecast(location: str, days: int, units: Optional[str] = "celsius") -> List[Dict]:
    """Get multi-day weather forecast (1–7 days)."""

    if not (1 <= days <= 7):
        raise ValueError("Days must be between 1 and 7.")

    unit_map = {"celsius": "metric", "fahrenheit": "imperial"}
    api_units = unit_map.get(units, "metric")

    url = f"http://api.openweathermap.org/data/2.5/forecast/daily?q={location}&cnt={days}&appid={OPENWEATHER_API_KEY}&units={api_units}"
    response = requests.get(url)
    data = response.json()

    forecast = []
    for day in data.get("list", []):
        forecast.append({
            "date": day["dt"],
            "temp_min": day["temp"]["min"],
            "temp_max": day["temp"]["max"],
            "conditions": day["weather"][0]["description"],
            "precipitation_chance": day.get("pop", 0)
        })

    return forecast


@function_tool
def get_hourly_forecast(location: str, hours: int, units: Optional[str] = "celsius") -> List[Dict]:
    """Get hourly weather forecast for next N hours (12–48h)."""

    if not (12 <= hours <= 48):
        raise ValueError("Hours must be between 12 and 48.")

    unit_map = {"celsius": "metric", "fahrenheit": "imperial"}
    api_units = unit_map.get(units, "metric")

    # Fetch coordinates first
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={location}&limit=1&appid={OPENWEATHER_API_KEY}"
    geo_response = requests.get(geo_url).json()
    if not geo_response:
        raise ValueError("Location not found.")
    
    lat = geo_response[0]["lat"]
    lon = geo_response[0]["lon"]

    url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units={api_units}"
    response = requests.get(url)
    data = response.json()

    forecast = []
    for item in data["list"][:hours]:  
        forecast.append({
            "time": item["dt_txt"],
            "temperature": item["main"]["temp"],
            "conditions": item["weather"][0]["description"],
            "wind_speed": item["wind"]["speed"]
        })

    return forecast
