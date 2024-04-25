Feature: This feature will verify the behaviour of the list functionality in oder to ensure proper functionality
  @T7
  Scenario: Verify that the user can create a movie list with name containg letters, numbers and special characters
    Given I am on the user account page
    When I click lists
    When I click create list
    And I insert "AutomatedList12@#" into the name input field
    And I click continue button
    Then I should be able to create the list