
students=["Hermione", "Hrry", "Ron"]

#========================
#without enumerate

# for i in range(len(students)):
#     print(i + 1, students[i])

#================================
#with enumerate

for i, student in enumerate(students):
    print(i+1, student)
    
    