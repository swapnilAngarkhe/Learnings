#========================================
#without unpack
# first, last=input("whats your name? ").split(" ")
# print(f"hello, {first}")
#=====================================

#suppose the coins list below have 100's of values 
#ie u canot pass it and it goes on 
#we use the keyword * before the varaible 
#*coins
#this will unpack and pass individual values from the list

# def total(galleons, sickles, knuts):
#     return(galleons *17 + sickles) *29+ knuts

# coins=[100,50,25]

# print(total(*coins), "knuts")

#=====================================
# will it work for dict?

# def total(galleons, sickles, knuts):
#     return(galleons *17 + sickles) *29+ knuts

# coins={"galleons":100, "sickles":50, "knuts":25}


# # print(total(*coins), "knuts")
# """"and the below is the result of using single * lol"""
# # galleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonsgalleonssicklesknuts knuts
# """here is the double * for dict"""
# print(total(**coins), "knuts")
#==================

"""
   the * are also used as a visual indicator 
   also work with *args, **kwargs lets see it below
    
"""
#===============================
def f(*args,**kwargs):
    print("positionals: ",args)
    print("positionals: ",kwargs)
    
f(100,50,25,)
f(galleons=100, sickles=50, knuts=25)
"""reminder to use *args for number/list and **kwargs for dicts"""