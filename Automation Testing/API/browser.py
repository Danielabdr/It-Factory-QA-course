from selenium import webdriver



class Browser:
    driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(5)



    def close_browser(self):
        self.driver.quit()
