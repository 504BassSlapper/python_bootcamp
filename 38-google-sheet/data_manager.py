import requests
import os

SHEETY_ENDPOINT = os.getenv("SHEETY_ENDPOINT")






TEST_RESPONSE = {
    "prices": [
        {"city": "Paris", "iataCode": "PAR", "lowestPrice": 54, "id": 2},
        {"city": "Berlin", "iataCode": "BER", "lowestPrice": 42, "id": 3},
        {"city": "Tokyo", "iataCode": "TYO", "lowestPrice": 485, "id": 4},
        {"city": "Sydney", "iataCode": "SYD", "lowestPrice": 551, "id": 5},
        {"city": "Istanbul", "iataCode": "IST", "lowestPrice": 95, "id": 6},
        {"city": "Kuala Lumpur", "iataCode": "KUL", "lowestPrice": 414, "id": 7},
        {"city": "New York", "iataCode": "NYC", "lowestPrice": 240, "id": 8},
        {"city": "San Francisco", "iataCode": "SFO", "lowestPrice": 260, "id": 9},
        {"city": "Cape Town", "iataCode": "CPT", "lowestPrice": 378, "id": 10},
    ]
}


class DataManager:
    def __init__(self):
        self.destination_data = {}

    # def get_destination_data(self):
    #     response = requests.get(url=SHEETY_ENDPOINT)
    #     data = response.json()
    #     self.destination_data = data["prices"]
    #     return self.destination_data

    def get_destination_data(self):
        data = TEST_RESPONSE
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data
            )
            print(response.json())
