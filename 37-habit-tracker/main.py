import requests

API_USERS_ENDPOINT = "https://pixe.la/v1/users"
API_KEY_PIXELA_TOKEN = "Token2023."

user_params = {
    "token":API_KEY_PIXELA_TOKEN,
    "notMinor": "yes",
    "agreeTermsOfService": "yes",
    "username": "bipbip"
}

response = requests.post(url=API_USERS_ENDPOINT, json=user_params)
print(response.json())