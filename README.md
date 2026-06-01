**Devsu QA Automation**

Repositorio desarrollado como parte del ejercicio práctico del proceso de selección de Devsu.

El proyecto contiene dos ejercicios automatizados dentro de un mismo repositorio:

Automatización E2E de un flujo de compra.
Automatización de pruebas API sobre servicios REST.

**Ejercicios seleccionados**
1. Automatización E2E

Opción seleccionada: SauceDemo

URL:
https://www.saucedemo.com/

Flujo automatizado:

Iniciar sesión con usuario estándar.
Agregar dos productos al carrito.
Visualizar el carrito.
Completar el formulario de compra.
Finalizar la compra.
Validar el mensaje de confirmación.

Tecnologías utilizadas:

Python
Pytest
Selenium WebDriver
WebDriver Manager
Pytest HTML

Ubicación del proyecto:

e2e-selenium-python/

2. Automatización de APIs

Opción seleccionada: Swagger Petstore User

URL:
https://petstore.swagger.io/

Flujo automatizado:

Crear un usuario.
Buscar el usuario creado.
Actualizar el nombre y correo del usuario.
Buscar el usuario actualizado.
Eliminar el usuario.
Validar que el usuario fue eliminado.

Tecnologías utilizadas:

Cypress
JavaScript
Node.js

Ubicación del proyecto:

api-cypress-js/

Estructura del repositorio
devsu-qa-automation/
│
├── e2e-selenium-python/
│   ├── config/
│   │   ├── config_local.ini
│   │   └── web_locators.ini
│   │
│   ├── devsu/
│   │   ├── reports/
│   │   ├── tests/
│   │   │   └── Web/
│   │   │       └── compra/
│   │   │           └── test_compra_saucedemo.py
│   │   │
│   │   └── utilidades/
│   │       ├── config_utils.py
│   │       ├── logs_utils.py
│   │       ├── process_utils.py
│   │       └── web_utils.py
│   │
│   ├── logs/
│   ├── screenshots/
│   ├── pytest.ini
│   ├── requirements.txt
│   ├── readme.txt
│   └── conclusiones.txt
│
├── api-cypress-js/
│   ├── collections/
│   │   └── petstore_user_collection.json
│   │
│   ├── cypress/
│   │   ├── e2e/
│   │   │   └── petstore_user.cy.js
│   │   ├── fixtures/
│   │   │   └── user.json
│   │   ├── support/
│   │   │   ├── commands.js
│   │   │   └── e2e.js
│   │   ├── screenshots/
│   │   └── videos/
│   │
│   ├── cypress.config.js
│   ├── package.json
│   ├── readme.txt
│   └── conclusiones.txt
│
├── README.md
├── readme.txt
├── conclusiones.txt
└── .gitignore

**Ejecución del ejercicio E2E**

Ingresar a la carpeta del proyecto E2E:

cd e2e-selenium-python

Crear ambiente virtual:

python3.12 -m venv venv

Activar ambiente virtual:

source venv/bin/activate

Instalar dependencias:

pip install -r requirements.txt

Ejecutar prueba E2E:

pytest -m compra

Ejecutar el archivo directamente:

pytest devsu/tests/Web/compra/test_compra_saucedemo.py

El reporte HTML se genera en:

devsu/reports/e2e_report.html

**Ejecución del ejercicio API**

Ingresar a la carpeta del proyecto API:

cd api-cypress-js

Instalar dependencias:

npm install

Ejecutar pruebas API por terminal:

npm run cy:run

Ejecutar pruebas API en modo visual:

npm run cy:open

Las evidencias generadas por Cypress pueden consultarse en:

cypress/videos/
cypress/screenshots/

La colección de referencia se encuentra en:

collections/petstore_user_collection.json

**Documentación adicional**

Cada ejercicio contiene su propio archivo readme.txt con instrucciones específicas de ejecución:

e2e-selenium-python/readme.txt
api-cypress-js/readme.txt

Cada ejercicio también contiene su propio archivo conclusiones.txt con hallazgos y conclusiones:

e2e-selenium-python/conclusiones.txt
api-cypress-js/conclusiones.txt

Adicionalmente, en la raíz del repositorio se incluyen:

readme.txt
conclusiones.txt

**Hallazgos importantes**

En el ejercicio E2E, el enunciado menciona la validación del mensaje:

GRACIAS POR SU PEDIDO

Sin embargo, la aplicación SauceDemo muestra el mensaje real en inglés:

Thank you for your order!

Por este motivo, la validación automatizada se realiza contra el texto real mostrado por la aplicación.

**Autor**

Desarrollado por Juan Carlos Restrepo como parte del ejercicio práctico de automatización E2E y APIs para Devsu.