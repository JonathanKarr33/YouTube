import time
from playsound import playsound
t = int(input("How many minutes to set a time for: ")) * 60
while t:
    mins = t // 60
    sec = t % 60
    timer = "{:02d}:{:02d}".format(mins,sec)
    print(timer,end="\r")
    time.sleep(1)
    t -= 1
print("Timer")
playsound('Tutorial_20/alarm.mp3')