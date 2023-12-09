#to use hints and mypy we notate an hint while taking the value as parameter
#def meow(parameter: int) 
#so bsically mypy and type hints are used to avoid typeerrors:

#def meow(n: int) -> None: The arrow and none describe the return value of that prticular function

# def meow(n: int)-> None:
#     for _ in range(n):
#         print("meow")
        
# number: int=int(input("mewomber: "))
# meows: str=meow(number)
# meow(number)

#====================================================

"""Now fordoc we need to start usinig these quotation marks """
"""it is considered as formal documenting"""

"""
:param n: number of times of meow
:type n: int 
:raise TypeError: if n is not an int
:return: a string of meows, one per line
:typereturn: str

"""

def meow(n: int)-> str:
    return "meow \n" *n
    
        
number: int=int(input("mewomber: "))
meows: str=meow(number)
meow(number)