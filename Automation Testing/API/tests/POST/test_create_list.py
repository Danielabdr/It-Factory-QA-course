from requests_folder.POST.request_POST_create_list import create_list


class TestCreateList:
    def test_create_list_with_string_description_and_name(self):
        response = create_list("hello", "API list")
        assert response.status_code == 201, f'Error, expected status code 201, actual status code {response.status_code}'
        assert response.json()["status_message"] == "Success.", f'Error, expected message "Success.", actual message {response.json()["status_message"]}'
