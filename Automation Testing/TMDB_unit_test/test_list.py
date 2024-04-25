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

    def setUp(self) -> None:
        self.driver = Driver()
        self.driver.get('https://www.themoviedb.org/')
        self.driver.maximize_window()
        self.driver.find_element(*self.ACCEPT_COOKIES_BUTTON).click()
        self.driver.find_element(*self.LOGIN_LINK).click()
        self.driver.find_element(*self.username_input).send_keys("Danielabdr")
        self.driver.find_element(*self.password_input).send_keys("TMDB1994@#@#")
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def tearDown(self) -> None:
        self.driver.quit()

    def test_check_creating_list_possible_with_name_containing_letters_numbers_and_special_characters(self):
        self.driver.find_element(*self.LIST_LINK).click()
        self.driver.find_element(*self.CREATE_LIST_BUTTON).click()
        self.driver.find_element(*self.LIST_NAME_INPUT_FIELD).send_keys("AutomatedList12@#45>%")
        self.driver.find_element(*self.CONTINUE_BUTTON).click()


