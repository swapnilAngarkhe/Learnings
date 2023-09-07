# class point():
#     def __init__( self,input1, input2):# here self indicate the function/object itself and the data in it ex rohan=22 and ramesh=33 we can call them by the class name point.
#         self.x= input1
#         self.y= input2
        
# p=point(8, 2)
# print(p.x) 
# print(p.y)

class Flight():
    def __init__(self, capacity):
     self.capacity=capacity
     self.passangers=[]
     
    def addpassanger(self, name):
        if not self.openseats():
            return False
        self.passangers.append(name)
        return True
        
    def openseats(self):
        return self.capacity - len(self.passangers)
                            
        
flight=Flight(3)

people=["Harry","Swap", "Hitesh","Ramesh"]
for person in people:
    sucess=flight.addpassanger(person)
    if sucess:
        print(f"added {person} to flight succesfully")
    else: print(f"No seats avlbl for {person}")