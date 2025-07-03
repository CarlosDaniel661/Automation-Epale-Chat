import pytest
import sys
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import allure
import os
import base64
from datetime import datetime

# Asegura que Python encuentre los módulos en utils/
sys.path.append(str(Path(__file__).parent.parent))

from utils.config import Config

@pytest.fixture(scope="function")
def browser(request):
    """Fixture para inicializar y configurar el navegador Chrome
    """
    options = Options()
    
    # Configuración básica del navegador
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--lang=es")
    
    if Config.HEADLESS:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    # Inicialización con webdriver-manager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    
    # Configura tiempoouts implícitos
    driver.implicitly_wait(Config.TIMEOUT)
    
    # Crea directorios para evidencias
    os.makedirs("artifacts/screenshots", exist_ok=True)
    
    yield driver
    
    # Toma screenshot si la prueba falló
    if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = f"artifacts/screenshots/fail_{request.node.name}_{timestamp}.png"
            driver.save_screenshot(screenshot_path)
            
            # Adjunta screenshot a Allure
            allure.attach.file(
                screenshot_path,
                name="Screenshot on failure",
                attachment_type=allure.attachment_type.PNG
            )
            
            # Adjunta screenshot al reporte HTML
            with open(screenshot_path, "rb") as f:
                html = f'<div><img src="data:image/png;base64,{base64.b64encode(f.read()).decode()}" style="width:600px;"></div>'
                if hasattr(request.config, '_html'):
                    request.config._html.extras.append(html)
        except Exception as e:
            print(f"No se pudo capturar screenshot: {str(e)}")
    
    # Cierra el navegador
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook para generar reportes detallados
    
    Args:
        item: Objeto de prueba pytest
        call: Información de la llamada de prueba
    """
    outcome = yield
    rep = outcome.get_result()
    
    # Almacena el resultado en el nodo de prueba
    setattr(item, f"rep_{rep.when}", rep)
    
    # Manejo especial para errores durante la configuración
    if rep.when == "setup" and rep.failed:
        if hasattr(item, 'funcargs') and 'browser' in item.funcargs:
            browser = item.funcargs['browser']
            try:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                screenshot_path = f"artifacts/screenshots/setup_fail_{item.name}_{timestamp}.png"
                browser.save_screenshot(screenshot_path)
                allure.attach.file(
                    screenshot_path,
                    name="Setup failed",
                    attachment_type=allure.attachment_type.PNG
                )
            except Exception as e:
                print(f"Error capturando screenshot de setup: {str(e)}")