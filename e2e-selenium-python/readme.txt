Ejercicio Automatización E2E - SauceDemo

Opción seleccionada:
Opción 2 de Automatización E2E - SauceDemo.

Tecnologías utilizadas:
- Python
- Pytest
- Selenium WebDriver
- WebDriver Manager
- Pytest HTML

Flujo automatizado:
1. Iniciar sesión con usuario estándar.
2. Agregar dos productos al carrito.
3. Visualizar el carrito.
4. Completar el formulario de compra.
5. Finalizar la compra.
6. Validar mensaje de confirmación.

Estructura:
- config/config_local.ini: configuración de ambiente, usuario y datos de compra.
- config/web_locators.ini: locators utilizados por la prueba.
- Devsu/utilidades/config_utils.py: lectura de archivos .ini.
- Devsu/utilidades/logs_utils.py: manejo de logs.
- Devsu/utilidades/process_utils.py: inicialización de Selenium WebDriver.
- Devsu/utilidades/web_utils.py: funciones reutilizables para acciones web.
- Devsu/tests/Web/compra/test_compra_saucedemo.py: caso automatizado E2E.
- Devsu/reports/e2e_report.html: reporte HTML de ejecución.
- logs/execution.log: log de ejecución.
- screenshots/: evidencias en caso de error.

Pasos de ejecución:

1. Ingresar a la carpeta del ejercicio:
cd e2e-selenium-python

2. Crear ambiente virtual:
python3.12 -m venv venv

3. Activar ambiente virtual:
source venv/bin/activate

4. Instalar dependencias:
pip install -r requirements.txt

5. Ejecutar el flujo E2E:
pytest -m compra

6. Ejecutar el archivo directamente:
pytest Devsu/tests/Web/compra/test_compra_saucedemo.py

7. Consultar reporte:
Devsu/reports/e2e_report.html