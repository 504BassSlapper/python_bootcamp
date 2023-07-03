from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime , timedelta

from json_file_wirter import write_json, read_json

from utils import get_the_better_price_flight

data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_destination_data()

IATA_FROM= "CRL"

# if sheet_data[0]["iataCode"] == "":
#     cities_name = [rw["city"] for rw in sheet_data]

#     # cities_code = [flight_search.get_destination_code(code) for code in cities_name]
#     # print(cities_code)
#     for row in sheet_data:
#         row["iataCode"] = flight_search.get_destination_code(row["city"])
#     # print(f"sheet_data = \n {sheet_data}")
#     data_manager.destination_data = sheet_data
#     data_manager.update_destination_codes()    

tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
six_months_later = (datetime.now() + timedelta(days=(30*6))).strftime("%d/%m/%Y")
print(tomorrow)
print(six_months_later) 

# data = flight_search.get_flights_by_date_and_destination("PAR", "LON", tomorrow, six_months_later)
# print(len(data["data"]))
# write_json(data["data"])

# my_data = read_json()

# print(len(get_the_better_price_flight(my_data)))

# write_json(get_the_better_price_flight(my_data),"new.json")

# prices = [ x["price"] for x in my_data]
# days = [x["local_departure"] for x in my_data]
# print(days)

best_flights_destination = []
# loop on cities
for destination in  sheet_data:
    if destination["iataCode"] != "":
        available_flights = flight_search.get_flights_by_date_and_destination(IATA_FROM , destination["iataCode"],tomorrow, six_months_later)
        # write_json(available_flights, "test.json")
        print(available_flights)
        best_flight = get_the_better_price_flight(available_flights["data"])
        departure_date = best_flight["local_departure"]
        
        split_elements = departure_date.split("T")
        formated_departure_date = split_elements[0]
        best_flights_destination.append( 
                                        {"destination" : destination["city"],
                                         "price": best_flight["price"],
                                         "departure_date": formated_departure_date
                                         })
    

print(best_flights_destination)
write_json(best_flights_destination, "result.json")  

    