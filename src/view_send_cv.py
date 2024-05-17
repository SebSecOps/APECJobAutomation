import requests
import json
from loguru import logger

def get_candidature_count(cookies):
    url = "https://www.apec.fr/cms/webservices/candidature/liste"
    payload = {
        "criteres": {
            "idCadre": 953325630,
            "dateMinCandidature": "2024-01-18T14:18:01.598Z",
            "tri": {
                "INTITULE_OFFRE": "DESC"
            }
        },
        "limit": 10,
        "offset": 0
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
        data = response.json()
        
        count = data.get("count", 0)
        logger.info(f"Nombre de candidatures envoyées : {count}")
        return count
    except requests.exceptions.RequestException as e:
        logger.error(f"Erreur lors de la requête HTTP : {e}")
        return None
    except ValueError as e:
        logger.error(f"Erreur lors du traitement de la réponse JSON : {e}")
        return None
