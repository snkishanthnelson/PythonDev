from time import sleep
from threading import *

class Hi(Thread):
    def run(self):
        for i in range(2):
            print("hi")
            sleep(5)

class Hello(Thread):
    def run(self):
        for i in range(1):
            print("hello")
            sleep(1)

t1 = Hi()
t2 = Hello()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()
print("exit")

