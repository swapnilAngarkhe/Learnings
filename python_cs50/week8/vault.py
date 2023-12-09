class Vault:
    def __init__(self,galleons=0, sickles=0, knuts=0):
        self.galleons=galleons
        self.sickles=sickles
        self.knuts=knuts
        
    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
    
    def __add__(self,other):
        Galleons= self.galleons + other.galleons
        Sickles=self.sickles + other.sickles
        Knuts=self.knuts + other.knuts
        return Vault(Galleons, Sickles, Knuts)
        
        
potter=Vault(100,20,5)
print(potter)
weasly=Vault(5,25,100)
print(weasly)
# to add the above
#object.__add__(self,other) IN THE CALSS IT SELF
#yes you can name the other anything u want
total=potter+weasly 