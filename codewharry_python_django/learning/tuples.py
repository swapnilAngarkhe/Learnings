t=(1,2,3,5,5) #tuples are not mutable ie. immutable 
print(t.count(5))
print(t.index(1))

#you cannot assign the value cuz tuple and strings are imutable. you can do it in list.
t[0]=2 #this will throw an error of tuple object does not support item assignment
