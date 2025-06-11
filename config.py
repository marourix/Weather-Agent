import os
from typing import Dict, Optional
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

# Configuration API
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY', '')
OPENWEATHER_BASE_URL = 'http://api.openweathermap.org/data/2.5'
OPENWEATHER_GEO_URL = 'http://api.openweathermap.org/geo/1.0'

# Timeouts et limites
REQUEST_TIMEOUT = 10  # secondes
MAX_RETRIES = 3
CACHE_DURATION = 300  # 5 minutes

# Unités et formats
UNITS_CONFIG: Dict[str, Dict[str, str]] = {
    'celsius': {
        'api': 'metric',
        'temp': '°C',
        'speed': 'km/h',
        'speed_multiplier': 3.6
    },
    'fahrenheit': {
        'api': 'imperial',
        'temp': '°F',
        'speed': 'mph',
        'speed_multiplier': 1
    }
}

DEFAULT_UNITS = 'celsius'
DEFAULT_LANGUAGE = 'fr'

# Messages d'erreur
ERROR_MESSAGES = {
    'no_api_key': ("⚠️ La clé API OpenWeather n'est pas configurée!\n"
                   "1. Créez un compte sur https://openweathermap.org/api\n"
                   "2. Obtenez votre clé API\n"
                   "3. Ajoutez la ligne: OPENWEATHER_API_KEY=votre_clé_api"),
    'invalid_api_key': "⚠️ Clé API OpenWeather invalide. Veuillez vérifier votre configuration.",
    'city_not_found': "❌ Ville non trouvée : {}",
    'connection_error': "🔌 Erreur de connexion. Vérifiez votre connexion internet.",
    'timeout_error': "⏱️ Délai d'attente dépassé. Veuillez réessayer.",
    'api_error': "❌ Erreur API ({}) pour {}"
}

# Emojis pour les conditions météo
WEATHER_EMOJIS: Dict[str, str] = {
    'thunderstorm': '⛈️',  # 200-299
    'drizzle': '🌧️',      # 300-399
    'rain': '🌧️',         # 500-599
    'snow': '🌨️',         # 600-699
    'mist': '🌫️',         # 700-799
    'clear': '☀️',         # 800
    'clouds': '☁️'         # 801-899
}

def get_weather_emoji(weather_id: int) -> str:
    """Retourne l'emoji approprié pour un code météo donné."""
    if 200 <= weather_id < 300:
        return WEATHER_EMOJIS['thunderstorm']
    elif 300 <= weather_id < 400:
        return WEATHER_EMOJIS['drizzle']
    elif 400 <= weather_id < 600:
        return WEATHER_EMOJIS['rain']
    elif 600 <= weather_id < 700:
        return WEATHER_EMOJIS['snow']
    elif 700 <= weather_id < 800:
        return WEATHER_EMOJIS['mist']
    elif weather_id == 800:
        return WEATHER_EMOJIS['clear']
    else:
        return WEATHER_EMOJIS['clouds']

def get_units_config(units: Optional[str] = None) -> Dict[str, str]:
    """Retourne la configuration des unités."""
    return UNITS_CONFIG.get(units or DEFAULT_UNITS, UNITS_CONFIG[DEFAULT_UNITS])
