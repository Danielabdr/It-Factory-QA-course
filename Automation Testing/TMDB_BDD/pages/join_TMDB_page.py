import random

from selenium.webdriver.common.by import By

from pages.base_page import Base_page


class JoinTMDBPage(Base_page):
    USERNAME_FIELD = (By.XPATH, '//input[@id="username"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@id="password"]')
    CONFIRM_PASSWORD_FIELD = (By.XPATH, '//input[@id="password_confirm"]')
    EMAIL_FIELD = (By.XPATH, '//input[@id="email"]')
    SIGN_IN_BUTTON = (By.XPATH, '//input[@id="sign_up_button"]')
    JOIN_TMDB_MESSAGE = (By.XPATH, '//div[@class="error_wrapper"]')




    def insert_username(self, username):
        number = random.randint(0, 9999999)
        username_input = str(number) + username
        self.enter_text(*self.USERNAME_FIELD, username_input)

    def insert_password(self, password):
        self.enter_text(*self.PASSWORD_FIELD, password)

    def insert_confirm_password(self, confirm_password):
        self.enter_text(*self.CONFIRM_PASSWORD_FIELD, confirm_password)

    def insert_email(self, email):
        number = random.randint(0, 99999)
        email_input = str(number) + email
        self.enter_text(*self.EMAIL_FIELD, email_input)

    def click_sign_in_button(self):
        self.driver.find_element(*self.SIGN_IN_BUTTON).click()

    def check_join_TMDB_message(self):
        current_url = self.driver.current_url
        actual_message = self.driver.find_element(*self.JOIN_TMDB_MESSAGE).text
        expected_message = "Your email address hasn't been verified. Please click the verification link in the email that was sent to the address you signed up with. (Don't forget to check your spam folder.) You may request the email be resent if you are unable to locate your activation email."
        assert 'signup' in current_url
        assert actual_message == expected_message, (f'Error: Expected message: {expected_message} Actual message: {actual_message}')

