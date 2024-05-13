from requests_folder.POST.request_POST_create_list import create_list


class TestCreateList:

    def test_create_list_with_special_characters_numbers_and_letters_in_name(self):
        response = create_list("", "API list*&@#123")
        assert response.status_code == 201, f'Error, expected status code 201, actual status code {response.status_code}'
        assert response.json()["status_message"] == "Success.", f'Error, expected message "Success.", actual message {response.json()["status_message"]}'
    def test_create_list_with_string_description_and_name(self):
        response = create_list("hello", "API list")
        assert response.status_code == 201, f'Error, expected status code 201, actual status code {response.status_code}'
        assert response.json()["status_message"] == "Success.", f'Error, expected message "Success.", actual message {response.json()["status_message"]}'

    def test_create_list_with_null_description_and_name(self):
        response = create_list("", "")
        assert response.status_code == 400, f'Error, expected status code 400, actual status code {response.status_code}'
        assert response.json()["status_message"] == "Validation failed.", f'Error, expected message "Validation failed.", actual message {response.json()["status_message"]}'
