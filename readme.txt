Proyecto Devsu QA Automation

Este repositorio contiene dos ejercicios prácticos desarrollados para el proceso de selección de Devsu:

1. Automatización E2E
2. Automatización de APIs

==================================================
1. AUTOMATIZACIÓN E2E
==================================================

Opción seleccionada:
SauceDemo

Carpeta:
e2e-selenium-python

Tecnologías:
- Python
- Pytest
- Selenium WebDriver
- WebDriver Manager
- Pytest HTML

Flujo automatizado:
1. Autenticarse con usuario estándar.
2. Agregar dos productos al carrito.
3. Visualizar el carrito.
4. Completar formulario de compra.
5. Finalizar la compra.
6. Validar mensaje de confirmación.

Pasos de ejecución:

1. Ingresar a la carpeta del proyecto E2E:

cd e2e-selenium-python

2. Crear ambiente virtual, si no existe:

python3.12 -m venv venv

Si python3.12 no está disponible, usar:

python3 -m venv venv

3. Activar ambiente virtual:

source venv/bin/activate

4. Instalar dependencias:

pip install -r requirements.txt

5. Ejecutar prueba E2E:

pytest -m compra

6. Ejecutar prueba por archivo:

pytest devsu/tests/Web/compra/test_compra_saucedemo.py

7. Consultar reporte HTML:

devsu/reports/e2e_report.html

8. Consultar logs:

logs/execution.log


==================================================
2. AUTOMATIZACIÓN DE APIS
==================================================

Opción seleccionada:
Swagger Petstore User

Carpeta:
api-cypress-js

Tecnologías:
- Cypress
- JavaScript
- Node.js

Flujo automatizado:
1. Crear un usuario.
2. Buscar el usuario creado.
3. Actualizar el nombre y correo del usuario.
4. Buscar el usuario actualizado.
5. Eliminar el usuario.
6. Validar eliminación del usuario.

Pasos de ejecución:

1. Ingresar a la carpeta del proyecto API:

cd api-cypress-js

2. Instalar dependencias:

npm install

3. Ejecutar pruebas API por terminal:

npm run cy:run

4. Ejecutar pruebas API en modo visual:

npm run cy:open

5. Consultar evidencias generadas por Cypress:

cypress/videos/
cypress/screenshots/

6. Consultar colección de referencia:

collections/petstore_user_collection.json


==================================================
DOCUMENTACIÓN ADICIONAL
==================================================

Cada ejercicio contiene su propio archivo readme.txt con instrucciones específicas:

- e2e-selenium-python/readme.txt
- api-cypress-js/readme.txt

Cada ejercicio también contiene su propio archivo conclusiones.txt:

- e2e-selenium-python/conclusiones.txt
- api-cypress-js/conclusiones.txt

La raíz del repositorio contiene este readme.txt general y el archivo conclusiones.txt general.