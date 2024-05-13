from requests_folder.PUT.request_PUT_update_list import update_list


class TestUpdateList:

    def test_update_list_name(self):
        response = update_list(8298301, "", "Updated list")
        assert response.status_code == 201, f'Error, expected status code 201, actual status code {response.status_code}'
        assert response.json()["status_message"] == "The item/record was updated successfully.", f'Error, expected message "The item/record was updated successfully.", actual message {response.json()["status_message"]}'

    def test_update_description_field(self):
        response = update_list(8298301, "Updated list description", "Updated list")
        assert response.status_code == 201, f'Error, expected status code 201, actual status code {response.status_code}'
        assert response.json()[
                   "status_message"] == "The item/record was updated successfully.", f'Error, expected message "The item/record was updated successfully.", actual message {response.json()["status_message"]}'

    def test_update_the_details_of_an_invalid_list(self):
        response = update_list(-562619564984, "6655", "unexisting list")
        assert response.status_code == 404, f'Error, expected status code 404, actual status code {response.status_code}'
        assert response.json()[
                   "status_message"] == "Invalid id: The pre-requisite id is invalid or not found.", f'Invalid id: The pre-requisite id is invalid or not found.", actual message {response.json()["status_message"]}'


