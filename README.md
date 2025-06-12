# Assistant Météo Intelligent

Un assistant météo sophistiqué qui utilise l'API Ollama avec le modèle Llama3.2 pour fournir des informations météorologiques détaillées en français. Ce projet démontre l'intégration d'un LLM local avec des outils météorologiques spécialisés.

## Table des matières
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Configuration d'Ollama](#configuration-dollama)
- [Structure du Projet](#structure-du-projet)
- [Outils Intégrés](#outils-intégrés)
- [Gestion des Erreurs](#gestion-des-erreurs)
- [Exemples d'Utilisation](#exemples-dutilisation)
- [Architecture et Conception](#architecture-et-conception)

## Prérequis

- Python 3.7+
- Ollama installé et en cours d'exécution via la commande ( ollama run llama3.2 )
- Connexion Internet pour les API météo
- 4GB+ de RAM pour exécuter le modèle LLM

## Installation

1. Clonez ce dépôt :
```bash
git clone [URL_DE_VOTRE_REPO]
cd [NOM_DU_DOSSIER]
```

2. Créez un environnement virtuel :
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
```

3. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Configuration d'Ollama

1. Téléchargez et installez Ollama depuis [ollama.com](https://ollama.com)

2. Téléchargez le modèle Llama :
```bash
ollama pull llama3.2  _ ou bien d'autre modéle 
```

3. Vérifiez que le modèle fonctionne :
```bash
ollama run llama3.2 
```

## Structure du Projet

```
weather-agent/
├── agent.py              # Script principal de l'assistant
├── tools/               # Dossier des outils météo
│   ├── current_weather.py
│   ├── forecast.py
│   ├── alerts.py
│   ├── location_resolver.py
│   └── clothing_advice.py
├── requirements.txt     # Dépendances Python
├── README.md           # Documentation
└── .gitignore         # Fichiers à ignorer par Git
```

## Outils Intégrés

### 1. Météo Actuelle (`get_current_weather`)
- **Objectif** : Obtenir les conditions météorologiques actuelles
- **Paramètres** : 
  - `location` : Ville
  - `units` : Unités de mesure (celsius)
- **Retour** : Température, conditions, vent, humidité, visibilité

### 2. Prévisions (`get_weather_forecast`)
- **Objectif** : Prévisions sur plusieurs jours
- **Paramètres** :
  - `location` : Ville
  - `days` : Nombre de jours (1-7)
- **Retour** : Températures min/max, conditions, risque de pluie

### 3. Prévisions Horaire (`get_hourly_forecast`)
- **Objectif** : Prévisions détaillées heure par heure
- **Paramètres** :
  - `location` : Ville
  - `hours` : Nombre d'heures (12-48)
- **Retour** : Température et conditions par heure

### 4. Alertes Météo (`get_weather_alerts`)
- **Objectif** : Informer sur les alertes météo actives
- **Paramètres** :
  - `location` : Ville
- **Retour** : Type d'alerte, description, niveau de sévérité

### 5. Résolution de Localisation (`resolve_location`)
- **Objectif** : Convertir les noms de lieux en coordonnées
- **Paramètres** :
  - `location_query` : Nom du lieu
- **Retour** : Latitude, longitude

### 6. Conseils Vestimentaires (`suggest_weather_clothing`)
- **Objectif** : Recommandations vestimentaires basées sur la météo
- **Paramètres** :
  - `current_weather` : Données météo actuelles
  - `activity` : Activité prévue (optionnel)
- **Retour** : Liste de recommandations vestimentaires

## Gestion des Erreurs

L'assistant implémente une gestion robuste des erreurs pour :
- Échecs d'API météo
- Entrées utilisateur invalides
- Problèmes de connexion
- Erreurs de résolution de localisation
- Timeouts et erreurs réseau

Chaque erreur est gérée avec des messages appropriés et des suggestions de récupération.


## Exemples d'Utilisation

### Exemple 1 : Météo Actuelle
```
Utilisateur : "Quel temps fait-il à Casablanca aujourd'hui ?"
Assistant : "Actuellement à Casablanca, il fait 24°C avec un ciel dégagé et une légère brise. C'est une journée parfaite pour les activités en plein air !"
```

### Exemple 2 : Besoin de Parapluie
```
Utilisateur : "Faut-il prendre un parapluie à Paris demain ?"
Assistant : "Oui, il est recommandé de prendre un parapluie. Les prévisions pour Paris demain indiquent un risque de pluie de 70% avec des températures autour de 18°C."
```

### Exemple 3 : Conseils Vestimentaires
```
Utilisateur : "Que dois-je porter à New York ce soir ?"
Assistant : "Ce soir à New York, il fera environ 15°C avec des vents légers. Je recommande :
- Un manteau léger ou un pull
- Des chaussures fermées
- Une écharpe légère"
```

## Architecture et Conception

### Modularité
- Chaque outil est implémenté comme une fonction indépendante
- Interface claire entre les composants
- Facilité d'ajout de nouveaux outils

### Scalabilité
- Architecture extensible pour de nouvelles fonctionnalités
- Support pour l'ajout de nouveaux modèles LLM
- Possibilité d'intégrer d'autres API météo

### Performance
- Utilisation efficace du LLM local
- Mise en cache des réponses fréquentes
- Optimisation des appels API

## Contribution

Les contributions sont les bienvenues ! Veuillez :
1. Fork le projet
2. Créer une branche pour votre fonctionnalité
3. Commiter vos changements
4. Pousser vers la branche
5. Ouvrir une Pull Request

