from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger

def get_profile_views(driver, wait):
    try:
        driver.get('https://www.apec.fr/candidat/mon-espace.html#/')

        views_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".metrics-visited__number .number")))

        views_count = views_element.text

        logger.info(f"Nombre de recruteurs ayant visité votre profil : {views_count}")
        return views_count
    except Exception as e:
        logger.error(f"Erreur lors de la récupération du nombre de recruteurs : {e}")
        return None
