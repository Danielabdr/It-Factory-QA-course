from seleniumbase import Driver

class Browser():
    driver = Driver()
    driver.maximize_window()
    driver.implicitly_wait(5)


    def close_browser(self):
        self.driver.quit()