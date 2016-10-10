#!/usr/bin/python
import time
import threading

def f(x):
    time.sleep(1)
    print "hello", x

result=[]
for x in range(10):
    result.append(threading.Thread(target=f, args=(x,)))
    result[x].start()
for x in result: x.join()
