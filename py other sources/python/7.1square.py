
import functions
# from functions import square
#this will import the fucntion from functions* for some reason we canot put a intiger in name of the file which we are importing.
#this is also an specfic import from the file functions which is square 
# for i in range(10):
#         print(f"square of{i} is {square(i)}")



#the other way to import is import the whole file and call the fucntion using . operator 
for i in range(10):
        print(f"square of {i} is {functions.square(i)}")