import requests
from requests_folder.Authorization.request_token import GenerateToken

def add_item_to_list(list_id, media_type, media_id):
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NWFmZTNlMzY3YjYxMzAwYWZmMGFiODciLCJuYmYiOjE3MDg0MzkwMDEsImF1ZCI6IjhhNjU3MTQwNzk5OTQwNDMwYjQ5MzY1NTBhOTUwNjUzIiwianRpIjoiNjc0MjUwNiIsInNjb3BlcyI6WyJhcGlfcmVhZCIsImFwaV93cml0ZSJdLCJ2ZXJzaW9uIjoxfQ.24I44CN46rLJglDrlajkH7q0EFHiaeQH6ut0ClcLDyA"
    }
    data = {
            "items": [
                {
                    "media_type": media_type,
                    "media_id": media_id
                }
            ]
    }
    return requests.post(f"{GenerateToken.REQUEST_URL}/4/list/{list_id}/items", headers=headers, json=data)
