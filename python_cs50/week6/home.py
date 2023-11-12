import csv

students=[]

with open ('home.csv') as file:
    reader=csv.DictReader(file) 
    for row in reader:
        students.append({"name": row["name"], "home": row["name"]})



for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from the {student['home']} ") 
    #here (above) it is critical to use double quote and single quotes vise versa
