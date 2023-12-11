# nesting of dictionary

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# nesting a list in dictioary

travel_log = {
    "France": ["Paris", "Lillie", "Djon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# nesting a dictionary in a dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lillie", "Djon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

print(travel_log["France"])

travel_log = [
    {"country": "France", "cities_visited": ["Paris", "Lillie", "Djon"], "total_visits": 12},
    {"country": "Germany", "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
]