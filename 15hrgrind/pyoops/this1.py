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
        
    def __add__(self,other):
        return self.salary + other.salary
    
    def __repr__(self):
        return 'Employee({}, {}, {})'.format (self.fname,self.lname, self.salary)
    


harry=Employee("harry","k", 50000)
rohan=Employee("rohan","das", 9)


print(repr (harry))