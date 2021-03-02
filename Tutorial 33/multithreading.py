from threading import *
import time
class hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello World")
            time.sleep(1)
class how_are_you(Thread):
    def run(self):
        for i in range (5):
            print("How are you doing?")
            time.sleep(1)
obj1 = hello()
obj2 = how_are_you()
obj1.start()
obj2.start()
obj1.join()
obj2.join()
print("Goodbye")