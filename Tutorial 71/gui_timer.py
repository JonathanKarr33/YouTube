import threading
import time
import tkinter as tk
from playsound import playsound

class timer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x250")
        self.root.title("Timer")

        self.enter_time = tk.Entry(self.root, font = ("Helvetica", 30))
        self.enter_time.grid(row = 0, column = 0, columnspan = 2, padx=5, pady=5)

        self.start_button = tk.Button(self.root, font = ("Helvetica", 30), text = "Begin", command = self.start_thread)
        self.start_button.grid(row = 1, column = 0, columnspan = 2, padx=5, pady=5)
        self.pause_button = tk.Button(self.root, font = ("Helvetica", 30), text = "Pause", command = self.pause)
        self.pause_button.grid(row = 1, column = 1, columnspan = 2, padx=5, pady=5)
        self.stop_button = tk.Button(self.root, font = ("Helvetica", 30), text = "End", command = self.stop)
        self.stop_button.grid(row = 1, column = 2, columnspan = 2, padx=5, pady=5)

        self.time_label = tk.Label(self.root, font = ("Helvetica", 30), text = "Time: 00:00:00")
        self.time_label.grid(row = 2, column = 0, columnspan = 5, padx=5, pady=5)

        self.stop_loop = False
        self.seconds_remaining = 0
        self.root.mainloop()

    def start_thread(self):
        t = threading.Thread(target=self.start)
        t.start()

    def start(self):
        self.stop_loop = False
        hours, minutes, seconds = 0, 0, 0
        string_split = self.enter_time.get().split(":")
        if len(string_split) == 3:
            hours = int(string_split[0])
            minutes = int(string_split[1])
            seconds = int(string_split[2])
        elif len(string_split) == 2:
            minutes = int(string_split[0])
            seconds = int(string_split[1])
        elif len(string_split) == 1:
            seconds = int(string_split[0])
        else:
            print("Invalid input")
            return
        self.seconds_remaining = hours * 3600 + minutes * 60 + seconds
        self.countdown()

        if not self.stop_loop:
            playsound("alarm.mp3")
    
    def countdown(self):
        while self.seconds_remaining > 0 and not self.stop_loop:
            self.seconds_remaining -= 1
            minutes, seconds = divmod(self.seconds_remaining, 60)
            hours, minutes = divmod(minutes, 60)
            self.time_label.config(text= f"Time : {hours:02d}:{minutes:02d}:{seconds:02d}")
            self.root.update()
            time.sleep(1)
    
    def pause(self):
        if self.stop_loop == True:
            self.stop_loop = False
            self.countdown()
        else:
            self.stop_loop = True

    def stop(self):
        self.stop_loop = True
        self.time_label.config(text="Time: 00:00:00")
timer()