Cypress.Commands.add("createUser", (user) => {
  return cy.request({
    method: "POST",
    url: "/user",
    body: user,
    failOnStatusCode: false
  });
});

Cypress.Commands.add("getUser", (username) => {
  return cy.request({
    method: "GET",
    url: `/user/${username}`,
    failOnStatusCode: false
  });
});

Cypress.Commands.add("updateUser", (username, user) => {
  return cy.request({
    method: "PUT",
    url: `/user/${username}`,
    body: user,
    failOnStatusCode: false
  });
});

Cypress.Commands.add("deleteUser", (username) => {
  return cy.request({
    method: "DELETE",
    url: `/user/${username}`,
    failOnStatusCode: false
  });
});