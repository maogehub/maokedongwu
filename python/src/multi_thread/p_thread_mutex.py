import thread
import time

lock=thread.allocate_lock()
def f(x):
    time.sleep(1)
    with lock:
        print "hello", x

for x in range(10):
    thread.start_new_thread(f, (x,))
time.sleep(2)
