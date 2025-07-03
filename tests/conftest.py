import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import allure
import os
import base64
from datetime import datetime
from utils.config import Config

@pytest.fixture(scope="function")
def browser(request):
    """Fixture para inicializar el navegador"""
    options = Options()
    options.add_argument("--start-maximized")
    if Config.HEADLESS:
        options.add_argument("--headless=new")
    
    # Inicializa el driver con webdriver-manager
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    
    # Crea directorio para screenshots si es que no existe
    os.makedirs("artifacts/screenshots", exist_ok=True)
    
    yield driver
    
    # Toma screenshot si la prueba falló
    if request.node.rep_call.failed:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        screenshot_path = f"artifacts/screenshots/fail_{request.node.name}_{timestamp}.png"
        driver.save_screenshot(screenshot_path)
        
        # Adjunta screenshot a Allure
        allure.attach.file(screenshot_path, name="Screenshot on failure", 
                         attachment_type=allure.attachment_type.PNG)
        
        # Adjunta screenshot al reporte HTML
        with open(screenshot_path, "rb") as f:
            html = f'<div><img src="data:image/png;base64,{base64.b64encode(f.read()).decode()}" style="width:600px;"></div>'
            pytest_html = request.config.pluginmanager.getplugin("html")
            if pytest_html:
                pytest_html.extras.append(pytest_html.extras.html(html))
    
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook para generar mis reportes de pytest"""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)