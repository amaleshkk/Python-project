country = input("Enter the name of the country you have visited: \n")
visits = int(input("Enter the number of visits: \n"))
list_of_cities = input("Enter the list of cities: \n")

travel_log = [
    {
        "country": "France",
        "visits" : 12,
        "cities": ["Paris", "Lillie", "Djon"]
    },
    {
        "country": "Germany",
        "visits" : 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]

def add_new_country(country, visits, cities_visited):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country(country, visits, list_of_cities)

print(travel_log)
print(f'{travel_log[2]["country"]} visits: {travel_log[2]["visits"]} places: {travel_log[2]["cities"]}')
