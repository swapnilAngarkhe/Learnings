students= [
    {"name": "Hermione", "house":"Gryffindor"},
    {"name": "Harry", "house":"Gryffindor"},
    {"name": "Ron", "house":"Gryffindor"},
    {"name": "Draco", "house":"Slythrin"}
]

#here u have to filter out gryfindor students

#===========================
# gryffindors=[
#     student["name"] for student in students if student ["house"]=="Gryffindor"
# ]

# for gryffindor in sorted(gryffindors):
#     print(gryffindor)
#======================
#better approch? "filter" 
#variable = filter(function, dict (in which you have to apply the function))

def is_gryffindor(s):
    return s["house"]=="Gryffindor"

gryffindors = filter(is_gryffindor, students)

for gryffindor in gryffindors:
    print(gryffindor["name"])