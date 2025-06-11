import requests
from config import OPENWEATHER_API_KEY
from agents import function_tool
from typing import Dict, Optional, List

@function_tool
def get_weather_alerts(location: str, severity_level: Optional[str] = None) -> List[Dict]:
    """Get active weather alerts for a location.
    
    Args:
        location (str): Name of the city or location.
        severity_level (str, optional): Filter for alerts by severity (e.g., 'moderate', 'severe').
    
    Returns:
        List[Dict]: List of active weather alerts, each containing:
            - type
            - severity
            - description
            - start_time
            - end_time
    """

    alerts = []
    
    
    if severity_level is None or severity_level == 'moderate':
        alerts.append({
            "type": "wind",
            "severity": "moderate",
            "description": "Strong winds expected",
            "start_time": "2024-03-20T12:00:00",
            "end_time": "2024-03-20T18:00:00"
        })
    
    if severity_level is None or severity_level == 'severe':
        alerts.append({
            "type": "rain",
            "severity": "severe",
            "description": "Heavy rainfall warning",
            "start_time": "2024-03-20T15:00:00",
            "end_time": "2024-03-21T03:00:00"
        })
    
    return alerts
