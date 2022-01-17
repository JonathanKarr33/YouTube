#pip install gtts
from gtts import gTTS
import os

myText = "This reads this line"
language = "en"
output = gTTS(text=myText,lang=language,slow=False)
output.save("output.mp3")
os.system("open output.mp3")