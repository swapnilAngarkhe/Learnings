#creating epty set
s=set()
#adding elements to the created set
s.add(0)
s.add(1)
s.add(2)
s.add(3)
s.add(3)#adding extra 3 will not affect the set at all it will print it once only.
s.remove(2)#as it says it will remove it, but what if i remove 3 cuz i put it twice?
s.remove(3)#as expected it will remove it completely, how about adding it again?
s.add(3) #ez it adds it again
print(s)

#"len" this is used to mesure the length. Remember to use "f" as formated list while printing.
print(f"the set has {len(s)} numbers of elements")
