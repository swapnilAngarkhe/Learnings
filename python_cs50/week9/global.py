balance=0 # the keyword global will make the variable global so that it can be altered.

def main():
    print("Balance: ", balance)
    deposit(100)
    withdraw(50)
    print("Current Balance: ", balance)

def deposit(n):
    global balance
    balance+=n
    
def withdraw(n):
    global balance
    balance-=n

if __name__=="__main__":
    main()
    
    
    #nOTE: that if you declare a local variable with the same name as a global variable then the loclal varible will 
    # work as it should and have no affect on the global variable
    
    #ALOSE ITS NOT RECOMENDED TO DO THAT
    