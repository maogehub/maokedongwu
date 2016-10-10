# multi-thread 多线程

常见的问题之一，这里以最简单的例子，从不同的角度介绍一下多线程

#####thread 属于 low level的thread模组，这里只是作为演示。如果写程序，建议用threading的模组（high level）而不是thread

[p_thread.py] (../src/multi_thread/p_thread.py)

~~~python
import thread
import time

def f(x):
    time.sleep(1)
    print "hello", x

for x in range(10):
    thread.start_new_thread(f, (x,))
time.sleep(2)
~~~

有一个funciton叫做f，function做1秒钟的sleep，然后打印 hello x。x是这个function的参数

跑10个线程去运行f（），最后sleep 2秒结束程序

运行结果

~~~bash
time python p_thread.py 
hellohellohellohello hellohello hello8   234
 

 5
 hello 7
hello9hello 1

6

 0

real	0m2.116s
user	0m0.020s
sys	0m0.026s
~~~

这里看到，程序是2.11秒运行完毕。不过屏幕显示的东西很乱。
这个是因为多现成中，每个现成都在试图用print指令（写入stdout）每个写入都是一个字符一个字符的写入，所以很多线程一起写，就会“不分前后”就变成这个样子了。

多线程之间，可以用mutex做lock上锁。下面的例子就是用了lock

[p\_thread_mutex.py] (../src/multi_thread/p_thread_mutex.py)

~~~python
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
~~~

这里看到，同样的代码，我么多了个lock，平却用context manager的**with** ， 在 **with lock** 下执行我们的print

运行结果

~~~bash
time python p_thread_mutex.py 
hello 9
hello 2
hello 3
hello 4
hello 5
hello 6
hello 7
hello 8
hello 1
hello 0

real	0m2.050s
user	0m0.019s
sys	0m0.016s
~~~

这次我们看到的结果就是“正常“的了，lock保证每次只有一个线程可以运行print指令，只有一个线程完成了print之后，另外的线程才能运行print指令

[p_threading.py](../src/multi_thread/p_threading.py)

~~~python
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
~~~

这里还是上面一样的function f，还是跑10个线程，不过这里用threading的模组，而不是thread。threading有了join()，所以我们不用自己sleep 2秒钟等待thread结束了。直接join（）threading就会自动等待所有的thread结束

运行结果

~~~bash
time python p_threading.py 
hellohellohello hellohello  hello  hello1 0
 hello 43

6
hello 5

8
2
7
hello 9

real	0m1.140s
user	0m0.024s
sys	0m0.032s
~~~

我们看到，这里跟之前第一个例子一样，打印出来的东西是混乱的。用mutex做lock就可以解决这个问题。不过，我们这这次用[Queue](QUEUE.md)来做。Queue可以说是专门拿来做thread的利器

[p\_threading_queue.py](../src/multi_thread/p_threading_queue.py)

~~~python
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
~~~

运行结果

~~~bash
time python p_threading_queue.py 
hello 3
hello 7
hello 9
hello 1
hello 2
hello 0
hello 4
hello 6
hello 8
hello 5

real	0m1.141s
user	0m0.025s
sys	0m0.032s
~~~

用threading的话，可以直接继承Thread的class。我们只要继承threading.Thread，并且定义run（）这个method就可以了。当执行你的thread的start（）的时候，就是执行run（）这个method

[p\_threading_class.py](../src/multi_thread/p_threading_class.py)

~~~python
#!/usr/bin/python
import time
import threading

class F(threading.Thread):
    def __init__(self, x):
        self.x=x
        threading.Thread.__init__(self)

    def run(self):
        time.sleep(1)
        print "hello", self.x

result=[]
for x in range(10):
    result.append(F(x))
    result[x].start()
for x in result: x.join()
~~~

运行结果

~~~bash
time python p_threading_class.py 
hellohellohellohello hello hello hello8hello  0
9 2

 37
 

hello 4
5hello
  6
1

real	0m1.131s
user	0m0.025s
sys	0m0.031s
~~~

当然了，我们看到的屏幕还是乱的，这次再换一个方法，我们既不用mutex，也不用Queue。这次我们直接用class中的property。然后等线程运行完毕后，再去找property的值就好

[p\_threading\_class_property.py](../src/multi_thread/p_threading_class_property.py)

~~~python
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
~~~

上面看到，我们把结果保存在self.result当中。然后等线程运行完毕后，我们直接打印每个线程中的 result 

运行结果如下：

~~~bash
time python p_threading_class_property.py 
hello 0
hello 1
hello 2
hello 3
hello 4
hello 5
hello 6
hello 7
hello 8
hello 9

real	0m1.146s
user	0m0.026s
sys	0m0.034s
~~~

每个thread，都是需要消耗一定的内存的。这个也就是thread的stack size。关于stack size的大小，是根据不同的系统而决定的。python最小需要 32,768 (32 KiB) 如果你需要跑很多线程（几千甚至更多）而你的机器没有很多的内存，那么你会发现很快你就out of memeory了。

python的stack是可以调整的

[stack_size.py](../src/multi_thread/stack_size.py)

~~~python
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
~~~

**threading.stack_size()**这里就定义了我们每个线程开启，到底给多少内存

除了stack size，系统还会有另外一个限制，就是你最多可以开多少个文件，多少个进程。也就是linux中你ulimit -a看到的东西。这个，也是可以在你写代码的时候设定。

[resource_limit.py](../src/multi_thread/resource_limit.py)

~~~python
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
~~~

resource的设定是在**resource**这个模组中。通过设定**RLIMIT_NPROC** (resource limit, number of process)可以调整你可以使用的线程数量。（如果是linux，运行这个脚本会需要root权限）

