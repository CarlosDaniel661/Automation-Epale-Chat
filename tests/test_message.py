import pytest
import allure
from pages.login_page import LoginPage
from pages.chat_page import ChatPage
from utils.config import Config

@allure.feature("Epale.chat Message Automation")
class TestEpaleChat:
    """Clase que contiene los tests de automatización para Epale.chat"""
    
    @allure.story("Send and verify message")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_send_message(self, browser):
        """Prueba que verifica el envío y visualización de un mensaje"""
        TEST_MESSAGE = "Hola, soy un mensaje automático"

        with allure.step("1. Login to Epale.chat"):
            login_page = LoginPage(browser)
            browser.get(Config.BASE_URL)
            login_page.login(Config.USERNAME, Config.PASSWORD)

        with allure.step("2. Send message"):
            chat_page = ChatPage(browser)
            chat_page.send_message(TEST_MESSAGE)

        with allure.step("3. Verify message in chat"):
            last_message = chat_page.get_last_message()
            assert last_message == TEST_MESSAGE, \
                f"Expected: '{TEST_MESSAGE}', Actual: '{last_message}'"