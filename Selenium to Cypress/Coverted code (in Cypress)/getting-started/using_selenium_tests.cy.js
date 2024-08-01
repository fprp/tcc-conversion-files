describe('Test Eight Components', () => {
    it('should submit the form and display the message', () => {
        // Visit the web form
        cy.visit('https://www.selenium.dev/selenium/web/web-form.html');

        // Verify the title
        cy.title().should('eq', 'Web form');

        // Wait for elements to load (implicit wait)
        cy.wait(500);

        // Find the text box and submit button
        cy.get('input[name="my-text"]').type('Selenium');
        cy.get('button').click();

        // Verify the message
        cy.get('#message').should('have.text', 'Received!');
    });
});
