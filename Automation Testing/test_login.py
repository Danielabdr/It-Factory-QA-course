import time
from telnetlib import EC

from selenium.webdriver.support import expected_conditions as EC
import softest


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from seleniumbase import Driver


class Test_Login(softest.TestCase):
    ACCEPT_COOKIES_BUTTON = (By.CSS_SELECTOR, 'button[id = "onetrust-accept-btn-handler"]')
    LOGIN_LINK = (By.XPATH, '/html/body/div[1]/header/div[1]/div/div[2]/ul/li[3]/a')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login_button"]')
    REQUIRED_FIELD_ERROR = (By.XPATH, '//*[@id="main"]/section/div/div/div/div/div/div/ul')
    username_input = (By.XPATH, '//*[@id="username"]')
    password_input = (By.XPATH, '//*[@id="password"]')
    reset_password = (By.XPATH, '//*[@id="login_form"]/div/p/a')
    reset_password_input = (By.XPATH, '//*[@id="email"]')
    reset_continue_button = (By.XPATH, '//*[@class="k-button k-primary"]')

    def setUp(self) -> None:
        self.driver = Driver()
        self.driver.get('https://www.themoviedb.org/')
        self.driver.maximize_window()
        self.driver.find_element(*self.ACCEPT_COOKIES_BUTTON).click()
        self.driver.find_element(*self.LOGIN_LINK).click()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_check_login_not_possible_when_user_and_pass_empty(self):
        time.sleep(2)
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()
        time.sleep(5)

        # Asteapta ca elementul sa fie vizibil
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.REQUIRED_FIELD_ERROR))

        required_field_error_message = self.driver.find_elements(*self.REQUIRED_FIELD_ERROR)
        expected_error_messages = [
            "We couldn't find your username.",
            "You have x remaining login attempts"
        ]
        #parcurgem lista cu mesaje
        for error_message in required_field_error_message:
            assert any(expected_message in error_message.text for expected_message in
                       expected_error_messages), "Error: The error message is incorrect"

        #reidentificarea butonului de login
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)

        # Verifica daca butonul de login este afisat
        is_login_button_displayed = login_button.is_displayed()
        self.assertTrue(is_login_button_displayed, "Error: The login button is not displayed")


    def test_check_login_with_valid_data(self):
        username_input_field = self.driver.find_element(*self.username_input)
        username_input_field.send_keys("Danielabdr")
        password_input_field = self.driver.find_element(*self.password_input)
        password_input_field.send_keys("Tmdb1994@#@#")
        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()

    def test_check_if_can_reset_password(self):
        reset_password_link = self.driver.find_element(*self.reset_password)
        reset_password_link.click()
        self.driver.find_element(*self.reset_password_input).send_keys("daniela.bdrdaniela@yahoo.com")
        continue_button = self.driver.find_element(*self.reset_continue_button)
        continue_button.click()









