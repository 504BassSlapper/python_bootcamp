from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()

# if sheet_data[0]["iataCode"] == "":
cities_name = [rw["city"] for rw in sheet_data]

cities_code = [flight_search.get_destination_code(code) for code in cities_name]
print(cities_code)
for row in sheet_data:
    row["iataCode"] = flight_search.get_destination_code(row["city"])
# print(f"sheet_data = \n {sheet_data}")
data_manager.destination_data = sheet_data
# data_manager.update_destination_codes()    
    