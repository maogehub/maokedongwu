# Cython 又一个神器

cython算是python的一个变种，也是以速度为目标的变种。跟[pypy](PYPY.md)不同的是，cython如果想要追寻速度，需要用cython自己的语法。另外，因为需要速度，所以变量类型需要定义固定类型（跟c一样）function也是一样，定义返回的数据类型，以及参数的数据类型

这里还是用之前pypy那个斐波那契数列的测试。

[speed_test.py](../src/cython/speed_test.py)

~~~python
def fib(n):
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
fib(500000)
~~~

python 运行耗时:5.5秒

~~~bash
time python speed_test.py

real	0m5.558s
user	0m5.051s
sys	0m0.082s
~~~

这里看cython的例子，注意，cython的文件是pyx结尾，不是py
而且我们需要用cdef而不是def，funciton也要定义数据类型 （int），参数n也是要定义数据类型（int），function内的a跟b同样需要定义数据类型。

[speed_test.pyx](../src/cython/speed_test.pyx)

~~~python
cdef int fib(int n):
    cdef int a
    cdef int b
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
fib(500000)
~~~

cython 运行耗时：0.6秒

~~~bash
time cython speed_test.pyx 

real	0m0.679s
user	0m0.295s
sys	0m0.125s
~~~

## 直接编译出可执行文件

cython 可以直接把python的文件，转换成c文件，然后直接编译出2进制的可执行文件。当然了，你需要一个c语言的编译器才能把c文件编译成可执行文件

~~~bash
cython --embed speed_test.pyx -o speed_test.c
gcc -I /usr/include/python2.7 speed_test.c -lpython2.7 -o speed_test
~~~

这个时候，我们直接编译我们的cython代码到c，到二进制了。这里用file指令看到，编译出来的speed_test是直接苹果的可执行文件

~~~bash
file speed_test
speed_test: Mach-O 64-bit executable x86_64
~~~

速度还更快了

~~~bash
rli-MacAir:cython rli$ time ./speed_test

real	0m0.114s
user	0m0.016s
sys	0m0.063s
~~~

## 编译成动态库，直接使用

cython还可以把代码直接编译成动态库（就是linux中的.so文件，或者windows中的.dll文件）

当你运行cython的时候，就会产生一个c文件

~~~bash
cython speed_test.pyx
~~~

~~~bash
gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -lm -I/usr/include/python2.7/ -lpython2.7 -o speed_test.so speed_test.c
~~~

~~~bash
file speed_test.so 
speed_test.so: Mach-O 64-bit dynamically linked shared library x86_64
~~~