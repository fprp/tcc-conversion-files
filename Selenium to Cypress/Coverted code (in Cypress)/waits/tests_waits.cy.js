describe('Selenium to Cypress Migration', () => {
    beforeEach(() => {
        cy.visit('https://www.selenium.dev/selenium/web/dynamic.html')
    })

    it('test_fails', () => {
        cy.get('#adder').click()

        cy.get('#box0').should('not.exist')
    })

    it('test_sleep', () => {
        cy.get('#adder').click()

        cy.wait(5000)
        cy.get('#box0').should('have.class', 'redbox')
    })

    it('test_implicit', () => {
        cy.get('#adder').click()

        cy.get('#box0').should('have.class', 'redbox')
    })

    it('test_explicit', () => {
        cy.get('#reveal').click()

        cy.get('#revealed', { timeout: 2000 }).should('be.visible')
        cy.get('#revealed').type('Displayed')
        cy.get('#revealed').should('have.value', 'Displayed')
    })

    it('test_explicit_options', () => {
        cy.get('#reveal').click()

        cy.get('#revealed', { timeout: 2000 }).should('be.visible')
        cy.get('#revealed').type('Displayed')
        cy.get('#revealed').should('have.value', 'Displayed')
    })
})
