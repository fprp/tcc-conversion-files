/// <reference types="cypress" />

describe('Select Options Tests', () => {
    beforeEach(() => {
      cy.visit('https://selenium.dev/selenium/web/formPage.html');
    });
  
    it('should select options in the select element', () => {
      cy.get('select[name="selectomatic"]').as('selectElement');
  
      cy.get('select[name="selectomatic"]').select('Four');
      cy.get('option[value="four"]').should('be.selected');
  
      cy.get('select[name="selectomatic"]').select('two');
      cy.get('option[value="two"]').should('be.selected');
  
      cy.get('@selectElement').select('still learning how to count, apparently');
      cy.get('option[value="still learning how to count, apparently"]').should('be.selected');
    });
  
    it('should select multiple options in the select element', () => {
      cy.get('select[name="multi"]').as('multiSelectElement');
  
      cy.get('option[value="ham"]').as('hamElement');
      cy.get('option[value="onion gravy"]').as('gravyElement');
      cy.get('option[value="eggs"]').as('eggElement');
      cy.get('option[value="sausages"]').as('sausageElement');
  
      cy.get('@multiSelectElement').then(select => {
        const options = select.find('option');
        const optionList = Array.from(options).map(option => option.value);
        expect(optionList).to.include.members(['ham', 'onion gravy', 'eggs', 'sausages']);
      });
  
      cy.get('@multiSelectElement').invoke('val').should('deep.equal', ['eggs', 'sausages']);
  
      cy.get('@multiSelectElement').select(['ham', 'onion gravy']);
      cy.get('@hamElement').should('be.selected');
      cy.get('@gravyElement').should('be.selected');
  
      cy.get('@multiSelectElement').invoke('val').should('not.include', ['eggs', 'sausages']);
      cy.get('@eggElement').should('not.be.selected');
      cy.get('@sausageElement').should('not.be.selected');
    });
  
    it('should handle disabled options', () => {
      cy.get('select[name="single_disabled"]').as('disabledSelectElement');
  
      cy.get('@disabledSelectElement').find('option').contains('disabled').should('be.disabled');
    });
  });
  