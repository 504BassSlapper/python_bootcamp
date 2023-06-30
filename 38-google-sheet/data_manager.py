import requests

SHEETY_ENDPOINT = "https://api.sheety.co/c593e0b12df26813bf44c40845673f7c/travelPrices/prices"

class DataManager: 
    def __init__(self):
        self.destination_data = {}
        
    def get_destination_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

        