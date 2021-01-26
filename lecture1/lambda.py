people = [
    {"name": "Harry", "house": "arlington"},
    {"name": "Rachel", "House": "Fairfax"},
    {"name": "Ahmet", "house": "DC"}
]


people.sort(key=lambda person: person["name"])

print(people)