#!/usr/bin/python
import Queue
import time

print "create queue max size: 10"
q = Queue.Queue(10)
print "try put 10 items"
for x in range(10):
    q.put('x'*100)
print 'qsize:', q.qsize()
print 'queue empty:', q.empty()
print 'queue full:', q.full()
print ''
print "put one more item, timeout=1 [%s]" %time.time()
try:
    q.put('x', timeout=1)
except Queue.Full:
    print "on exception Queue.Full [%s]" %time.time()
print ''
print "put one more item, non blocking [%s]" %time.time()
try:
    q.put('x', False)
except Queue.Full:
    print "on exception Queue.Full [%s]" %time.time()
print ''
print "try get 10 items from queue"
for x in range(10):
    q.get()
print 'qsize:', q.qsize()
print 'queue empty:', q.empty()
print 'queue full:', q.full()
print ''
print "get one more, timeout=1 [%s]" %time.time()
try:
    q.get(timeout=1)
except Queue.Empty:
    print "on execption Queue.Empty [%s]" %time.time()
print ''
print "get one more, non blocking [%s]" %time.time()
try:
    q.get(False)
except Queue.Empty:
    print "on execption Queue.Empty [%s]" %time.time()
print ''
print 'Done'
