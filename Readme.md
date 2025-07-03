# 🚀 Automatización de Epale.chat

Proyecto de automatización para la plataforma Epale.chat que verifica el envío y recepción de mensajes en el chat, implementando las mejores prácticas de automatización de pruebas UI.

## 📌 Requerimientos del proyecto

- [x] Automatizar el envío de mensajes
- [x] Verificar visualización correcta de mensajes
- [x] Implementar Page Object Model (POM)
- [x] Generar reportes y evidencias
- [x] Documentación clara

## 🛠️ Stack Tecnológico

| Tecnología         | Versión | Propósito Principal                     | Beneficio Clave                                  |
|--------------------|---------|-----------------------------------------|--------------------------------------------------|
| **Python**         | 3.8+    | Lenguaje principal                      | Sintaxis clara y amplio soporte para testing     |
| **Selenium**       | 4.15.2  | Automatización del navegador            | Soporte multiplataforma y multi-navegador        |
| **pytest**         | 7.4.3   | Framework de pruebas                    | Fixtures avanzadas y reportes detallados         |
| **Allure**         | 2.13.2  | Reportes interactivos                   | Visualización profesional de resultados          |
| **Page Objects**   | -       | Patrón de diseño                        | Código mantenible y reusable                   


## ⚙️ Por qué este stack?

1. **Selenium WebDriver**:
   - Estándar industrial para automatización web
   - Compatibilidad con múltiples navegadores
   - Comunidad activa y soporte extendido

2. **pytest**:
   - Más potente que unittest tradicional
   - Soporte nativo para parametrización
   - Ecosistema rico de plugins

3. **Allure Framework**:
   - Reportes ejecutivos con detalles técnicos
   - Integración con CI/CD pipelines
   - Soporte para attachments (screenshots, logs)

4. **Page Object Model**:
   - Reduce duplicación de código
   - Facilita mantenimiento
   - Separa lógica de pruebas de locators


## 🏗️ Estructura del Proyecto

```bash
automation_epale/
├── artifacts/              # Evidencias y reportes
│   ├── allure/             # Reportes Allure
│   ├── logs/               # Logs de ejecución
│   └── screenshots/        # Capturas de error
├── pages/                  # Page Objects
│   ├── base_page.py        # Clase base con métodos comunes
│   ├── login_page.py       # Página de login
│   └── chat_page.py        # Página del chat
├── tests/                  # Casos de prueba
│   ├── conftest.py         # Configuración de pytest
│   └── test_message.py     # Prueba principal
├── utils/                  # Utilidades
│   ├── config.py           # Configuración global
│   └── logger.py           # Sistema de logging
├── pytest.ini              # Configuración de pytest
├── requirements.txt        # Dependencias
└── README.md               # Este archivo
```

## 🚀 Cómo Ejecutar las Pruebas
# Prerrequisitos
 - Python 3.8+ instalado
 - Google Chrome instalado
 - Git (opcional)


## 🛠️ Instalación
# Clonar repositorio (si aplica)
git clone [https://github.com/CarlosDaniel661/Automation-Epale-Chat.git]
cd automation_epale

# Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt


# Ejecución de Pruebas
# Opción 1: Ejecución básica con reporte HTML
pytest tests/ --html=artifacts/report.html --self-contained-html

# Opción 2: Ejecución con Allure (reporte interactivo)
pytest tests/ --alluredir=artifacts/allure
allure serve artifacts/allure

# Opción 3: Ejecución en modo headless (sin interfaz gráfica)
* Editar HEADLESS = True en utilities/config.py


## 📊 Generación de Evidencias

# El proyecto genera automáticamente:

1. Reporte HTML: artifacts/report.html
2. Reporte Allure: Carpeta artifacts/allure/
3. Screenshots: En artifacts/screenshots/ cuando fallan pruebas
4. Logs de ejecución: En artifacts/logs/test_execution.log


🤝 Contribución

1. Haz fork del proyecto

2. Crea una rama (git checkout -b feature/nueva-funcionalidad)

3. Haz commit de tus cambios (git commit -m 'Add some feature')

4. Haz push a la rama (git push origin feature/nueva-funcionalidad)

5. Abre un Pull Request

📧 Contacto

[Carlos Daniel Jiménez Cálcena] - [carlos.danielj1291@gmail.com]
[LinkedIn/https://www.linkedin.com/in/carlos-daniel-jim%C3%A9nez-c%C3%A1lcena-07a77a180/TuPerfil]
[GitHub/CarlosDaniel661]