

def get_the_better_price_flight(flights_list):
    global best_flight
    if len(flights_list) >0:
        best_price = flights_list[0]["price"]
        best_flight = flights_list[0]
        for element in flights_list: 
            if(best_price > element["price"]):
                best_price = element["price"]
                best_flight = element
    return best_flight
        