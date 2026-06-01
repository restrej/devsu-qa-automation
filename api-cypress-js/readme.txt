Ejercicio API - Swagger Petstore User

Opción seleccionada:
Opción 3 de APIs - Swagger Petstore User.

Tecnologías utilizadas:
- Cypress
- JavaScript
- Node.js

Flujo automatizado:
1. Crear un usuario.
2. Buscar el usuario creado.
3. Actualizar el nombre y correo del usuario.
4. Buscar el usuario actualizado.
5. Eliminar el usuario.
6. Validar que el usuario fue eliminado.

Estructura:
- cypress/e2e/petstore_user.cy.js: prueba automatizada API.
- cypress/fixtures/user.json: datos de prueba.
- cypress/support/commands.js: comandos reutilizables para POST, GET, PUT y DELETE.
- cypress.config.js: configuración base de Cypress.
- collections/petstore_user_collection.json: colección de referencia tipo Postman.
- cypress/videos/: evidencia de ejecución si Cypress genera video.
- cypress/screenshots/: screenshots en caso de fallo.

Pasos de ejecución:

1. Ingresar a la carpeta:
cd api-cypress-js

2. Instalar dependencias:
npm install

3. Ejecutar pruebas por terminal:
npm run cy:run

4. Ejecutar pruebas en modo visual:
npm run cy:open