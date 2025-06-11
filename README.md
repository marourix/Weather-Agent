# Assistant Météo

Un assistant météo intelligent qui utilise l'API Ollama avec le modèle Llama pour fournir des informations météorologiques en français.

## Prérequis

- Python 3.7+
- Ollama installé et en cours d'exécution sur `localhost:11434`
- Le modèle Llama 3.2 installé dans Ollama

## Installation

1. Clonez ce dépôt :
```bash
git clone [URL_DE_VOTRE_REPO]
cd [NOM_DU_DOSSIER]
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Utilisation

1. Assurez-vous qu'Ollama est en cours d'exécution sur votre machine
2. Lancez l'assistant :
```bash
python agent.py
```

3. Posez vos questions météo en français, par exemple :
- "Quel temps fait-il à Paris ?"
- "Quelles sont les prévisions pour Lyon sur 3 jours ?"
- "Faut-il prendre un parapluie à Marseille aujourd'hui ?"
- "Quels vêtements porter à Bordeaux ?"

## Fonctionnalités

- Météo actuelle
- Prévisions sur plusieurs jours
- Prévisions horaires
- Alertes météo
- Conseils vestimentaires
- Résolution de localisation

## Structure du Projet

- `agent.py` : Script principal de l'assistant
- `tools/` : Dossier contenant les différents outils météo
- `requirements.txt` : Liste des dépendances Python
- `README.md` : Documentation du projet

## Note

Cet assistant utilise l'API Ollama avec le modèle Llama 3.2. Assurez-vous d'avoir Ollama installé et configuré correctement sur votre machine. 