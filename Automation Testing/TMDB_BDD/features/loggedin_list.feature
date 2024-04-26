Feature: This feature will verify the behaviour of the list functionality in oder to ensure proper functionality
  @T7-ok
  Scenario: Verify that the user can create a movie list with name containg letters, numbers and special characters
    Given I am on the user account page
    When I click lists
    When I click create list
    And I insert "AutomatedList12@#" into the name input field
    And I click continue button
    Then I should be able to create the list and a succes message will appear

  @T8-ok
  Scenario: Verify that the user can add an item to a movie list
    Given I am on the user account page
    When I click lists
    When I click on a list
    When I click Edit button
    When I click Add/Edit Items
    When I insert "King Kong" text into Add Item field
    When I click first movie from the movie dropdown
    Then I click save button and a succes message should appear

  @T9-ok
  Scenario: Verify that the user can delete a list
    Given I am on the user account page
    When I click lists
    When I click on "AutomatedList"
    When I click Edit button
    When I click Delete List button
    When I click Delete button
    Then I click Yes button and the list should be deleted

