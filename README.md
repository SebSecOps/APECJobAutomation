# APECJobAutomation

## Description

**APECJobAutomation** est un bot Python pour automatiser les tâches sur le site de l'APEC. Il permet de voir les visites de profil, consulter les offres d'emploi recommandées, envoyer des candidatures automatiquement, suivre les candidatures envoyées et gérer les candidatures efficacement. Simplifiez votre recherche d'emploi avec ce bot automatisé.

## Fonctionnalités

Le script principal offre un menu interactif avec les options suivantes :

1. Voir le nombre de personnes qui ont vu votre profil.
2. Voir les offres d'emploi recommandées.
3. Envoyer automatiquement des demandes de candidature.
4. Voir le nombre de candidatures envoyées.
5. Voir toutes les offres d'emploi disponibles.
6. Envoyer des candidatures massivement.
7. Quitter le programme.

## Configuration du fichier `settings.py`

Avant de pouvoir utiliser le script, vous devez configurer le fichier `settings.py` avec vos informations d'authentification et d'autres paramètres nécessaires. Voici un exemple de ce à quoi pourrait ressembler `settings.py` :

```python
# settings.py

# Identifiants de connexion à l'APEC
APEC_USERNAME = 'votre_nom_utilisateur'
APEC_PASSWORD = 'votre_mot_de_passe'
```

Remplacez `'votre_nom_utilisateur'`, `'votre_mot_de_passe'` par vos propres informations.

## Installation des dépendances

Les dépendances nécessaires pour ce projet sont listées dans le fichier `requirements.txt`. Vous pouvez les installer en utilisant la commande suivante :

```sh
pip install -r requirements.txt
```

## Exécution du script

Pour exécuter le script principal, utilisez la commande suivante dans votre terminal :

```sh
python main.py
```

## Fonctionnement général

1. **Connexion** : Le script se connecte au site de l'APEC en utilisant les informations d'identification fournies dans `settings.py`.
2. **Récupération des offres** : Le script peut récupérer les offres d'emploi recommandées et toutes les offres disponibles.
3. **Envoi de candidatures** : Le script peut envoyer des candidatures automatiquement pour les offres sélectionnées ou envoyer des candidatures massivement pour plusieurs offres.

Ce projet est conçu pour faciliter la recherche et la candidature à des offres d'emploi sur le site de l'APEC, en automatisant les processus répétitifs et en permettant de gérer les candidatures de manière plus efficace.
