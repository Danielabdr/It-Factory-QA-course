

from selenium.webdriver.common.by import By


from pages.base_page import Base_page


class LoggedinAccountPage(Base_page):
    MY_ACCOUNT_BUTTON = (By.XPATH, '//a[@title="Profile and Settings"]')
    LOG_OUT_BUTTON = (By.LINK_TEXT, 'Logout')

    def check_account_created(self):
        current_url = self.driver.current_url
        assert 'Danielabdr' in current_url, f'Error: "Danielabdr" not in current url page'

    def log_out(self):
        self.driver.find_element(*self.MY_ACCOUNT_BUTTON).click()
        self.driver.find_element(*self.LOG_OUT_BUTTON).click()