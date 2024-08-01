describe('Popup Tests', () => {
    const url = "https://www.selenium.dev/documentation/webdriver/interactions/alerts/";
  
    it('Test Alert Popup', () => {
      cy.visit(url);
      cy.contains('See an example alert').click();
      
      cy.on('window:alert', (text) => {
        expect(text).to.equal('Sample alert');
      });
    });
  
    it('Test Confirm Popup', () => {
      cy.visit(url);
      cy.contains('See a sample confirm').click();
      
      cy.on('window:confirm', (text) => {
        expect(text).to.equal('Are you sure?');
        return false; // Simulate dismissing the confirm popup
      });
    });
  
    it('Test Prompt Popup', () => {
      cy.visit(url);
      cy.window().then((win) => {
        cy.stub(win, 'prompt').returns('Selenium');
      });
      cy.contains('See a sample prompt').click();
      
      cy.on('window:prompt', (text) => {
        expect(text).to.equal('What is your tool of choice?');
      });
    });
  });
  