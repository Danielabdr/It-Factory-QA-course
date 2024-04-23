from selenium.webdriver.common.by import By

from pages.base_page import Base_page


class LoggedinListPage(Base_page):
    LIST_LINK = (By.XPATH, '//a[@href="/u/Danielabdr/lists"]')
    CREATE_LIST_BUTTON = (By.LINK_TEXT, 'Create List')
    LIST_NAME_INPUT_FIELD = (By.XPATH, '//input[@id="name"]')
    CONTINUE_BUTTON = (By.XPATH, '//input[@id="step_1_submit"]')

    def click_list_link(self):
        self.driver.find_element(*self.LIST_LINK).click()

    def click_create_list_button(self):
        self.driver.find_element(*self.CREATE_LIST_BUTTON).click()

    def insert_list_name(self, name):
        self.enter_text(*self.LIST_NAME_INPUT_FIELD, name)

    def click_continue_button(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()