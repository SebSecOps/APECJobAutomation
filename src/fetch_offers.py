import requests
import json
from loguru import logger

def fetch_offers(cookies):
    url = "https://www.apec.fr/cms/webservices/affiniteOrchestration/matching-candidat"
    payload = {
        "criteres": {
            "idCadre": 953325630,
            "secteurActivitePoids": 4,
            "salairePoids": 4,
            "metierPoids": 4,
            "lieuxPoids": 4,
            "categoryPoids": 9,
            "includePartner": False
        },
        "offset": 0,
        "limit": 100
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

        if 'results' in offers:
            sorted_offers = sorted(offers['results'], key=lambda x: x['scoreAffinite'], reverse=True)
            return sorted_offers
        else:
            logger.error("Clé 'results' non trouvée dans la réponse de l'API.")
            return None
    except requests.exceptions.RequestException as e:
        logger.error(f"Erreur lors de la récupération des offres : {e}")
        return None