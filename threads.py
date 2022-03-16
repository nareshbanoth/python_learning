from threading import Thread
from time import sleep


class Hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)


class Hi(Thread):
    def wait(self):
        for i in range(5):
            print("hi")
            sleep(1)


o1 = Hello()
o2 = Hi()
#o1.run()
#o2.run()
o1.start()
sleep(0.2)
o2.start()
o1.join()
o2.join()
print("Bye")