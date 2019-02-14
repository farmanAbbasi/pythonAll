from threading import *
from time import sleep
class A(Thread):
    
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)
            
class B(Thread):
    
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)
             
obj1=A()
obj2=B()
obj1.start()
sleep(0.1)
obj2.start()
#here bye will be printed in between by the main thread so to print the at the last 
#use join
obj1.join()
obj2.join()
print("bye")
