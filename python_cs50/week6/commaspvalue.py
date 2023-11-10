names=[]

with open('name.txt') as file:
    for line in file:
        names.append(line.strip())

for name in sorted(names):
    print(f'hello, {name}')