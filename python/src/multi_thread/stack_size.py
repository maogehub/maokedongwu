#/usr/bin/python
import threading
import time
threading.stack_size(32768)

def test():
    time.sleep(1)

threads=[]
for x in range(30000):
    try:
        threads.append(threading.Thread(target=test))
        threads[x].start()
    except Exception, error:
        print error
        threads.pop()
        break
print "there are %s threads running" %threading.active_count()
for x in threads:
    x.join()
