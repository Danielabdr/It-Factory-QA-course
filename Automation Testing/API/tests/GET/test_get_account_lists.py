
from requests_folder.GET.request_GET_list import get_list_by_id
class TestGetList:
    def test_get_list_by_valid_id(self):
        response = get_list_by_id(8290580)
        assert response.status_code == 200, f'Error, expected status code 200, actual status code: {response.status_code}'

    def test_get_list_by_invalid_id_float(self):
        response = get_list_by_id(8290580.689)
        assert response.status_code == 404, f'Error, expected status code 404, actual status code {response.status_code}'
        assert response.json()["status_message"] == "Invalid id: The pre-requisite id is invalid or not found.", f'Error, expected message "Invalid id: The pre-requisite id is invalid or not found.", actual message: {response["status_message"]}'

    def test_get_list_by_invalid_id_zero(self):
        response = get_list_by_id(0)
        assert response.status_code == 404, f'Error, expected status code 404, actual status code {response.status_code}'
        assert response.json()["status_message"] == "Invalid id: The pre-requisite id is invalid or not found.", f'Error, expected message "Invalid id: The pre-requisite id is invalid or not found.", actual message: {response["status_message"]}'

    def test_get_list_by_invalid_id_negative(self):
        response = get_list_by_id(-123645)
        assert response.status_code == 404, f'Error, expected status code 404, actual status code {response.status_code}'
        assert response.json()["status_message"] == "Invalid id: The pre-requisite id is invalid or not found.", f'Error, expected message "Invalid id: The pre-requisite id is invalid or not found.", actual message: {response["status_message"]}'

    def test_get_list_by_invalid_id_string(self):
        response = get_list_by_id("list")
        assert response.status_code == 404, f'Error, expected status code 404, actual status code {response.status_code}'
        assert response.json()["status_message"] == "Invalid id: The pre-requisite id is invalid or not found.", f'Error, expected message "Invalid id: The pre-requisite id is invalid or not found.", actual message: {response["status_message"]}'



