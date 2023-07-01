import os 
import requests


TEQUILLA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILLA_API_KEY = os.getenv("TEQUILLA_API_KEY")


class FlightSearch:
     
    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILLA_ENDPOINT}/locations/query"
        header = {
            "apikey": TEQUILLA_API_KEY
        }
        query = {
            "term": city_name,
            "location_type": "city"
        }
        response = requests.get(url=location_endpoint, headers=header, params=query)
        data = response.json()["locations"]
        code  = data[0]["code"]
        print(code)
        return code


