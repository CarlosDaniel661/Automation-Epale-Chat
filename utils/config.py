class Config:
    """Clase de configuración para constantes del proyecto"""
    
    # Configuración de la aplicación
    BASE_URL = "https://web.epale.chat/login"
    TIMEOUT = 10  # Tiempo máximo de espera en segundos
    
    # Configuración del navegador
    HEADLESS = False  # Cambiar a True para ejecución en CI/CD
    
    # Credenciales de prueba
    USERNAME = "cdjc_test_epale@gmail.com"
    PASSWORD = "Test+123"