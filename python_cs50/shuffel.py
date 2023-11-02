import random 

#creating a shuffel list 

names=['Rawhen', 'swap', 'amanda', 'david']

random.shuffle(names)

for name in names :
    print(name)    
    
winner=random.choice(names)

print(f"{winner} is the lucky winner!")



        








