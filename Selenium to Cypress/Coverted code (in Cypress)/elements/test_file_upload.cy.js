describe('File Upload Test', () => {
    it('should upload a file successfully', () => {
      // Visit the URL
      cy.visit('https://the-internet.herokuapp.com/upload');
  
      // Define the file to be uploaded
      const filePath = '../selenium-snapshot.png';
  
      // Attach the file
      cy.get('input[type="file"]').attachFile(filePath);
  
      // Click the submit button
      cy.get('#file-submit').click();
  
      // Assert that the uploaded file name is correct
      cy.get('#uploaded-files').should('include.text', 'selenium-snapshot.png');
    });
  });

// for this test case you will need install the plugin cypress-file-upload: npm install --save-dev cypress-file-upload
// and add the following line to the file cypress/support/commands.js: import 'cypress-file-upload';
  