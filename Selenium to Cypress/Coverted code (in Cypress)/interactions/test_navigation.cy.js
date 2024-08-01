describe('Test script migration from Selenium to Cypress', () => {
    it('should navigate and assert page titles correctly', () => {
      // Visit the first URL
      cy.visit('https://www.selenium.dev');
      
      // Visit the second URL
      cy.visit('https://www.selenium.dev/selenium/web/index.html');
      
      // Assert the title is "Index of Available Pages"
      cy.title().should('eq', 'Index of Available Pages');
      
      // Go back to the previous page
      cy.go('back');
      
      // Assert the title is "Selenium"
      cy.title().should('eq', 'Selenium');
      
      // Go forward to the next page
      cy.go('forward');
      
      // Assert the title is "Index of Available Pages"
      cy.title().should('eq', 'Index of Available Pages');
      
      // Refresh the page
      cy.reload();
      
      // Assert the title is still "Index of Available Pages"
      cy.title().should('eq', 'Index of Available Pages');
    });
  });
  