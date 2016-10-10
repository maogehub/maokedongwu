# PYPY

很简单的介绍一下 <http://pypy.org>

pypy是用JIT (Just-in-time)的编译器。所以根据代码而定，速度可以快很多。包括python的作者Guido van Rossum都说，pypy很快，你要是关心速度，用pypy吧。

基本来说，python的代码不需要更改，就可以直接用pypy跑

pypy内建有stackless的支持。可以跑micro-thread （python中有stackless跟greenlets模组，你也可以下载这个然后跑stack-less）

国外出名的dropbox，就是用python做的，用的就是pypy

这里给一个很简单的测试例子，用斐波那契数列

[speed_test.py](../src/pypy/speed_test.py)

~~~python
def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
fib(500000)
~~~

python 运行结果，耗时5.5秒

~~~bash
time python speed_test.py

real	0m5.558s
user	0m5.051s
sys	0m0.082s
~~~

pypy 运行结果，耗时3.3秒

~~~bash
time pypy speed_test.py

real	0m3.336s
user	0m2.768s
sys	0m0.132s
~~~
