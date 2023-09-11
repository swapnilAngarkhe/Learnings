people=[
    {"name": "Harry", "House":"Griffindoor" },
    {"name": "Cho", "House":"Ravenclaw" },
    {"name": "Draco", "House":"Slythrin" }
    
]

# def f(person):
#     return person["name"]


people.sort(key=lambda person: person["name"] )

print(people)