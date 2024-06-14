# main.py
# josedaniel_chinea_marrero

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from login_page.reject_cookies import reject_cookies_automation
from login_page.inputs_login import inputs_login
from main_menu import main_menu

username = 'gemiliano_charizard'  # Reemplaza con el nombre de usuario
password = 'u_38002508'  # Reemplaza con tu contraseña

driver = webdriver.Safari()
driver.get("https://www.instagram.com")

try:
    reject_cookies_automation(driver)
    inputs_login(username, password, driver)
    main_menu(driver)

except Exception as e:
    print(f"Error: {e}")

finally:
    print(f"Cerrando TOTALMENTE el programa...")
    driver.quit()
