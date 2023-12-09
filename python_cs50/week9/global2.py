class Account:
    def __init__(self):
        self._balance=0
    
    @property
    def balance(self):
        return self._balance
    
    def deposit(self,n):
        self._balance+=n
        
    def withdraw(self,n):
        self._balance-=n

def main():
    account=Account()
    print("balance: ", account.balance )
    account.deposit(100)
    account.withdraw(10)
    print("Balance: ",account.balance)
    

if __name__=="__main__":
    main()
    
    
    #RULE OF THUMB is to use global variables as less as possible, or none if can do so.