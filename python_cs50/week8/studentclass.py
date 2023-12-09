# taking exp from hat.py here we can put the main function into the class tself
#its a good design and will be helpufl in long run.
#also the get student because it make sense to put everything related to students into a class named after it.

class Student:
    def __init__(self,name,house,): 
        self.name= name                             
        self.house= house
    
    def __str__(self):
        return f'{self.name} from {self.house}'
    
    @classmethod #this method edit. again note that class methods can be called w/o initailising the class.
    def get(cls):
        house=input('house: ')
        name=input('name: ')
        return cls(name,house)
    

def main():
    student=Student.get() #here edit
    print(student)
    print(f'{student.name} from {student.house}')
    
        

if __name__=="__main__":
    main()
