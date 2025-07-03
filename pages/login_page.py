from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    """Page Object para la página de login de Epale.chat"""
    
    # Selectores
    USERNAME_INPUT = (By.CSS_SELECTOR, "input[placeholder='Ingresa tu email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[placeholder='Ingresa tu contraseña']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(., 'ENTRAR')]")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "div.mantine-Alert-message")

    def login(self, username, password):
        """
        Realiza el proceso de login
        """
        self.logger.info(f"Logging in with user: {username}")
        self.clear_and_send_keys(self.USERNAME_INPUT, username)
        self.clear_and_send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        """
        Obtiene el mensaje de error si existe
        """
        if self.is_element_present(self.ERROR_MESSAGE):
            return self.driver.find_element(*self.ERROR_MESSAGE).text
        return None