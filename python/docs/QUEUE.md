# Queue

为什么要单独说 Queue 呢。因为发现很多人都不知道用这个东西。Queue是一个内建非常好用的东西。我一直管queue就叫做queue，为了写这个，专门去百度了一下，好吧，中文叫做“线性表”。

不管叫什么了，再多进程中，queue是最简单也是最容易的作为信息传递的方法。

python 中的queue出现在两个模组中。一个是Queue模组本身，另外一个是multiprocessing中。multiprocessing中的Queue跟本身的Queue使用起来是一样，唯一的区别是，内建的Queue适用于多线程，而multiprocessing中的Queue则适用于多进程

[normal.py](../src/queue/normal.py)

~~~python
import Queue
q=Queue.Queue()
q.put('message 1')
q.put('message 2')
q.put('message 3')
q.put('message 4')
q.put('message 5')
while not q.empty():
    print q.get()
~~~

一个简单的queue，丢入5个东西进去，然后通过 get() 拿出来。运行我们会看到拿到的信息。Queue.Queu()是FIFO queue。就是first in first out （先进先出）

~~~bash
message 1
message 2
message 3
message 4
message 5
~~~

[lifo.py](../src/queue/lifo.py)

~~~python
import Queue
q=Queue.LifoQueue()
q.put('message 1')
q.put('message 2')
q.put('message 3')
q.put('message 4')
q.put('message 5')
while not q.empty():
    print q.get()
~~~

这个就是一个LIFO的queue，last in first out （后进先出）
运行我们会看到，拿出来的顺序是跟进入的顺序相反的

~~~bash
message 5
message 4
message 3
message 2
message 1
~~~

[priority.py](../src/queue/priority.py)

~~~python
import Queue
q=Queue.PriorityQueue()
q.put((5, 'priority 5'))
q.put((3, 'priority 3'))
q.put((1, 'priority 1'))
q.put((2, 'priority 2'))
q.put((4, 'priority 4'))
while not q.empty():
    print q.get()
~~~

同时，还可以定义priority queue，也就是有优先级别的queue，你可以自定义优先级别。这个有优先级别，可以是任意可以做对比的对象，这里我们用tuple来做演示（你也可以写一个自己的priority的class来专门做这些）运行结果如下

~~~bash
(1, 'priority 1')
(2, 'priority 2')
(3, 'priority 3')
(4, 'priority 4')
(5, 'priority 5')
~~~

[other.py](../src/queue/others.py)

~~~python
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
~~~

上面的例子演示了使用queue.empty(), queue.full()以及blocking跟non-blocking的put与get

运行结果如下（注意在blocking跟non-blocking中时间的区别）

~~~bash
create queue max size: 10
try put 10 items
qsize: 10
queue empty: False
queue full: True

put one more item, timeout=1 [1476035766.74]
on exception Queue.Full [1476035767.75]

put one more item, non blocking [1476035767.75]
on exception Queue.Full [1476035767.75]

try get 10 items from queue
qsize: 0
queue empty: True
queue full: False

get one more, timeout=1 [1476035767.75]
on execption Queue.Empty [1476035768.75]

get one more, non blocking [1476035768.75]
on execption Queue.Empty [1476035768.75]

Done
~~~
