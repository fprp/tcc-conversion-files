describe('Pointer Actions Page', () => {
    beforeEach(() => {
      cy.visit('https://www.selenium.dev/selenium/web/pointerActionsPage.html');
    });
  
    it('should use pen input for pointer actions', () => {
      const centerCoordinates = (element) => {
        const rect = element[0].getBoundingClientRect();
        return {
          centerX: rect.x + rect.width / 2,
          centerY: rect.y + rect.height / 2,
        };
      };
  
      cy.get('#pointerArea').then((pointerArea) => {
        const { centerX, centerY } = centerCoordinates(pointerArea);
  
        cy.wrap(pointerArea)
          .trigger('pointermove', { pointerType: 'pen', pageX: centerX, pageY: centerY, button: -1 })
          .trigger('pointerdown', { pointerType: 'pen', pageX: centerX, pageY: centerY, button: 0 })
          .trigger('pointermove', { pointerType: 'pen', pageX: centerX + 2, pageY: centerY + 2, button: -1 })
          .trigger('pointerup', { pointerType: 'pen', pageX: centerX + 2, pageY: centerY + 2, button: 0 });
  
        cy.get('.pointermove').first().should('contain.text', `pointerType: pen, button: -1, pageX: ${Math.floor(centerX)}, pageY: ${Math.floor(centerY)}`);
        cy.get('.pointerdown').should('contain.text', `pointerType: pen, button: 0, pageX: ${Math.floor(centerX)}, pageY: ${Math.floor(centerY)}`);
        cy.get('.pointermove').eq(1).should('contain.text', `pointerType: pen, button: -1, pageX: ${Math.floor(centerX + 2)}, pageY: ${Math.floor(centerY + 2)}`);
        cy.get('.pointerup').should('contain.text', `pointerType: pen, button: 0, pageX: ${Math.floor(centerX + 2)}, pageY: ${Math.floor(centerY + 2)}`);
      });
    });
  
    it('should set pointer event properties', () => {
      const centerCoordinates = (element) => {
        const rect = element[0].getBoundingClientRect();
        return {
          centerX: rect.x + rect.width / 2,
          centerY: rect.y + rect.height / 2,
        };
      };
  
      cy.get('#pointerArea').then((pointerArea) => {
        const { centerX, centerY } = centerCoordinates(pointerArea);
  
        cy.wrap(pointerArea)
          .trigger('pointermove', { pointerType: 'pen', pageX: centerX, pageY: centerY, button: -1 })
          .trigger('pointerdown', { pointerType: 'pen', pageX: centerX, pageY: centerY, button: 0 })
          .trigger('pointermove', { pointerType: 'pen', pageX: centerX + 2, pageY: centerY + 2, button: -1, tiltX: -72, tiltY: 9, twist: 86 })
          .trigger('pointerup', { pointerType: 'pen', pageX: centerX + 2, pageY: centerY + 2, button: 0 });
  
        cy.get('.pointermove').first().should('contain.text', `pointerType: pen, button: -1, pageX: ${Math.floor(centerX)}, pageY: ${Math.floor(centerY)}`);
        cy.get('.pointerdown').should('contain.text', `pointerType: pen, button: 0, pageX: ${Math.floor(centerX)}, pageY: ${Math.floor(centerY)}`);
        cy.get('.pointermove').eq(1).should('contain.text', `pointerType: pen, button: -1, pageX: ${Math.floor(centerX + 2)}, pageY: ${Math.floor(centerY + 2)}, tiltX: -72, tiltY: 9, twist: 86`);
        cy.get('.pointerup').should('contain.text', `pointerType: pen, button: 0, pageX: ${Math.floor(centerX + 2)}, pageY: ${Math.floor(centerY + 2)}`);
      });
    });
  });
  