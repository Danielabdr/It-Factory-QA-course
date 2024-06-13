UnitTest - Automation Testing for TMDB (The movie Database)

1. Test Setup

a) Install libraries
pip install selenium
pip install html-testRunner
pip install seleniumbase

b) Define test structure
- test_files (starting with test_)
- test suite (in the file called suite)

2. Libraries used:
- from unittest import TestCase
- from selenium.webdriver import Keys
- from selenium.webdriver.common.by import By
- from selenium.webdriver.support.select import Select
- from seleniumbase import Driver 
- import HtmlTestRunner

3. Running the tests
- can be done by running the entire test suite, which will start the running of all the tests in the classes that were called in the test suite
- the running will be done based on a runner defined as an instance of class HTMLTestRunner

4. Test results
Through running the test suites I have obtained a number of eleven executed tests, which all passed. 
The tests that were passed are the following:
- test_check_creating_list_possible_with_name_containing_letters_numbers_and_special_characters 
- test_check_user_is_able_to_delete_a_list
- test_check_login_not_possible_when_user_and_pass_empty
- test_check_login_with_valid_data
- test_check_if_can_reset_password
- test_check_signup_not_possible_when_fields_empty
- test_check_signup_not_possible_with_username_containing_special_characters
- test_check_signup_not_possible_with_username_too_long
- test_check_signup_not_possible_with_password_less_than_four_characters
- test_check_signup_not_possible_with_wrong_confirmation_password
- test_check_signup_not_possible_with_invalid_email


5. Performance indicators:
- in order to make the code more efficient the most suitable selectors were found in order to be able to identify the web elements in consequence, id or link text selectors were used as means of identification, except when the specifics of a web element required otherwise.
- also, CSS selector was preferred to XPATH selector since it is usually faster. Nevertheless, whenever I needed to search for an element that was not able to be found with CSS selector, XPATH selector was used
- also, the usage of a sleep instruction was reduced as much as possible and as a general trend the waits are to be preferred to the sleep instruction
