from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger
import sys

logger.remove()
logger.add(sys.stdout, format="<green>{time}</green> | <cyan>{level}</cyan> | <level>{message}</level>", level="INFO")

def get_offer_details(driver, numero_offre):
    url = f"https://www.apec.fr/candidat/recherche-emploi.html/emploi/detail-offre/{numero_offre}?affinite=true&selectedIndex=0&page=0&includePartner=false"
    driver.get(url)

    try:
        wait = WebDriverWait(driver, 20)
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "article")))

        try:
            salaire_element = driver.find_element(By.XPATH, "//div[h4[text()='Salaire']]/span")
            salaire = salaire_element.text if salaire_element else "Salaire non spécifié"
        except Exception as e:
            salaire = "Salaire non spécifié"

        logger.info(f"Détails de l'offre {numero_offre} récupérés avec succès.")
        logger.info(f"Salaire : {salaire}")
        print(" ")
        return salaire
    except Exception as e:
        return None, None