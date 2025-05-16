travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new_country(country, number_of_visit, cities):
    new_country = {"country": country, "visits": number_of_visit, "cities": cities}
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint petersburg"])
print(travel_log)
