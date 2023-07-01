import os 

TEQUILLA_ENDPOINT = "https://api.tequila.kiwi.com"
TEQUILLA_API_KEY = os.getenv("TEQUILLA_API_KEY")
class FlightSearch:
     
    def get_destination_code(self, city_name):
        code = "test"
        return code