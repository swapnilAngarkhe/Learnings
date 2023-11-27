class Student:
    #lets start with dunder ie: __init__
    def __init__(self,name,house): # this helps  initalize contents of class object.
        if not name: 
            raise ValueError ('missing name')
        if house not in["Gryffindoor", "Slythrin", "Hufflepuff", "Ravenclaw"]:
            raise ValueError("House does not exist")
        self.name= name                             
        self.house= house


def main():
    student=get_student()
    
    print(f'{student.name} from {student.house}')
    

def get_student():
    try:
        name=input('Name: ')
        house=input('House: ')
        return Student(name, house)
    except ValueError:
        ...
        
    

if __name__=="__main__":
    main()
