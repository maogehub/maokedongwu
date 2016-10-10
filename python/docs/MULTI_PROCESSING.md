# Multi-Processing 多进程

之前讲述了 [多线程] (MULTI_THREAD.md)这里在简单的介绍一下多进程。因为 python 是有 GIL Lock 的。所以对于吃CPU资源的运算来说，多线程并没有任何帮助。多线程只能帮助吃IO资源的工作。这个时候，如果本身电脑是有1颗以上的CPU的情况下，那么就可以用多进程，让每个CPU都忙起来

[multi\_process_map.py](../src/multi_process/multi_process_map.py)

~~~python
#!/usr/bin/python
import multiprocessing
import time

def f(x):
    time.sleep(1)
    return x*x

if __name__=='__main__':
    p = multiprocessing.Pool(10)
    x = p.map(f, [x for x in range(10)])
    print (x)
~~~

这个是一个用map拿到结果的例子。我们每次都做了1秒钟的sleep，这样只是为了辨别最后所花费的时间，从而证明我们是在多个进程下跑的。（运行10个线程，总耗时在1秒多）

运行结果如下

~~~bash
# time python multi_process_map.py 
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

real	0m1.258s
user	0m0.058s
sys	0m0.089s
~~~


同样一个例子，我们再用async_apply来做

[multi\_process\_apply_async.py](../src/multi_process/multi_process_apply_async.py)

~~~python
#!/usr/bin/python
import multiprocessing
import time

def f(x):
    time.sleep(1)
    return x*x

if __name__=='__main__':
    result=[]
    p=multiprocessing.Pool(10)
    for i in range(10):
        result.append(p.apply_async(f,(i,)))
    p.close()
    p.join()
    print [x.get() for x in result]
~~~

运行结果

~~~bash
time python multi_process_apply_async.py 
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

real	0m1.254s
user	0m0.057s
sys	0m0.081s
~~~
