students=["Hermione", "Harry", "Ron"]

#====================================
#without dictcomprihension

# gryffindors=[]
# for student in students:
#     gryffindors.append({"name": student, "house":"Gryffindor"})
    
#==========================\
#with dict comprehension

# gryffindors=[{"name":student, "house": "Gryffindor"} for student in students]
# 

#=====================================
#more optimal

gryffindors={student: "Gryffindor" for student in students}

print(gryffindors)