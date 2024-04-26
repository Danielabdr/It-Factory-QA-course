from selenium.webdriver.common.by import By

from browser import Browser


class Base_page(Browser):
    def enter_text(self, by, value, search_value):
        self.driver.find_element(by, value).send_keys(search_value)





