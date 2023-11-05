import requests
import json
import sys

if len(sys.argv) !=2:
    sys.exit

# making http request to the server
response=requests.get(f"https://itunes.apple.com/search?entity=song&limi=1&term= {sys.argv[1]}")

o=response.json()

for result in o ['results']:
    print(result['trackName'])


# here we are using an example of i tunes of apple music app.
# request will make u able to make a request as you are a web browser
#pyppi.org/project/request