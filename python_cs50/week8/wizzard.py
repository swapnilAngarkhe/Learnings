#here we will see how to use properties of existing classes in other classses so that you dont have re write the code
# to do so you can put the primary calss into the secondery calss like "def seconderyclass(primaryclass)"
# after defining the initialising of 2ndry class you have to deff- "super(),__init__(parameter to use)"
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("missing name")
        self.name=name  
    

class student(Wizard):
    def __init__(self, name, house) :
        super().__init__(name)
        self.house=house
        
        

class prof(Wizard):
    def __init__(self,name,subject) :
        super().__init__(name)
        self.subject=subject
        
        
        