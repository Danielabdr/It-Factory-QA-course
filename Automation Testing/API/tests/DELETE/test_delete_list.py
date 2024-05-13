from requests_folder.DELETE.request_DELETE_list import delete_list


class TestDeleteList:

    def test_delete_list(self):
        response = delete_list(8300285)
        assert response.status_code == 200, f'Error, expected status code 201, actual status code {response.status_code}'
        assert response.json()["status_message"] == "Success.", f'Error, expected message "Success.", actual message {response.status_code}"'