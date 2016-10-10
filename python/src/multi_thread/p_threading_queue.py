#!/usr/bin/python
import time
import threading
import Queue

q=Queue.Queue()

def f(x):
    time.sleep(1)
    q.put("hello %s" %x)

result=[]
for x in range(10):
    result.append(threading.Thread(target=f, args=(x,)))
    result[x].start()
for x in result: x.join()
while not q.empty(): print q.get()
