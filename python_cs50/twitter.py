import re
#goal is to get the username of the user from their twitter link

url=input('paste your twitter profile url: ').strip()

#==========================================
            # username=url.replace("https://twitter.com/", "")

            # print(f'hello {username}')
#===========================================

# ^ for starting string match 
# ? for the opptional s as page might load with http only
# (www\.) \. for for the litral dot itself and not confuse it with . ie:: any char:: 
# the www is written in parenth- because the whole string is optional and followed with ?
# the ? makes the whole www\. string optional
# then the user might mess up the protocol so we put the https:// part as optional putting them into paran and then a ?

        # username=re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
        # print(f'hello, {username}')

# here the issue raises that what if uer typed a whole diff url ex: www.google.com
#========================================

        # matches=re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
        # if matches:
        #     print(f'hello, {matches.group(2)}')
#==========================================

# lets recall the walrus operator :=

        # if matches :=re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
        #     print(f'hello, {matches.group(2)}')
    
# but but but recall the very last one? (?:...) non-captering version? YES
#below u can see the ?: used in www.\ which will not capture it even if its typed or not and making the gorup 1.
#not to ignore at last we changed the username thingy to ranges
matches=re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_])$", url, re.IGNORECASE)
if matches:
    print(f'hello, {matches.group(1)}')


