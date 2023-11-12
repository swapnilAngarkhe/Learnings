# for name csv
#not specifing 'r' as its default

# with open ('student.csv', 'r') as file:
#     for line in file:
#        row= line.rstrip().split(",")
#        print(f'{row[0]} is in {row[1]}')
    

# the effective way to write the above one is:

with open ('student.csv', 'r') as file:
    for line in file:
        #in the csv file in use, we have written few dishes and their city. So we can assign the value as follows:
       dish, city= line.rstrip().split(",")
       print(f'{dish} is in {city}')

