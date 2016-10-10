# PYPY

很简单的介绍一下 <http://pypy.org>

pypy是用JIT (Just-in-time)的编译器。所以根据代码而定，速度可以快很多。包括python的作者Guido van Rossum都说，pypy很快，你要是关心速度，用pypy吧。

基本来说，python的代码不需要更改，就可以直接用pypy跑

pypy内建有stackless的支持。可以跑micro-thread （python中有stackless跟greenlets模组，你也可以下载这个然后跑stack-less）

国外出名的dropbox，就是用python做的，用的就是pypy

这里给一个很简单的测试例子

[speed_test.py](../src/pypy/speed_test.py)

~~~python
import random
data=[random.randint(1,100) for x in range(1000000)]
data.sort()
~~~

很简单，做一个list，random一堆东西，然后sort（）排序

python 运行结果，耗时2.8秒

~~~bash
time python speed_test.py 

real	0m2.827s
user	0m2.613s
sys	0m0.085s
~~~

pypy 运行结果，耗时0.6秒

~~~bash
time pypy speed_test.py 

real	0m0.637s
user	0m0.225s
sys	0m0.071s
~~~
