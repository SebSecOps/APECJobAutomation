from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import config
import config.settings as config

username = config.APEC_USERNAME
password = config.APEC_PASSWORD

def login_to_apec(driver, wait):
    try:
        driver.get('https://www.apec.fr/')

        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
            accept_cookies_button.click()
        except Exception as e:
            logger.info("Aucune bannière de cookies détectée ou déjà acceptée.")

        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='nav-link nav-link-espace' and @aria-label='Mon espace']")))
        login_button.click()

        username_field = wait.until(EC.visibility_of_element_located((By.ID, 'emailid')))
        password_field = wait.until(EC.visibility_of_element_located((By.ID, 'password')))

        username_field.send_keys(username)
        password_field.send_keys(password)
        password_field.send_keys(Keys.RETURN)

        time.sleep(2)

        if "mon espace" in driver.page_source.lower():
            logger.info("Vous êtes connnecté en tant que : " + config.APEC_USERNAME)
            cookies = driver.get_cookies()
            return cookies
        else:
            logger.error("Connexion échouée.")
            return False
    except Exception as e:
        logger.error(f"Erreur lors de la connexion : {e}")
        return False
