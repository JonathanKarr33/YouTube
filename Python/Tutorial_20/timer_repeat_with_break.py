import time
from playsound import playsound
minutes = int(input("How many minutes to set a time for: "))
number = int(input("How many times do you want to repeat the timer: "))
break_time = int(input("How many minutes to set a break for: "))
t = minutes *60
for i in range(number):
    while t:
        mins = t // 60
        sec = t % 60
        timer = "{:02d}:{:02d}".format(mins,sec)
        print(timer,end="\r")
        time.sleep(1)
        t -= 1
    print("Timer")
    playsound('Tutorial_20/alarm.mp3')
    time.sleep(break_time * 60)
    playsound('Tutorial_20/alarm.mp3')
    print("Your break is over")
    t = minutes * 60