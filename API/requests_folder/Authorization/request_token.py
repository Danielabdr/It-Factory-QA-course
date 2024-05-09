import requests
from selenium.webdriver.common.by import By
from browser import Browser

class GenerateToken(Browser):
    REQUEST_URL = "https://api.themoviedb.org"
    APPROVE_BUTTON = (By.CSS_SELECTOR, '#main > section > div > div > form > input.k-button.k-primary')
    LOGIN_BUTTON = (By.XPATH, '//a[@href="/login"]//h2')
    USERNAME_FIELD = (By.XPATH, '//*[@id="username"]')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="password"]')
    LOGIN = (By.XPATH, '//*[@id="login_button"]')
    ACCEPT_COOKIES_BUTTON = (By.XPATH, '//button[@id="onetrust-accept-btn-handler"]')

    def create_request_token(self):

        headers = {
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4YTY1NzE0MDc5OTk0MDQzMGI0OTM2NTUwYTk1MDY1MyIsInN1YiI6IjY1YWZlM2UzNjdiNjEzMDBhZmYwYWI4NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UPr29bMUKwY-sqhxdEnaLvcwVEtCLFqTyTMCQTHMTEA',
            'accept': 'application/json',
            'content-type': 'application/json'
        }
        raw_body = {
            "redirect_to": "https://www.themoviedb.org/"
        }

        response = requests.post(f'{self.REQUEST_URL}/4/auth/request_token', headers=headers, json=raw_body)
        return response

    def ask_permission(self, request_token):

        request_token_response = self.create_request_token()
        if request_token_response.status_code == 200:
            request_token = request_token_response.json().get('request_token')
            print("Request token:", request_token)
        else:
            print("Failed to obtain request token")

        self.driver.get(f'https://www.themoviedb.org/auth/access?request_token={request_token}')
        self.driver.find_element(*self.ACCEPT_COOKIES_BUTTON).click()
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        self.driver.find_element(*self.USERNAME_FIELD).send_keys('Danielabdr')
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys('Tmdb1994@#@#')
        self.driver.find_element(*self.LOGIN).click()
        self.driver.find_element(*self.APPROVE_BUTTON).click()

    def create_access_token(self, request_token):
        headers = {
            'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4YTY1NzE0MDc5OTk0MDQzMGI0OTM2NTUwYTk1MDY1MyIsInN1YiI6IjY1YWZlM2UzNjdiNjEzMDBhZmYwYWI4NyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.UPr29bMUKwY-sqhxdEnaLvcwVEtCLFqTyTMCQTHMTEA',
        }
        raw_body = {
            "request_token": request_token
        }

        response = requests.post(f'{self.REQUEST_URL}/4/auth/access_token', headers=headers, json=raw_body)
        return response


# Creeaza o instanta a clasei GenerateToken
token_generator = GenerateToken()

# Apelarea metodei create_request_token()
response_create_token = token_generator.create_request_token()

#Extrage tokenul de cerere din raspunsul json
request_token = response_create_token.json().get('request_token')

#Apelarea metodei ask_permission() cu tokenul de cerere
token_generator.ask_permission(request_token)

#Apelarea metodei create_access_token() cu tokenul de cerere
response_access_token = token_generator.create_access_token(request_token)

