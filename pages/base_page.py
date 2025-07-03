from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import logging

class BasePage:
    """Clase base que contiene métodos comunes para todas las páginas"""
    
    def __init__(self, driver): 
        """define el constructor"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Espera máxima de 10 segundos
        self.logger = logging.getLogger(__name__)

    def click(self, locator):
        """
        Hace clic en un elemento después de esperar que sea clickeable
        """
        try:
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
            self.logger.info(f"Clicked on element: {locator}")
        except TimeoutException:
            self.logger.error(f"Element not clickable: {locator}")
            raise

    def send_keys(self, locator, text):
        """
        Escribe texto en un campo después de esperar que sea visible
        """
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            self.logger.info(f"Sent text '{text}' to element: {locator}")
        except TimeoutException:
            self.logger.error(f"Element not visible: {locator}")
            raise

    def is_element_present(self, locator):
        """
        Verifica si un elemento está presente
        """
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def clear_and_send_keys(self, locator, text):
        """
        Limpia un campo y escribe texto
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)