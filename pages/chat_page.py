from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class ChatPage(BasePage):
    """Page Object para la página de chat de Epale.chat"""
    
    # Selectores
    MESSAGE_INPUT = (By.ID, "message-input")
    SEND_BUTTON = (By.ID, "send-btn")
    LAST_MESSAGE = (By.XPATH, "(//div[contains(@class,'message-text')])[last()]")

    def send_message(self, message):
        """
        Envía un mensaje al chat
        """
        self.logger.info(f"Sending message: {message}")
        self.send_keys(self.MESSAGE_INPUT, message)
        self.click(self.SEND_BUTTON)
        time.sleep(1)  # espera 1 seg para asegurar el envío

    def get_last_message(self):
        """
        Obtiene el último mensaje visible en el chat
        """
        if self.is_element_present(self.LAST_MESSAGE):
            return self.driver.find_element(*self.LAST_MESSAGE).text
        return None