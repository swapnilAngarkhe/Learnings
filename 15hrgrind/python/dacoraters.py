
# def announce(f):
#     def wrapper():
#         print("about to run the function...")
#         f()
#         print("done with the fucntion")
#         return wrapper
    
# @announce
# def hello():
#      print("hello world")

# hello()

def announce(f):
    def wrapper():
        print ("About to run the function...")
        f( )
        print ("Done with the function.")
    return wrapper
    
@announce
def hello():
    print ("Hello, world!")
    
 
hello()
