import requests
import json
from loguru import logger

def fetch_massive_offer(cookies):
    url = "https://www.apec.fr/cms/webservices/rechercheOffre"
    payload = {
        "lieux": ["75"],
        "fonctions": [],
        "statutPoste": [],
        "typesContrat": [],
        "typesConvention": ["143686", "143687", "143684", "143685"],
        "niveauxExperience": [],
        "idsEtablissement": [],
        "secteursActivite": [],
        "typesTeletravail": [],
        "idNomZonesDeplacement": [],
        "positionNumbersExcluded": [],
        "typeClient": "CADRE",
        "sorts": [{"type": "SCORE", "direction": "DESCENDING"}],
        "pagination": {"range": 100, "startIndex": 0},
        "activeFiltre": True,
        "pointGeolocDeReference": {"distance": 0},
        "salaireMinimum": "45",
        "salaireMaximum": "200",
        "motsCles": "" # Adapter selon votre choix
    }
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Connection": "keep-alive"
    }

    cookies_dict = {cookie['name']: cookie['value'] for cookie in cookies}

    try:
        response = requests.post(url, headers=headers, cookies=cookies_dict, data=json.dumps(payload))
        response.raise_for_status()
        offers = response.json()
        
        if 'resultats' in offers:
            return offers['resultats']
        else:
            logger.error("Clé 'results' non trouvée dans la réponse de l'API.")
            return None
    except requests.exceptions.RequestException as e:
        logger.error(f"Erreur lors de la récupération des offres : {e}")
        return None