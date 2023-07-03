import os
import requests


TEQUILLA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILLA_API_KEY = os.getenv("TEQUILLA_API_KEY")
HEADER = {"apikey": TEQUILLA_API_KEY}


class FlightSearch:
    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILLA_ENDPOINT}/locations/query"

        query = {"term": city_name, "location_type": "city"}
        response = requests.get(url=location_endpoint, headers=HEADER, params=query)
        data = response.json()["locations"]
        code = data[0]["code"]
        print(code)
        return code

    def get_flights_by_date_and_destination(self, fly_from, fly_to, date_from, date_to):
        search_flights_endpoint = f"{TEQUILLA_ENDPOINT}/v2/search"
        params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": date_from,
            "date_to": date_to,
            # "nights_in_dst_to" : 15,
            # "nights_in_dst_from" : 2,
            # "one_for_city": 1,
            "sort" : "price",
            "max_stopovers": 1,
            "limit" : 1
        }
        resposne = requests.get(
            url=search_flights_endpoint,
            headers=HEADER,
            params=params
        )
        
        return resposne.json()
