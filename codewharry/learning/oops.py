class employee:
    def __init__(self, name, pagar, age):
        self.name=name
        self.pagar=pagar
        self.age=age
        
    def getpagar(self):
        return self.pagar
rohan=employee ("harry", "20000", 35)
print(rohan.pagar)
print(rohan.name)
print(rohan.age)

Samosa=employee ("Samosa", "10rs", "fresh")
print(rohan.pagar)
print(rohan.name)
print(rohan.age)
        
        