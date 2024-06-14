# main_follow_users.py
# josedaniel_chinea_marrero
import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def follow_users(driver, accounts):
    print("Siguiendo usuarios... Iniciando la lógica para seguir usuarios...")
    try:
        for account in accounts:
            print(f"Procesando la cuenta: {account}")

            # Abrir la página de la cuenta específica
            driver.get(f"https://www.instagram.com/{account}/")

            # Esperar hasta que el perfil esté cargado
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "header"))
            )

            # Hacer clic en el enlace de seguidores
            followers_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "followers"))
            )
            followers_link.click()

            # Esperar hasta que la ventana emergente de seguidores esté cargada
            followers_popup = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div[role='dialog']"))
            )

            # Desplazarse y seguir a los usuarios
            while True:
                # Encuentra todos los botones de "Seguir"
                follow_buttons = followers_popup.find_elements(By.XPATH, "//button[text()='Follow']")

                if not follow_buttons:
                    break  # Salir del bucle si no hay más botones "Seguir"

                for button in follow_buttons:
                    try:
                        button.click()
                        # Esperar un tiempo aleatorio entre 2 y 5 segundos para evitar ser bloqueado por Instagram
                        time.sleep(random.uniform(2, 5))
                    except Exception as e:
                        print(f"Error al seguir al usuario: {e}")
                        continue

                # Desplazar hacia abajo en la ventana emergente de seguidores
                driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup)
                time.sleep(2)

    except Exception as e:
        print(f"Error al seguir usuarios: {e}")

