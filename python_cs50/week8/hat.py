import random

class Hat:
    houses=["Griffindoor", "Hufflepuff", "Ravenclaw", "Slythrin" ]
        
    @classmethod
    def sort(cls,name): # here we can use "cls" to access the stuff in the class.
        
        print(f"{name} is in", random.choice(cls.houses))
        
    
Hat.sort("Harry") 