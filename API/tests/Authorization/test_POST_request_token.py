from requests_folder.Authorization.request_token import GenerateToken

class TestRequestToken:
    def test_token_request_has_correct_status_code(self):
        token_generator = GenerateToken()
        response = token_generator.create_request_token()
        assert response.status_code == 200, f'Error: Expected status code 200, actual status code {response.status_code}'

    def test_request_token_is_valid(self):
        token_generator = GenerateToken()
        response = token_generator.create_request_token().json()
        assert response["request_token"] != "", f'Error: Expected request token not null, actual response {response["request_token"]}'
