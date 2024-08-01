describe('Selenium to Cypress Migration', () => {
    it('should navigate to Selenium website and verify title and URL', () => {
      // Visit the Selenium website
      cy.visit('https://www.selenium.dev')
  
      // Verify the title of the page
      cy.title().should('eq', 'Selenium')
  
      // Verify the current URL
      cy.url().should('eq', 'https://www.selenium.dev/')
    })
  })