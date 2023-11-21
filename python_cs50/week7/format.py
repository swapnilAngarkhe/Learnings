import re

# here the user might type in the last name first then the first name 
#we can handel it with if and else ofc overwriting the name by spliting them into two and reformating
#but still there are plenty of edge cases here what if they do a space or a comma and space or a space without comma etc
#but there must be a better way?


name=input('what is your name? ').strip()

matches= re.search("^(.+), (.+)$", name,re.IGNORECASE )
# the parentheses above in pattern will capture the group 
# below after if matches we see matches.groups() which will get you the captured groups above.
if matches:
    last=matches.group(1)
    first=matches.group(2)
    name=f"{first} {last}"

print(f'hello {name}')

