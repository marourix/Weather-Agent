import asyncio
from typing import Optional
from agents import Agent, Runner, ModelSettings, OpenAIChatCompletionsModel, AsyncOpenAI
from agents import set_tracing_disabled

from tools.current_weather import get_current_weather
from tools.forecast import get_weather_forecast, get_hourly_forecast
from tools.alerts import get_weather_alerts
from tools.location_resolver import resolve_location
from tools.clothing_advice import suggest_weather_clothing

# Désactiver le traçage pour plus de performance
set_tracing_disabled(True)

# Configuration du modèle
model = OpenAIChatCompletionsModel(
    model="llama3.2",
    openai_client=AsyncOpenAI(
        base_url="http://localhost:11434/v1",
        api_key="nokeyneeded"
    )
)

AGENT_INSTRUCTIONS = """
Tu es un assistant météo français. Tu dois répondre à toutes les requêtes météo des utilisateurs de manière naturelle et utile.

OUTILS DISPONIBLES :

1. MÉTÉO ACTUELLE
- Outil : get_current_weather
- Paramètres :
  - location : nom de la ville
  - units : 'celsius'
- Format de réponse : "[ville] maintenant : [température]°C, [condition], vent [vitesse]m/s, humidité [%], visibilité [km]"

2. PRÉVISIONS MÉTÉO
- Outil : get_weather_forecast
- Paramètres :
  - location : nom de la ville
  - days : nombre de jours (entre 1 et 7)
  - units : 'celsius'
- Format : "[ville], prévisions sur [X] jours :
  * [jour de la semaine] : [min]-[max]°C, [condition], risque de pluie : [%]"
- Important : Utiliser les vrais jours de la semaine (lundi, mardi, etc.) en fonction de la date actuelle

3. PRÉVISIONS HORAIRES
- Outil : get_hourly_forecast
- Paramètres :
  - location : nom de la ville
  - hours : nombre d'heures (entre 12 et 48)
  - units : 'celsius'
- Format : "[ville], prévisions horaires :
  * [heure]h : [température]°C, [condition]"

4. ALERTES MÉTÉO
- Outil : get_weather_alerts
- Paramètres :
  - location : nom de la ville
- Format : "[ville] : [type d'alerte] - [description] (niveau : [severity])"
  ou "Aucune alerte météo active pour [ville]"

5. LOCALISATION
- Outil : resolve_location
- Paramètres :
  - location_query : nom du lieu
- Format : "[lieu] : coordonnées [latitude], [longitude]"

6. CONSEILS VESTIMENTAIRES
- Outil : suggest_weather_clothing
- Paramètres :
  - current_weather : données météo actuelles (OBLIGATOIRE)
  - activity : activité spécifique (OPTIONNEL)
- Format : "[ville] ([température]°C) :
  Recommandations vestimentaires :
  - [conseil 1]
  - [conseil 2]"

RÈGLES IMPORTANTES :
1. Comprendre l'intention de la question avant de choisir l'outil
2. Toujours utiliser les unités métriques (°C)
3. Pour les questions sur le parapluie :
   - Utiliser get_weather_forecast pour voir le risque de pluie
   - Répondre clairement si un parapluie est nécessaire ou non
4. Pour les questions sur les vêtements :
   - D'abord appeler get_current_weather
   - Puis utiliser suggest_weather_clothing
5. Ne jamais inventer de données météo
6. Répondre de manière naturelle et utile
7. Ne jamais afficher les détails techniques ou les noms des outils
8. Toujours vérifier la validité de la ville avant de répondre
9. Pour les alertes, vérifier d'abord si la ville existe
10. Si aucune alerte n'est trouvée, répondre "Aucune alerte météo active pour [ville]"
11. Pour les prévisions horaires, toujours indiquer l'heure locale
12. Pour les prévisions journalières, indiquer les températures min/max
13. Pour les prévisions, toujours utiliser les vrais jours de la semaine en fonction de la date actuelle

TRADUCTIONS CONDITIONS MÉTÉO :
- clear sky → dégagé
- few clouds → peu nuageux
- scattered clouds → partiellement nuageux
- broken clouds → nuageux
- shower rain → averses
- rain → pluie
- thunderstorm → orage
- snow → neige
- mist → brumeux

MESSAGES D'ERREUR :
- "❌ Ville non trouvée"
- "❌ Données météo indisponibles"
- "❌ Service indisponible"
"""


# Création de l'agent
agent = Agent(
    name="Assistant Météo",
    instructions=AGENT_INSTRUCTIONS,
    tools=[
        get_current_weather,
        get_weather_forecast,
        get_hourly_forecast,
        get_weather_alerts,
        resolve_location,
        suggest_weather_clothing
    ],
    model=model
)

async def stream_response(user_input: str):
    """Gère le streaming des réponses de l'agent.
    
    Args:
        user_input: Question de l'utilisateur
    """
    try:
        # Extraire la ville de la question
        city = user_input.split('à')[-1].strip().replace('?', '').strip()
        
        # Laisser l'agent décider quel outil utiliser en fonction de la question
        result = Runner.run_streamed(agent, user_input)
        
        # Afficher la réponse
        async for event in result.stream_events():
            if event.type == "raw_response_event" and hasattr(event.data, 'delta'):
                content = event.data.delta
                if not content.strip().startswith("{") and not content.strip().endswith("}"):
                    print(content, end="", flush=True)
        
        print("\n")
                
    except Exception as e:
        print(f"❌ Une erreur est survenue : {str(e)}")
        print("Veuillez réessayer avec une autre question.")

if __name__ == "__main__":
    print("Assistant Météo — tapez 'exit' pour quitter.\n")
    
    while True:
        try:
            user_input = input("Posez votre question météo : ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ["exit", "quit", "q"]:
                print("À bientôt ! 👋")
                break
                
            asyncio.run(stream_response(user_input))
            
            
        except KeyboardInterrupt:
            print("\nÀ bientôt ! 👋")
            break
        except Exception as e:
            print(f"❌ Une erreur est survenue : {str(e)}")