class Student:
    #lets start with dunder ie: __init__
    def __init__(self,name,house, patrones): # this helps  initalize contents of class object.
        if not name: 
            raise ValueError ('missing name')
        if house not in["Gryffindoor", "Slythrin", "Hufflepuff", "Ravenclaw"]:
            raise ValueError("House does not exist")
        self.name= name                             
        self.house= house
        self.patrones=patrones
    
    def __str__(self):
        return f'{self.name} from {self.house}'

        #__str__ will be called automatically by class when someone expects a string response from your program
        # above we saw two special functions that python call automatically now lets try creating our own
        #dont forget to put in self as a parameter because its a method inside a class 
    def charm(self):
        match self.patrones:
            case 'stag':
                return "🐴"
            case 'otter':
                return "🦦"
            case "jack russel terier":
                return "🐶"
            case _:
                return "🧹"
            

def main():
    student=get_student()
    print('expecto petronum')
    print(student.charm())
    print(f'{student.name} from {student.house}') 
    print(student)
    

def get_student():

 name=input('Name: ')
 house=input('House: ')
 patrones=input('patrones: ')
 return Student(name, house, patrones) 

        
    

if __name__=="__main__":
    main()
