describe('Mouse Interaction Tests', () => {

    beforeEach(() => {
      cy.visit('https://selenium.dev/selenium/web/mouse_interaction.html');
    });
  
    it('test_click_and_hold', () => {
      cy.get('#clickable')
        .trigger('mousedown', { button: 0 });
      cy.wait(500);
      cy.get('#click-status')
        .should('have.text', 'focused');
    });
  
    it('test_click_and_release', () => {
      cy.get('#click')
        .click();
      cy.url()
        .should('include', 'resultPage.html');
    });
  
    it('test_right_click', () => {
      cy.get('#clickable')
        .rightclick();
      cy.wait(500);
      cy.get('#click-status')
        .should('have.text', 'context-clicked');
    });
  
    it('test_back_click_ab', () => {
      cy.get('#click').click();
      cy.title().should('eq', 'We Arrive Here');
      cy.go('back');
      cy.title().should('eq', 'BasicMouseInterfaceTest');
    });
  
    it('test_forward_click_ab', () => {
      cy.get('#click').click();
      cy.go('back');
      cy.title().should('eq', 'BasicMouseInterfaceTest');
      cy.go('forward');
      cy.title().should('eq', 'We Arrive Here');
    });
  
    it('test_double_click', () => {
      cy.get('#clickable')
        .dblclick();
      cy.get('#click-status')
        .should('have.text', 'double-clicked');
    });
  
    it('test_hover', () => {
      cy.get('#hover')
        .trigger('mouseover');
      cy.get('#move-status')
        .should('have.text', 'hovered');
    });
  
    it('test_move_by_offset_from_element', () => {
      cy.get('#mouse-tracker')
        .trigger('mousemove', 8, 0);
      cy.get('#relative-location')
        .invoke('text')
        .then(text => {
          const coordinates = text.split(', ');
          console.log(coordinates);
          expect(Math.abs(parseInt(coordinates[0]) - 100 - 8)).to.be.lessThan(2);
        });
    });
  
    it('test_move_by_offset_from_viewport_origin_ab', () => {
      cy.get('body')
        .trigger('mousemove', 8, 0);
      cy.get('#absolute-location')
        .invoke('text')
        .then(text => {
          const coordinates = text.split(', ');
          expect(Math.abs(parseInt(coordinates[0]) - 8)).to.be.lessThan(2);
        });
    });
  
    it('test_move_by_offset_from_current_pointer_ab', () => {
      cy.get('body')
        .trigger('mousemove', 6, 3);
      cy.get('body')
        .trigger('mousemove', 19, 18);
      cy.get('#absolute-location')
        .invoke('text')
        .then(text => {
          const coordinates = text.split(', ');
          expect(Math.abs(parseInt(coordinates[0]) - 6 - 13)).to.be.lessThan(2);
          expect(Math.abs(parseInt(coordinates[1]) - 3 - 15)).to.be.lessThan(2);
        });
    });
  
    it('test_drag_and_drop_onto_element', () => {
      cy.get('#draggable')
        .trigger('mousedown', { which: 1 });
      cy.get('#droppable')
        .trigger('mousemove')
        .trigger('mouseup', { force: true });
      cy.get('#drop-status')
        .should('have.text', 'dropped');
    });
  
    it('test_drag_and_drop_by_offset', () => {
      cy.get('#draggable')
        .then(draggable => {
          const start = draggable[0].getBoundingClientRect();
          cy.get('#droppable')
            .then(droppable => {
              const finish = droppable[0].getBoundingClientRect();
              const offsetX = finish.x - start.x;
              const offsetY = finish.y - start.y;
              cy.get('#draggable')
                .trigger('mousedown', { which: 1 });
              cy.get('#draggable')
                .trigger('mousemove', { clientX: start.x + offsetX, clientY: start.y + offsetY })
                .trigger('mouseup', { force: true });
            });
        });
      cy.get('#drop-status')
        .should('have.text', 'dropped');
    });
  
  });
  