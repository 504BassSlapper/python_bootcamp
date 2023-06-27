import requests
from datetime import datetime

API_USERS_ENDPOINT = "https://pixe.la/v1/users"
USERNAME= "bipbip"
GRAPH_ID= "graph1"
API_GRAPH_ENDPOINT = f"{API_USERS_ENDPOINT}/{USERNAME}/graphs"
PIXEL_CREATION_END_POINT= f"{API_GRAPH_ENDPOINT}/{GRAPH_ID}"
API_KEY_PIXELA_TOKEN = "Token2023."
print(API_GRAPH_ENDPOINT)
user_params = {
    "token":API_KEY_PIXELA_TOKEN,
    "notMinor": "yes",
    "agreeTermsOfService": "yes",
    "username": USERNAME
}

graphs_params= {
    "id": "graph1",
    "name": "my graph",
    "unit": "commits",
    "type": "int",
    "color": "ajisai"
}

header = {
    "X-USER-TOKEN": API_KEY_PIXELA_TOKEN
}

pixel_data ={
    "date": "20230620",
    "quantity": "9"
}

today = datetime.now()
pixel_today_data ={
    "date": today.strftime("%Y%m%d"),
    "quantity": "3"
} 
# response = requests.post(url=API_USERS_ENDPOINT, json=user_params)
# print(response.json())

# response = requests.post(url=API_GRAPH_ENDPOINT, json=graphs_params, headers=header)
# print(response.json())
date_time_request = datetime(2023,6,1)

response = requests.post(url=PIXEL_CREATION_END_POINT, json=pixel_data, headers=header)
response2 = requests.post(url=PIXEL_CREATION_END_POINT, json=pixel_today_data, headers=header)
print(PIXEL_CREATION_END_POINT)
print(response.json())