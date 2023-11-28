class Student:
    #lets start with dunder ie: __init__
    def __init__(self,name,house,): # this helps  initalize contents of class object.
        # if not name:
        #     raise ValueError("Missing name")
        #  if house not in ["Gryffindoor", "Slythrin", "Hufflepuff", "Ravenclaw"]:
        #     raise ValueError("House does not exist")
        self.name= name                             
        self.house= house
    
    def __str__(self):
        return f'{self.name} from {self.house}'
    #================================
        #G E T T E R
    #so here for decorator we use @property and for setter we use @self.setter
    #to avoid confusion between the upper self.something with lowe, we put an underscore before
    #like this self._something and also in the return value
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name=name
        
    
    
    @property
    def house(self):
        return self._house
    
        #S E T T E R 
        #here you can set the conditions and properties.
    @house.setter
    def house(self,house):
        if house not in ["Gryffindoor", "Slythrin", "Hufflepuff", "Ravenclaw"]:
            raise ValueError("House does not exist")
        self._house=house 
        
    #==========================
    #so because of getter and setter we no longer need that before used conditions up above so yet!

def main():
    student=get_student()
    print(student)
    print(f'{student.name} from {student.house}')
    
    #now the thing is you can overwrite stuff of class using the dot notation for example:
    #   if you type this in main self.house=vadapav wale ke peeche then it will overwrite  the value 
    #for the above problem there is "properties" and with @ ie: decorators 
    #we can do it with getters and setters
    
    

def get_student():

 name=input('Name: ')
 house=input('House: ')
 return Student(name, house,) 

        
    

if __name__=="__main__":
    main()
