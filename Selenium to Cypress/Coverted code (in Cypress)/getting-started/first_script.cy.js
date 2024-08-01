describe('Web Form Test', () => {
    it('fills and submits the form', () => {
      // Visit the web form page
      cy.visit('https://www.selenium.dev/selenium/web/web-form.html');
  
      // Check the title of the page
      cy.title().should('eq', 'Web form');
  
      // Implicit wait can be handled by Cypress' built-in retry mechanism
      // Type "Selenium" into the text box
      cy.get('input[name="my-text"]').type('Selenium');
  
      // Click the submit button
      cy.get('button').click();
  
      // Verify the message
      cy.get('#message').should('have.text', 'Received!');
    });
  });