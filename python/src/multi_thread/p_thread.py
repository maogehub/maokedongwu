import thread
import time

def f(x):
    time.sleep(1)
    print "hello", x

for x in range(10):
    thread.start_new_thread(f, (x,))
time.sleep(2)
