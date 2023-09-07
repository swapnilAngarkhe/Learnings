import requests
import json
import win32com.client as wincom
speak=wincom.Dispatch("SAPI.SpVoice")

city=input("enter the name of the city: ")
url=f'http://api.weatherapi.com/v1/current.json?key=8c3a9fe79821438b9e794127232806&q={city}'
r=requests.get(url)
print(r.text)
print(type(r.text))
weatherdic=json.loads(r.text)
print(weatherdic["current"]["temp_c"])

speak(f"speak'the current temprature in {city} is {weatherdic}'") # dubug this one


