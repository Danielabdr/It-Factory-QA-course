import random

from selenium.webdriver.common.by import By

from pages.base_page import Base_page


class JoinTMDBPage(Base_page):
    USERNAME_FIELD = (By.XPATH, '//input[@id="username"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@id="password"]')
    CONFIRM_PASSWORD_FIELD = (By.XPATH, '//input[@id="password_confirm"]')
    EMAIL_FIELD = (By.XPATH, '//input[@id="email"]')
    SIGN_IN_BUTTON = (By.XPATH, '//input[@id="sign_up_button"]')
    JOIN_TMDB_MESSAGE = (By.CSS_SELECTOR, '#main > div > div > div > div > h2')




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

    def check_join_TMDB_message(self, account_activation_message):
        actual_message = self.driver.find_element(*self.JOIN_TMDB_MESSAGE).text
        assert actual_message == account_activation_message, (f'Error: Expected message: {account_activation_message} Actual message: {actual_message}')

