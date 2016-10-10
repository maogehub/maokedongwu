#!/usr/bin/python
import time
import threading

class F(threading.Thread):
    def __init__(self, x):
        self.x=x
        self.result=None
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(1)
        self.result="hello %s" %self.x

result=[]
for x in range(10):
    result.append(F(x))
    result[x].start()
for x in result:
    x.join()
    print x.result

