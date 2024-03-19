class Employee:
    increment=1.5
    def __init__(self, fname, lname, salary):
        self.fname=fname
        self.lname=lname
        self.salary=salary
        
    
    def increase(self):
        self.salary=int(self.salary * self.increment)
    
    @classmethod
    def change_increment(cls,ammount):
        cls.increment=ammount
    
    @classmethod
    def from_str(cls, emp_string):
        fname,lname, salary = emp_string.split('-')
        return cls(fname,lname,salary)
    
    @staticmethod
    def isopen(day):
        if day== "sunday":
            return False
        else:
            return True
class Programer(Employee):
    def __init__(self, fname, lname, salary, proglang, exp):
        super().__init__(fname, lname, salary)
        self.proglang=proglang
        self.exp=exp



harry=Programer("harry","k", 50000, "python", "3 years")

        
Harry=Employee("Harry", "k", 43000)
rohan=Employee("rohan", "k", 74000)
lovish=Employee("lovish","L", 67000)
shumbham=Employee("shumbham","c", 88000)

print(harry.exp, harry.proglang)

# print(Employee.isopen("sunday"))

# print(lovish.salary)



#print(Harry.salary)
#Employee.change_increment(3)
#Harry.increase()
#print(Harry.salary)