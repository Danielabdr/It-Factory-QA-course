Feature: This feature will verify the behaviour of the log in functionality in oder to ensure proper functionality
  @T3-ok
  Scenario: Verify that when the user inserts valid data into the input fields, then he is able to log into the application
    Given I am on TMDB home page
    When I click on the Login link
    When I insert username "Danielabdr"
    When I insert password "Tmdb1994@#@#"
    When I click on the Login button
    Then I should be able to log into the application

  @T4-ok
  Scenario Outline: Verify that when the user inserts invalid data into the log in fields, then he is not able to log into the application
    Given I am on TMDB home page
    When I click on the Login link
    When I insert username "<username>"
    When I insert password "<password>"
    When I click on the Login button
    Then I receive an error message "<error_message>"

    Examples:
      | username       | password     | error_message                 |
      | Anamaria28936  | Test         | Username or password invalid. |
      | Danielabdr     | test1        | Username or password invalid. |
      | Maria12344@#$% | Tmdb1994@#@# | Username or password invalid. |
    #Valid credentials :
    # username: Danielabdr
    # password: Tmdb1994@#@#

  @T5
#  Scenario Outline: Verify that when the user inserts invalid data into the log in fields more than 10 times,
#    he is not able to log into the application and an error message is displayed saying that he used all the login attempts
#      Given I am on TMDB home page
#      When I click on the Login link
#      When I try to login 11 times with "<username>" and "<password>" and I click login button
#      Then I receive an error message "<error_message>"
#      Then I receive an attempts error message "Nu mai există încercări de conectare"
#
#      Examples:
#        | username        | password        | error_message                                     |
#        | anamiaria maria | testestestest   | Username or password is invalid. Please try again |
#        | Danielabdr      | 123456789123456 | Username or password is invalid. Please try again |
#        | Maria12344@#$%  | Tmdb1994@#@#    | Username or password is invalid. Please try again |
#        | anamiariamaria  | testestestest   | Username or password is invalid. Please try again |
#        | Danielabdr      | 123456789123456 | Username or password is invalid. Please try again |
#        | Maria12344@#$%  | Tmdb1994@#@#    | Username or password is invalid. Please try again |
#        | anamiariamaria  | testestestest   | Username or password is invalid. Please try again |
#        | Danielabdr      | 123456789123456 | Username or password is invalid. Please try again |
#        | Maria12344@#$%  | Tmdb1994@#@#    | Username or password is invalid. Please try again |
#        | anamiariamaria  | testestestest   | Username or password is invalid. Please try again |
#        | anamiariamaria  | testestestest   | Username or password is invalid. Please try again |

  @T6
  Scenario: Verify that when the user doesn't insert data into the log in fields, then he is not able to log into the application
      Given I am on TMDB home page
      When I click on the Login link
      When I click on the Login button
      Then I should not be able to log into the application

