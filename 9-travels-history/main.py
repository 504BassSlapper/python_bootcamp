travel_log = [
    {
        "country": "France",
        "visits": "12",
        "cities": ["Paris", "Lille", "Bordeaux", "Nice"],
    },
    {
        "country": "Belgium",
        "visits": "10",
        "cities": ["Brussel", "Charleroi", "Tournai", "Liege", "Anvers", "Brugge", "Ostend"]
    }
]

wish_list_travel = [
    {
        "country": "France",
        "priority": "1",
        "cities": ["Marseille", "Nice"],
    },
    {
        "country": "Danemark",
        "priority": "2",
        "cities": []
    }
]


def add_travel(country, city):
    new_country = True
    for travel in travel_log:
        if travel["country"] in country:
            new_country = False
            travel["visits"] = str(int(travel[1]) + 1)
            if city not in travel["cities"]:
                travel[2].add(city)

    if new_country:
        add_country(country, city)
    print(f"{travel_log}")


def add_country(country, city):
    country_dictionnary = {
        "country": country,
        "visits": "1",
        "cities": [city]
    }
    travel_log.append(country_dictionnary)


add_travel("Russia", "Moscou")
