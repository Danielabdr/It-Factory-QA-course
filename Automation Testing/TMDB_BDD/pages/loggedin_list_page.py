import time


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Base_page



class LoggedinListPage(Base_page):
    LIST_LINK = (By.XPATH, '//a[@href="/u/Danielabdr/lists"]')
    CREATE_LIST_BUTTON = (By.LINK_TEXT, 'Create List')
    LIST_NAME_INPUT_FIELD = (By.XPATH, '//input[@id="name"]')
    CONTINUE_BUTTON = (By.XPATH, '//input[@id="step_1_submit"]')
    LIST_NAME_LINK = (By.XPATH, '//*[@id="main"]/div[4]/div/div/div/div[2]/div[1]/div[1]/div[2]/h2/a')
    EDIT_BUTTON = (By.XPATH, '//a[@class="font-semibold"]')
    ADD_ITEMS_BUTTON = (By.LINK_TEXT, 'Add/Edit Items')
    ADD_ITEM_FIELD = (By.XPATH, '//input[@id="list_item_search"]')
    FIRST_MOVIE_FROM_DROPDOWN = (By.CSS_SELECTOR, '#list_item_search_listbox > li:nth-child(1) > div > div > div > div.content > p.name')
    SAVE_BUTTON = (By.XPATH, '//input[@class="k-button k-primary submit_comment"]')
    DELETE_LIST_BUTTON = (By.LINK_TEXT, 'Delete List')
    DELETE_BUTTON = (By.XPATH, '//button[@id="delete_list"]')
    YES_BUTTON = (By.XPATH, '//div[@role="toolbar"]/button[2]')
    LIST_OF_LIST = (By.XPATH, '//div[@class="list_cards"]/div')

    def click_list_link(self):
        self.driver.find_element(*self.LIST_LINK).click()

    def click_create_list_button(self):
        self.driver.find_element(*self.CREATE_LIST_BUTTON).click()

    def insert_list_name(self, name):
        self.enter_text(*self.LIST_NAME_INPUT_FIELD, name)

    def click_continue_button(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def click_list(self):
        self.driver.find_element(*self.LIST_NAME_LINK).click()

    # def click_on_a_list(self, list_name):
    #     list_results = self.driver.find_elements(*self.LIST_OF_LIST)
    #     list_name_in_list = False
    #     for list_element in list_results:
    #         if list_name in list_element.text:
    #             list_name_in_list = True
    #             list_element.click()
    #
    #             break
    #     assert list_name_in_list, f"Error: The '{list_name}' is not found"

    def click_on_a_list(self, list_name):
        list_results = self.driver.find_elements(*self.LIST_OF_LIST)
        list_name_in_list = False
        for list_element in list_results:
            if list_name in list_element.text:
                list_name_in_list = True
                #click on the title element(found it by tag name)
                title_element = list_element.find_element(By.TAG_NAME, "h2")
                title_element.click()
                break
        assert list_name_in_list, f"Error: The '{list_name}' is not found"

    def click_edit_button(self):

        edit_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.EDIT_BUTTON))
        edit_button.click()
        # self.driver.find_element(*self.EDIT_BUTTON).click()

    def click_add_items_button(self):
        self.driver.find_element(*self.ADD_ITEMS_BUTTON).click()

    def add_movie_name_into_add_items_field(self, movie_name):
        self.enter_text(*self.ADD_ITEM_FIELD, movie_name)

    def click_first_movie_from_the_dropdown(self):
        self.driver.find_element(*self.FIRST_MOVIE_FROM_DROPDOWN).click()

    def click_save_button(self):
        self.driver.find_element(*self.SAVE_BUTTON).click()

    def click_delete_list_button(self):
        self.driver.find_element(*self.DELETE_LIST_BUTTON).click()

    def click_delete_button(self):
        self.driver.find_element(*self.DELETE_BUTTON).click()

    def click_yes_button(self):
        self.driver.find_element(*self.YES_BUTTON).click()








