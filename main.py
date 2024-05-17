from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from src.detail_offers import get_offer_details
from src.login import login_to_apec
from src.view_count import get_profile_views
from src.fetch_offers import fetch_offers
from src.fetch_massive_offer import fetch_massive_offer
from src.view_send_cv import get_candidature_count
from src.send_cv import send_cv

def main():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--log-level=3") 
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)

    cookies = login_to_apec(driver, wait)

    if cookies:
        while True:
            print("\nMenu :")
            print("1 - Voir le nombre de personnes qui ont vu mon profil")
            print("2 - Voir les offres d'emploi recommandées")
            print("3 - Envoyer automatiquement les demandes de candidature")
            print("4 - Voir le nombre de candidature envoyé")
            print("5 - Voir toutes les offres d'emploi")
            print("6 - Envoyer automatiquement les demandes de candidature massivement")
            print("7 - Quitter")
            choice = input("Sélectionnez une option : ")

            if choice == '1':
                get_profile_views(driver, wait)
            elif choice == '2':
                offers = fetch_offers(cookies)
                if offers:
                    for offer in offers:
                        score_affinite = offer['scoreAffinite']
                        intitule = offer['detailOffre']['intitule']
                        numero_offre = offer['detailOffre']['numeroOffre']
                        score_percentage = int(score_affinite * 100)
                        print(f"[{score_percentage}%] - {intitule}")

                        get_offer_details(driver, numero_offre)
                else:
                    print("Aucune offre récupérée.")
            elif choice == '3':
                offers = fetch_offers(cookies)
                if offers:
                    for offer in offers:
                        numero_offre = offer['detailOffre']['numeroOffre']
                        success = send_cv(driver, numero_offre)
                        if success:
                            print(f"Candidature envoyée avec succès pour l'offre {numero_offre}")
                        else:
                            print(f"Échec de l'envoi de la candidature pour l'offre {numero_offre}")
                else:
                    print("Aucune offre récupérée.")
            elif choice == '4':
                get_candidature_count(cookies)
            elif choice == '5':
                offers = fetch_massive_offer(cookies)
                if offers:
                    for offer in offers:
                        intitule = offer['intitule']
                        numero_offre = offer['numeroOffre']
                        print(f"[{intitule}")

                        get_offer_details(driver, numero_offre)
                else:
                    print("Aucune offre récupérée.")
            elif choice == '6':
                offers = fetch_massive_offer(cookies)
                if offers:
                    for offer in offers:
                        numero_offre = offer['numeroOffre']
                        success = send_cv(driver, numero_offre)
                        if success:
                            print(f"Candidature envoyée avec succès pour l'offre {numero_offre}")
                        else:
                            print(f"Échec de l'envoi de la candidature pour l'offre {numero_offre}")
                else:
                    print("Aucune offre récupérée.")         
            elif choice == '7':
                break
            else:
                print("Option invalide. Veuillez réessayer.")
    else:
        print("Connexion échouée. Impossible de récupérer les offres.")

    driver.quit()

if __name__ == "__main__":
    main()
