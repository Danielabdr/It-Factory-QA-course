import time

import softest
from selenium.webdriver.common.by import By
from seleniumbase import Driver


class TestList(softest.TestCase):
    ACCEPT_COOKIES_BUTTON = (By.CSS_SELECTOR, 'button[id = "onetrust-accept-btn-handler"]')
    LOGIN_LINK = (By.XPATH, '/html/body/div[1]/header/div[1]/div/div[2]/ul/li[3]/a')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login_button"]')
    username_input = (By.XPATH, '//*[@id="username"]')
    password_input = (By.XPATH, '//*[@id="password"]')
    LIST_LINK = (By.XPATH, '//a[@href="/u/Danielabdr/lists"]')
    CREATE_LIST_BUTTON = (By.LINK_TEXT, 'Create List')
    LIST_NAME_INPUT_FIELD = (By.XPATH, '//input[@id="name"]')
    CONTINUE_BUTTON = (By.XPATH, '//input[@id="step_1_submit"]')
    EDIT_BUTTON = (By.XPATH, '//a[@class="font-semibold"]')
    LIST_OF_LIST = (By.XPATH, '//div[@class="list_cards"]/div')
    DELETE_LIST_BUTTON = (By.LINK_TEXT, 'Delete List')
    DELETE_BUTTON = (By.XPATH, '//button[@id="delete_list"]')
    YES_BUTTON = (By.XPATH, '//div[@role="toolbar"]/button[2]')
    LOG_OUT_BUTTON = (By.LINK_TEXT, 'Logout')
    MY_ACCOUNT_BUTTON = (By.XPATH, '//a[@title="Profile and Settings"]')


    def setUp(self) -> None:
        self.driver = Driver()
        self.driver.get('https://www.themoviedb.org/')
        self.driver.maximize_window()
        self.driver.find_element(*self.ACCEPT_COOKIES_BUTTON).click()
        self.driver.find_element(*self.LOGIN_LINK).click()
        self.driver.find_element(*self.username_input).send_keys("Danielabdr")
        self.driver.find_element(*self.password_input).send_keys("Tmdb1994@#@#")
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(3)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_check_creating_list_possible_with_name_containing_letters_numbers_and_special_characters(self):
        self.driver.find_element(*self.LIST_LINK).click()
        self.driver.find_element(*self.CREATE_LIST_BUTTON).click()
        self.driver.find_element(*self.LIST_NAME_INPUT_FIELD).send_keys("AutomatedList12@#45>%")
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        self.driver.find_element(*self.MY_ACCOUNT_BUTTON).click()
        self.driver.find_element(*self.LOG_OUT_BUTTON).click()


    def test_check_user_is_able_to_delete_a_list(self, list_name="My first created Listtttt"):
        self.driver.find_element(*self.LIST_LINK).click()

        list_results = self.driver.find_elements(*self.LIST_OF_LIST)
        list_name_in_list = False
        for list_element in list_results:
            if list_name in list_element.text:
                list_name_in_list = True
                # click on the title element(found it by tag name)
                title_element = list_element.find_element(By.TAG_NAME, "h2")
                title_element.click()
                break
        assert list_name_in_list, f"Error: The '{list_name}' is not found"

        self.driver.find_element(*self.EDIT_BUTTON).click()
        self.driver.find_element(*self.DELETE_LIST_BUTTON).click()
        self.driver.find_element(*self.DELETE_BUTTON).click()
        self.driver.find_element(*self.YES_BUTTON).click()
        time.sleep(2)
        self.driver.find_element(*self.MY_ACCOUNT_BUTTON).click()
        time.sleep(2)
        self.driver.find_element(*self.LOG_OUT_BUTTON).click()




