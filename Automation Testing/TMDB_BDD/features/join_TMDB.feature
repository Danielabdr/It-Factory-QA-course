Feature: This feature will verify the behaviour of the create account functionality in oder to ensure proper functionality
  @T2
  Scenario: Verify that when the user inserts valid data into the input fields, then he will be able to create an account
    Given I am on TMDB home page
    When I click on the Join TMDB link
    When I insert "Daniela1234" on the username field
    When I insert "parola123456789" on the password field
    When I insert "parola123456789" on the confirmation password field
    When I insert "Daniela.daniela12@yahoo.com" on the email field
    When I click Sign In button
    Then the user will be directed to a page with a message saying that he needs to activate the account from the email recieved

