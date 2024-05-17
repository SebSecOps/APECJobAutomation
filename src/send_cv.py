from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger
import sys

logger.remove()
logger.add(sys.stdout, format="<green>{time}</green> | <level>{level}</level> | <cyan>{message}</cyan>", level="INFO")

def send_cv(driver, numero_offre):
    detail_url = f"https://www.apec.fr/candidat/recherche-emploi.html/emploi/detail-offre/{numero_offre}"
    driver.get(detail_url)
    logger.info(f"Ouverture de l'URL : {detail_url}")

    try:
        wait = WebDriverWait(driver, 10)
        wait.until(EC.visibility_of_element_located((By.TAG_NAME, "apec-offre-metadata")))
        logger.info("Élément de la page de détail de l'offre trouvé.")

        try:
            postuler_lien = driver.find_element(By.XPATH, f"//a[contains(@href, 'promotion/{numero_offre}') and contains(@class, 'btn btn-primary ml-0')]")
            bouton_texte = postuler_lien.text
            if "Postuler sur le site de l'entreprise" in bouton_texte:
                logger.info("Bouton 'Postuler sur le site de l'entreprise' détecté, passant à l'offre suivante.")
                return False
            postuler_lien.click()
            logger.info("Redirection vers la page de candidature.")

            wait.until(EC.visibility_of_element_located((By.TAG_NAME, "apec-promotion-page")))
            logger.info("Élément de la page de candidature trouvé.")

            try:
                postuler_button = driver.find_element(By.XPATH, "//button[@title='Postuler' and contains(@class, 'btn btn-primary')]")
                postuler_button.click()
                logger.info("Bouton 'Postuler' cliqué.")

                wait.until(EC.visibility_of_element_located((By.TAG_NAME, "apec-candidature-page")))
                logger.info("Élément de la page de soumission de candidature trouvé.")

                try:
                    envoyer_button = driver.find_element(By.XPATH, "//button[@title='Envoyer ma candidature' and @class='btn btn-primary']")
                    if envoyer_button.is_displayed() and envoyer_button.is_enabled():
                        envoyer_button.click()
                        logger.info("Candidature envoyée avec succès (clic natif)")
                    else:
                        logger.warning("Le bouton 'Envoyer ma candidature' n'est pas cliquable.")
                        driver.execute_script("arguments[0].click();", envoyer_button)
                        logger.info("Candidature envoyée avec succès (clic JavaScript)")
                except Exception as e:
                    logger.error(f"Erreur lors du clic sur le bouton 'Envoyer ma candidature' : {e}")
                    return False

            except Exception as e:
                logger.error(f"Erreur lors du clic sur le bouton 'Postuler' : {e}")
                return False

        except Exception as e:
            logger.error(f"Erreur lors de la recherche du bouton 'Postuler' : {e}")
            return False

    except Exception as e:
        logger.error(f"Erreur lors de la navigation vers la page de candidature : {e}")
        return False