import time

import softest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seleniumbase import Driver


class Test_Signup(softest.TestCase):
    ACCEPT_COOKIES_BUTTON = (By.CSS_SELECTOR, 'button[id = "onetrust-accept-btn-handler"]')
    JOIN_TMDB_LINK = (By.XPATH, '/html/body/div[1]/header/div[1]/div/div[2]/ul/li[4]/a')
    SIGN_UP_BUTTON = (By.CSS_SELECTOR, 'input#sign_up_button')
    REQUIRED_FIELDS_ERROR_MESSAGE = (By.XPATH, '//*[@id="main"]/div/div/div/div/section/div/div/div/div/ul')
    username = (By.XPATH, '//*[@id="username"]')
    password = (By.XPATH, '//*[@id="password"]')
    confirm_password = (By.XPATH, '//*[@id="password_confirm"]')
    email = (By.XPATH, '//*[@id="email"]')
    USERNAME_ERROR_MESSAGE = (By.XPATH, '//*[@id="main"]/div/div/div/div/section/div/div/div/div/ul')
    PASSWORD_ERROR_MESSAGE = (By.XPATH, '//*[@id="main"]/div/div/div/div/section/div/div/div/div/ul')



    def setUp(self) -> None:
        self.driver = Driver()
        self.driver.get('https://www.themoviedb.org/')
        self.driver.maximize_window()
        self.driver.find_element(*self.ACCEPT_COOKIES_BUTTON).click()
        self.driver.find_element(*self.JOIN_TMDB_LINK).click()



    def tearDown(self) -> None:
        self.driver.quit()

    def test_check_signup_not_possible_when_fields_empty(self):
        signup_button = self.driver.find_element(*self.SIGN_UP_BUTTON)
        signup_button.click()
        required_fields_error = self.driver.find_elements(*self.REQUIRED_FIELDS_ERROR_MESSAGE)
        expected_error_messages = [
            "Email is required",
            "Password is required",
            "Username is required",
            "Password can't be blank",
            "Password confirm can't be blank",
            "Password needs to be at least 4 characters long",
            "Email does not appear to be valid"
        ]
        for error_message in required_fields_error:
            assert any(expected_message in error_message.text for expected_message in expected_error_messages), "Error: The error message is incorrect"

    def test_check_signup_not_possible_with_username_containing_special_characters(self):
        username_input = self.driver.find_element(*self.username)
        username_input.send_keys("Daniela()_@#>?")
        password_input = self.driver.find_element(*self.password)
        password_input.send_keys("123456789")
        password_confirm_input = self.driver.find_element(*self.confirm_password)
        password_confirm_input.send_keys("123456789")
        email_input = self.driver.find_element(*self.email)
        email_input.send_keys("daniela@yahoo.com")
        signup_button = self.driver.find_element(*self.SIGN_UP_BUTTON)
        signup_button.click()
        username_error = self.driver.find_elements(*self.USERNAME_ERROR_MESSAGE)
        expected_error_messages = [
            "Username cannot contain ampersands",
            "Username cannot contain question marks",
            "Username cannot contain plus signs",
            "Username cannot contain percentage signs",
            "Username cannot contain brackets"
        ]
        for error_message in username_error:
            assert any(expected_message in error_message.text for expected_message in expected_error_messages), "Error: The error message is incorrect"

    def test_check_signup_not_possible_with_username_too_long(self):
        username_input = self.driver.find_element(*self.username)
        username_input.send_keys("Daniela()_@#>?SDFSDFDSF213156456456456wkjhsidhfoisjodifjskdjfkjsdbfihsjhfdytdgfxdgcghv>")
        password_input = self.driver.find_element(*self.password)
        password_input.send_keys("123456789")
        password_confirm_input = self.driver.find_element(*self.confirm_password)
        password_confirm_input.send_keys("123456789")
        email_input = self.driver.find_element(*self.email)
        email_input.send_keys("daniela@yahoo.com")
        signup_button = self.driver.find_element(*self.SIGN_UP_BUTTON)
        signup_button.click()
        username_errors = self.driver.find_elements(*self.USERNAME_ERROR_MESSAGE)

        # Așteapta pana cand mesajele de eroare pentru numele de utilizator devin vizibile
        username_errors = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(self.USERNAME_ERROR_MESSAGE))
        expected_error_message = "Username is too long (maximum is 32 characters)"
        is_error_correct = False
        for error in username_errors:
            if error.text == expected_error_message:
                is_error_correct = True
                break
        assert is_error_correct == False, f"Error: The expected error message '{expected_error_message}' was not found"


    def test_check_signup_not_possible_with_less_than_four_characters(self):
        username_input = self.driver.find_element(*self.username)
        username_input.send_keys(
            "Daniela()_@#>?SDFSDFDSF213156456456456wkjhsidhfoisjodifjskdjfkjsdbfihsjhfdytdgfxdgcghv>")
        password_input = self.driver.find_element(*self.password)
        password_input.send_keys("123")
        time.sleep(3)
        password_confirm_input = self.driver.find_element(*self.confirm_password)
        password_confirm_input.send_keys("123")
        email_input = self.driver.find_element(*self.email)
        email_input.send_keys("daniela@yahoo.com")
        signup_button = self.driver.find_element(*self.SIGN_UP_BUTTON)
        signup_button.click()
        password_errors = self.driver.find_elements(*self.PASSWORD_ERROR_MESSAGE)

        # Așteapta pana cand mesajele de eroare pentru numele de utilizator devin vizibile
        password_errors = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.PASSWORD_ERROR_MESSAGE))
        expected_error_message = "Password needs to be at least 4 characters long"
        is_error_correct = False
        for error in password_errors:
            if error.text == expected_error_message:
                is_error_correct = True
                break
        assert is_error_correct == False, f"Error: The expected error message '{expected_error_message}' was not found"


    def test_check_signup_not_possible_with_wrong_confirmation_password(self):
        username_input = self.driver.find_element(*self.username)
        username_input.send_keys("Danielabdr")
        password_input = self.driver.find_element(*self.password)
        password_input.send_keys("123456")
        time.sleep(3)
        password_confirm_input = self.driver.find_element(*self.confirm_password)
        password_confirm_input.send_keys("123")
        email_input = self.driver.find_element(*self.email)
        email_input.send_keys("danielaa@yahoo.com")
        signup_button = self.driver.find_element(*self.SIGN_UP_BUTTON)
        signup_button.click()
        password_errors = self.driver.find_elements(*self.PASSWORD_ERROR_MESSAGE)

        # Așteapta pana cand mesajele de eroare pentru numele de utilizator devin vizibile
        password_errors = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.PASSWORD_ERROR_MESSAGE))
        expected_error_message = "Password and password confirmation do not match"
        is_error_correct = False
        for error in password_errors:
            if error.text == expected_error_message:
                is_error_correct = True
                break
        assert is_error_correct == False, f"Error: The expected error message '{expected_error_message}' was not found"


    def test_check_signup_not_possible_with_invalid_email(self):
        username_input = self.driver.find_element(*self.username)
        username_input.send_keys("Danielabdr")
        password_input = self.driver.find_element(*self.password)
        password_input.send_keys("123456")
        time.sleep(3)
        password_confirm_input = self.driver.find_element(*self.confirm_password)
        password_confirm_input.send_keys("123456")
        email_input = self.driver.find_element(*self.email)
        email_input.send_keys("daniela.bd@yahoo.comkjbjbjbbjbkj3156465456454!@#%$^&*()_+<>")
        signup_button = self.driver.find_element(*self.SIGN_UP_BUTTON)
        signup_button.click()
        password_errors = self.driver.find_elements(*self.PASSWORD_ERROR_MESSAGE)

        # Așteapta pana cand mesajele de eroare pentru numele de utilizator devin vizibile
        password_errors = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_all_elements_located(self.PASSWORD_ERROR_MESSAGE))
        expected_error_message = "Email does not appear to be valid"
        is_error_correct = False
        for error in password_errors:
            if error.text == expected_error_message:
                is_error_correct = True
                break
        assert is_error_correct == False, f"Error: The expected error message '{expected_error_message}' was not found"


