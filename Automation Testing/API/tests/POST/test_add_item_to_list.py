from requests_folder.POST.request_POST_add_item_to_list import add_item_to_list

class TestAddItemToList:
    def test_add_item_to_unexisting_list_id(self):
        response = add_item_to_list(5555555555555555555555, "movie", 823464)
        assert response.status_code == 404, f'Error, expected status code 404, actual status code {response.status_code}'
        assert response.json()["status_message"] == "Invalid id: The pre-requisite id is invalid or not found.", f'Error, expected message "Invalid id: The pre-requisite id is invalid or not found.", actual message {response.json()["status_message"]}'

    def test_add_item_to_list_with_invalid_movie_type(self):
        response = add_item_to_list(8298607, "nothing", 823464)
        assert response.status_code == 404, f'Error, expected status code 404, actual status code {response.status_code}'
        assert response.json()[
                   "results"][0]["error"] == "Media is required", f'Error, expected message "Media is required", actual message {response.json()["results"][0]["error"]}'

    def test_add_item_to_list_with_negative_media_id(self):
        response = add_item_to_list(8298607, "movie", -25345698)
        assert response.status_code == 404, f'Error, expected status code 404, actual status code {response.status_code}'
        assert response.json()[
                   "results"][0]["error"] == "Media is required", f'Error, expected message "Media is required", actual message {response.json()["results"][0]["error"]}'

    def test_add_item_to_list_with_int_movie_type_and_string_media_id(self):
        response = add_item_to_list(8298607, 23568, "media")
        assert response.status_code == 404, f'Error, expected status code 404, actual status code {response.status_code}'
        assert response.json()[
                   "results"][0]["error"] == "Media is required", f'Error, expected message "Media is required", actual message {response.json()["results"][0]["error"]}'