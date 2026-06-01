describe("Swagger Petstore - User API", () => {
  const TestData = {
    updatedFirstName: "Carlos",
    updatedEmail: "juan_actualizado@test.com"
  };

  it("Crear, consultar, actualizar, consultar actualizado y eliminar usuario", () => {
    cy.fixture("user").then((user) => {
      const updatedUser = {
        ...user,
        firstName: TestData.updatedFirstName,
        email: TestData.updatedEmail
      };

      cy.log("Crear usuario");
      cy.createUser(user).then((response) => {
        expect(response.status).to.be.oneOf([200, 201]);
        expect(response.body).to.have.property("message");
      });

      cy.log("Buscar usuario creado");
      cy.getUser(user.username).then((response) => {
        expect(response.status).to.eq(200);
        expect(response.body.username).to.eq(user.username);
        expect(response.body.email).to.eq(user.email);
      });

      cy.log("Actualizar nombre y correo del usuario");
      cy.updateUser(user.username, updatedUser).then((response) => {
        expect(response.status).to.eq(200);
        expect(response.body).to.have.property("message");
      });

      cy.log("Buscar usuario actualizado");
      cy.getUser(user.username).then((response) => {
        expect(response.status).to.eq(200);
        expect(response.body.username).to.eq(user.username);
        expect(response.body.firstName).to.eq(TestData.updatedFirstName);
        expect(response.body.email).to.eq(TestData.updatedEmail);
      });

      cy.log("Eliminar usuario");
      cy.deleteUser(user.username).then((response) => {
        expect(response.status).to.eq(200);
      });

      cy.log("Validar usuario eliminado");
      cy.getUser(user.username).then((response) => {
        expect(response.status).to.eq(404);
      });
    });
  });
});