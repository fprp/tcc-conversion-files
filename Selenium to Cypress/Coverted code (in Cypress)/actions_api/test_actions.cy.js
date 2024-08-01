describe('Test mouse interactions', () => {
    // Test for pauses and duration
    it('should pause and perform actions within expected duration', () => {
        const start = Date.now();
        
        cy.visit('https://selenium.dev/selenium/web/mouse_interaction.html');
        
        cy.get('#clickable')
            .trigger('mouseover')
            .wait(1000)
            .trigger('mousedown')
            .wait(1000)
            .type('abc');

        cy.then(() => {
            const duration = (Date.now() - start) / 1000;
            expect(duration).to.be.greaterThan(2);
            expect(duration).to.be.lessThan(3);
        });
    });

    // Test for releasing all keys
    it('should release all keys and validate the input value', () => {
        cy.visit('https://selenium.dev/selenium/web/mouse_interaction.html');
        
        cy.get('#clickable')
            .trigger('mousedown')
            .type('{shift}a', { release: false });
        
        // Clear actions by releasing all keys
        cy.get('body').type('a');
        
        cy.get('#clickable').should(($el) => {
            const value = $el.val();
            expect(value[0]).to.equal('A');
            expect(value[1]).to.equal('a');
        });
    });
});
