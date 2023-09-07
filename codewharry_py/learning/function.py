def greethello(name, ending):
    print('hello ' + name)
    print('hello ' + name)
    print('hello ' + name)
    print(ending)
    
def lettergenrator(name, date, location, time ):
    st= f'''This is {name} writing to you to inqure about the event on {date}. \n
            I live at {location} it takes me around {time} to reach the destination'''
    print(st)
    
def avg(num1, num2):
    print(num1+num2)/2

greethello("swapnil", " how are your?")
greethello("shivam", "how are you?")
lettergenrator("vishal", "20th June 2023", "thane", "2hrs")
avg(10,5)