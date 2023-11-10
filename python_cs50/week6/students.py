# for name csv
#not specifing 'r' as its default

with open ('student.csv', 'r') as file:
    for line in file:
       row= line.rstrip().split(",")
       print(f'{row[0]} is in {row[1]}')
    

