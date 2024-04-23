

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import Base_page


class Home_page(Base_page):
    SEARCH_INPUT_BOX = (By.ID, 'inner_search_v4')
    JOIN_TMDB_LINK = (By.XPATH, '/html/body/div[1]/header/div[1]/div/div[2]/ul/li[4]/a')
    ACCEPT_COOKIES_BUTTON = (By.ID, 'onetrust-accept-btn-handler')


    def navigate_to_home_page(self):
        self.driver.get('https://www.themoviedb.org/')

    def click_accept_cookies(self):
        accept_cookies = WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.ACCEPT_COOKIES_BUTTON))
        accept_cookies.click()


    def enter_search_value(self, search_value):
        self.enter_text(*self.SEARCH_INPUT_BOX, search_value)


    def enter_key_from_keyboard(self, key_entered):
        if key_entered.upper() == 'ENTER':
            self.enter_text(*self.SEARCH_INPUT_BOX, Keys.ENTER)

    def navigate_to_join_TMDB_link(self):
        self.driver.find_element(*self.JOIN_TMDB_LINK).click()



