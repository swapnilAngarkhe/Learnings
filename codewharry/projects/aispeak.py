#since the tutorial was in mac I've to figured out how the say command work in windows in which i found about wincom.

import win32com.client as wincom
speak=wincom.Dispatch("SAPI.SpVoice")

while True:
    text=input("enter the text you want: ")
    if text=="q":
        speak.speak("aara aarah saayoo naaraa")
        break
        
    speak.speak(text)