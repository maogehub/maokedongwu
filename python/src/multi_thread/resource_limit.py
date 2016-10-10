#!/usr/bin/python
import threading
import time
import resource

def test():
    time.sleep(1)

threading.stack_size(32768)
resource.setrlimit(resource.RLIMIT_NPROC, (65535, 65535))
xxx=[]
for x in range(50000):
    xxx.append(threading.Thread(target=test))
    try:
        xxx[x].start()
    except Exception, error:
        print error
        xxx.pop()
        break
print 'there are %s threads running' %threading.activeCount()
for x in xxx: x.join()
