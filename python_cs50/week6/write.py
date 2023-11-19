import csv

name=input('whats your name?: ')
home=input('where is your house: ')

with open("students2.csv", 'a') as file:
    writer=csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
    
