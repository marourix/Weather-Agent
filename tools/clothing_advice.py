from agents import function_tool
from typing import Optional
from pydantic import BaseModel

class WeatherData(BaseModel):
    temperature: float
    wind_speed: float
    humidity: float

@function_tool
def suggest_weather_clothing(current_weather: WeatherData, activity_type: Optional[str] = None) -> str:
    """Suggest clothing based on weather and optional activity."""

    temperature = current_weather.temperature
    wind_speed = current_weather.wind_speed
    humidity = current_weather.humidity

    suggestion = []

    # Température
    if temperature < 5:
        suggestion.append("Habillez-vous chaudement avec un manteau, une écharpe et un bonnet.")
    elif temperature < 15:
        suggestion.append("Portez une veste ou un pull.")
    elif temperature < 25:
        suggestion.append("Une tenue légère suffit.")
    else:
        suggestion.append("Portez des vêtements très légers et hydratez-vous bien.")

    # Vent
    if wind_speed > 10:
        suggestion.append("Le vent est fort, prévoyez une veste coupe-vent.")

    # Activité
    if activity_type == "running":
        suggestion.append("Optez pour une tenue de sport respirante.")
    elif activity_type == "business meeting":
        suggestion.append("Choisissez une tenue formelle adaptée à la température.")

    return " ".join(suggestion)
