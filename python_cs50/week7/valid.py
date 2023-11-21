import re

# email=input("what's your email? ").strip()
# username, domain=email.split('@')

# if username and "." in domain:
#     print('valid')
# else:
#     print('valid')
    
#to improve the above we have a library called "re" that is REGULAR EXPRESSION
#function to learn is re.serach(pattern, string, flag)


       ###    Remember to put an r for the raw string         ###     
# . any char except a newline
# * 0 or more repetitions
# + 1 or more repetations
# ? 0 or 1 repetition
# {m} repetition
#{m-n} repetation
# ^ matches the start of string
# $ matches the end of the string just before the newline
# [] set of char
# [^] complementing the text
#[a-z1-0A-Z_] you dont have to use any seprateors or any space


# below using the . before @ will apply any char except a newline and more included as did
# note that puttint an r before a string make the string as "raw string"
#here also the . with the backslash is necessory because if not the intrepreture will take it litraly as the sign of any char

#so [^@] refered to @ sign like you cant have @ in the . ie any char symbol, basically [^ symbol] will set and exception
# but one better way is to use the range
#idk how many there are but this one is pretty short its \w which will take the ranges [a-z1-0A-Z_]
# and the third argument here is re.function (pattern, string, flag) which act like a flah (r'^\w+@\w+\.edu$', email, re.IGNORECASE)
# so with the above we might face problem when the domain have multipal dots in them ex: malan.haravard.cs50.edu this will throw invalid

# A|B a or b
#(...) a group
#  I KINDA HATE THIS ONE PARTICLAR LESSON what is going on!!???

#======================================================================

# email=input("what's your email? ").strip()
# if re.search(r'^\w+@(\w+\.)?\w+\.edu$', email, re.IGNORECASE):
#     print('valid')
# else:
#     print('invalid')
 
 #====================================================================

#THANK GOD THERE IS AN LIBRARY!!!

email=input("what's your email? ").strip()
if re.search(r'^\w+@(\w+\.)?\w+\.edu$', email, re.IGNORECASE):
    print('valid')
else:
    print('invalid')
    
# go to format .py