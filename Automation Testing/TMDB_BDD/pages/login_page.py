from selenium.webdriver.common.by import By

from pages.base_page import Base_page


class LoginPage(Base_page):
    LOGIN_LINK = (By.XPATH, '/html/body/div[1]/header/div[1]/div/div[2]/ul/li[3]/a')
    USERNAME_FIELD = (By.XPATH, '//input[@id="username"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@id="password"]')
    LOGIN_BUTTON = (By.XPATH, '//input[@id="login_button"]')
    USERNAME_AND_PASSWORD_ERROR_MESSAGE = (By.XPATH, '//div[@class="content"]/ul')
    ATTEMPTS_ERROR_MESSAGE = (By.XPATH, '//*[@id="main"]/div/div/div/div/h2')
    def navigate_to_login_page(self):
        self.driver.find_element(*self.LOGIN_LINK).click()

    def insert_username(self, username):
        self.enter_text(*self.USERNAME_FIELD, username)

    def insert_password(self, password):
        self.enter_text(*self.PASSWORD_FIELD, password)

    def insert_username_password_11_times(self, username, password):
        for _ in range(11):
            self.insert_username(username)
            self.insert_password(password)
            self.click_login_button()
            if _ == 10:
                self.check_attempts_error_message("Nu mai există încercări de conectare")
            else:
                self.check_error_message("Username or password is invalid. Please try again")

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def check_user_not_logged(self):
        current_url = self.driver.current_url
        assert "login" in current_url, f'Error: User is logged in'

    def check_error_message(self, error_message):
        actual_message = self.driver.find_element(*self.USERNAME_AND_PASSWORD_ERROR_MESSAGE).text
        assert {actual_message} == {error_message}, f'Error: Actual message: {actual_message}, Expected message: {error_message}'

    def check_attempts_error_message(self, attempts_error_message):
        actual_message = self.driver.find_element(*self.ATTEMPTS_ERROR_MESSAGE).text
        assert {attempts_error_message} == {actual_message}, f'Error: Actual message: {actual_message}, Expected message: {attempts_error_message}t'

