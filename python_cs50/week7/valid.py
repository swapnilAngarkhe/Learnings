import re

# email=input("what's your email? ").strip()
# username, domain=email.split('@')

# if username and "." in domain:
#     print('valid')
# else:
#     print('valid')
    
#to improve the above we have a library called "re" that is REGULAR EXPRESSION
#function to learn is re.serach(pattern, string, flag)

# . any char except a newline
# * 0 or more repetitions
# + 1 or more repetations
# ? 0 or 1 repetition
# {m} repetition
#{m-n} repetation

email=input("what's your email? ").strip()
# below using the . before @ will apply any char except a newline and more included as did

if re.search('.+@.+', email):
    print('valid')
else:
    print('invalid')

