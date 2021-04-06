#pip install gtts
from gtts import gTTS
import os

with open("example.txt","r") as document:
    myText = document.read()
    language = "en"
    output = gTTS(text=myText,lang=language,slow=False)
    output.save("output.mp3")
os.system("open output.mp3")