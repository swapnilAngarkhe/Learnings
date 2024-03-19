class flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.psg=[]
        
    def add_psg(self, name):
        if not self.open_seats():
            return False
        self.psg.append(name)   # here you store the passangers name in the self .psg list
        return True
    
    def open_seats(self):
        return self.capacity - len(self.psg)

flight=flight(3)      

people=["swapnil", "Nikhil", "Aaditya","bakliwal"]  
for person in people:
    success=flight.add_psg(person)
    if success:
        print(f"Added {person} to the flight successfully")
    else: print(f"no seats avlbl for {person}")
    