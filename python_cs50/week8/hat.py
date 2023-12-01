import random

class Hat:
    houses=["Griffindoor", "Hufflepuff", "Ravenclaw", "Slythrin" ]
        
    def sort(cls,name):
        
        print(f"{name} is in", random.choice(cls.houses))
        
    
hat = Hat()
hat.sort("Harry")