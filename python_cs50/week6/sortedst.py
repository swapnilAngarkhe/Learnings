import csv

students=[]

with open ('student.csv', 'r') as file:
    for line in file:
       name, house= line.rstrip().split(",")
       
       student={"name":name, "house":house }
       students.append(student) # appending the disctionary to the list
       

#show how to short a dictionary now?
# def get_name(student): 
#     return student["name"]
    ## the above is one approch surely but there is a funciton called "lambda" you may see the syntax below

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is famous in {student['house']} ") 
    #here (above) it is critical to use double quote and single quotes vise versa
