import requests
from config import OPENWEATHER_API_KEY
from agents import function_tool
from typing import Dict, Optional

@function_tool
def get_current_weather(location: str, units: Optional[str] = "celsius") -> Dict:
    """Get current weather conditions for a location."""
    
    unit_map = {"celsius": "metric", "fahrenheit": "imperial"}
    api_units = unit_map.get(units, "metric")
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={OPENWEATHER_API_KEY}&units={api_units}"
    response = requests.get(url)
    data = response.json()

    return {
        "location": data.get("name"),
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "wind_speed": data["wind"]["speed"],
        "visibility": data.get("visibility", 0)
    }
