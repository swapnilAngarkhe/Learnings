students=[
    {"name": "Hermoine", "house": "gryffindoor"},
    {"name": "Harry", "house": "gryffindoor"},
    {"name": "Ron", "house": "gryffindoor"},
    {"name": "draco", "house": "Slythrin"},
    {"name": "Padma", "house": "Ravenclaw"},
]
# what are the unique houses in which they live 
#so keeping in mind that if we loop it through dict then the houses might repeat themselves 
#to approch this problem we can use "sets"
#but first lets see how its done without sets

#======================================================
# houses=[]

# for student in students:
#     if student["house"] not in [houses]:
#         houses.append(student["house"])


# for house in sorted(houses):
    # print(house)
#=====================================================

houses= set()

for student in students:
    houses.add(student["house"])
    
for house in sorted(houses):
    print(house)
    
