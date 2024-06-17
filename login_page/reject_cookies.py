# reject_cookies.py
# josedaniel_chinea_marrero

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def reject_cookies_automation(driver):
    # Intentar localizar el botón de "Decline optional cookies" usando diferentes selectores
    try:
        decline_button = WebDriverWait(driver, 7).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Decline optional cookies']"))
        )
    except TimeoutException:
        decline_button = WebDriverWait(driver, 7).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button._a9--._ap36._a9_1"))
        )

    decline_button.click()

    # Esperar a que la acción anterior se complete
    WebDriverWait(driver, 7).until(EC.staleness_of(decline_button))
