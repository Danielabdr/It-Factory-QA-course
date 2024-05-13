import requests
from requests_folder.Authorization.request_token import GenerateToken

def update_list(list_id, description="", name=""):
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI2NWFmZTNlMzY3YjYxMzAwYWZmMGFiODciLCJuYmYiOjE3MDg0MzkwMDEsImF1ZCI6IjhhNjU3MTQwNzk5OTQwNDMwYjQ5MzY1NTBhOTUwNjUzIiwianRpIjoiNjc0MjUwNiIsInNjb3BlcyI6WyJhcGlfcmVhZCIsImFwaV93cml0ZSJdLCJ2ZXJzaW9uIjoxfQ.24I44CN46rLJglDrlajkH7q0EFHiaeQH6ut0ClcLDyA"
    }
    data = {
            "description": description,
            "name": name,
            "public": True,
            "sort_by": "original_order.asc"
}
    return requests.put(f"{GenerateToken.REQUEST_URL}/4/list/{list_id}", headers=headers, json=data)
