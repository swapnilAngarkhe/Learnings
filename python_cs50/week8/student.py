
#============================================================================================
 # USING LIST AND TUPLE
# def main():
#     student=get_student()
#     if student[0] == 'Padma':
#         student[1]='RavenClaw'
#     # print(f'{name}, is from {house}') so instead of this the below...
#     print(f'{student[0]} is from {student[1]}')
    


# # def get_name():
# #     return input('what is your name: ')

# # def get_house():
# #     return input('what is your house: ')
# #========================================
# #but we can do this both in one function so ... how to return 2 values you ask?
# #use a dict ez whats more easy? return both lol return name1, name2 just liek that!
# #to get the values use name1, name2 = functioname() yes it is a tuple, reminder its not mutable
# #but what if we want to mute lol, use a list simple by pputting square bracets instead


# def get_student():
#     name=input('Name: ')
#     house=input('house: ')
    
#     return [name, house]
#===============================================================================================


def main():
    student=get_student()
    if student["name"]=="padma":
        student['house']='ravenclaw'
    print(f'{student["name"]} from {student["house"]}')
    
    

def get_student():
    student={"name": input('Name: ')}
    student["house"]=input('house: ')
    return student

if __name__=="__main__":
    main()
