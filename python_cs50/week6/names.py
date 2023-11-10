# names=[]

# for _ in range(3):
#     names.append(input('whats your name?: '))
    
# for name in sorted(names):
#     print(f'Hello, {name}')

#--------------------

#you need to assign the open to a file name it in this case "file"
# open to open+create a file--- w to write --- r to read --- 
#syntax open('filename', 'permmision')
#syntax file.write(nameoffile)

# name = input('whats your name: ')
# file=open("name.txt", 'a')
# file.write(f'{name} \n')
# file.close()
#here we can only write one name and the write funciton will re-write the whole file again each tme we run the program 
#make the w as 'a' for append and you know the rest
#the close function not been presnt can create courpted files and other problems so ..
#----------------------------------

#so the better approch here is "with" it opens and closes automatically.

# name = input('whats your name: ')
# #syntax of "with"
# with open("name.txt", 'a') as file:
#     file.write(f'{name} \n')
    
# # NOW time to "read"
# with open ('name.txt', 'r') as file:
#     
    
# for line in lines:
#     print(f'hello, {line.strip()}')

#----------------
#elegante~

# with open("name.txt", 'r') as file:
    # for line in file:
    #     print(f"Hello {line.strip()}")
#but can we sort the above? no we cant.

# so here is another one

# names=[]

# with open('name.txt') as file:
#     for line in file:
#         names.append(line.strip())

# for name in sorted(names):
#     print(f'hello, {name}')

# ok prolly the last one ...
names=[]

with open('name.txt') as file:
    for line in sorted(file):
        names.append(line.strip())
        print(f'hello, {line.strip()}')


    
