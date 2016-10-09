# Decorator 

python decorator 到底是什么呢？其实这个就是去“加工”一下现有的东西而已。似乎很多初学的人，对于python中的 **@** 都觉得不是很好理解。掉这个 @xxx 是做了什么事情。

[decorator.py](../src/decorator/decorator.py)

~~~python
def deco(func):
    def inner(*args, **kwargs):
        print ("before calling func")
        func(*args, **kwargs)
        print ("after calling func")
    return inner
~~~

这里定义个很简单的decorator，首先我们定义一个funciton叫做deco，deco这个funciton接受一个参数func

在这个funciton中，我们在定义一个叫做inner的funciton，inner的function吃所有的位置参数(\*args)跟名称参数(\**kwargs)。deco的返回值是inner这个function

在inner中，我们首先打印一行“before calling func”然后，直接叫func（也就是deco传递进来的）然后我们在打印一个"after calling func" 

现在来看调用部分

~~~python
@deco
def myfunc(a):
    print ("myfunc() called. a=%s" %a)

myfunc("hello")
~~~

调用的时候，我们写一个叫做myfunc的function，但是注意在这个funciton之前，我们有一行@deco就是说，使用我们写的deco的那个decorator。这个时候，其实当你运行myfunc（）的时候，你会被带入到deco中去运行，也就是首先有一个打印“before calling func”然后执行我们定义的myfunc，然后再打印一个“after calling func”

运行结果如下：

~~~bash
# python decorator.py 
before calling func
myfunc() called. a=hello
after calling func
~~~

如果写网页的，例如django，flask, bottle等等，可能已经看到很多的这样类似的例子了。

也许有人觉得那个print的例子，看不出来有什么用。那么下面这个就是一个可以“用”的例子了。（实际上这个就是我写的用来做REST-API、cache的decorator，我平时自己的代码就有用到这个decorator）

[cache.py](../src/decorator/cache.py)

~~~python
#!/usr/bin/python
import functools
import time

class Cache(object):
    """Decorator. Caches a function's return value each time it is called.
    if called later with same arguments, the cached value is returned
    default timeout=30 seconds
    """

    def __init__(self, timeout=30):
        self.timeout=timeout
        self.cache={}

    def __call__(self, func):
        @functools.wraps(func)
        def decorated(*args, **kwargs):
            if args in self.cache:
                if time.time()-self.cache[args]['time']<self.timeout:
                    return self.cache[args]['value']
            value = func(*args, **kwargs)
            self.cache[args]={'value': value, 'time': time.time()}
            return value
        return decorated

    def __repr__(self):
        """return function's docstring.
        """
        return self.func.__doc__

    def __get__(self, obj, objtype):
        """support instance methods.
        """
        return functools.partial(self.__call__, obj)
~~~

上面是个cache的例子，例如我写一个http的request的function去服务器那结果，可能我这个function会被重复叫到很多次。但是我知道服务器那边结果并没有变动那么快，我只需要每30秒更新一次答案就可以（default timeout=30）那么使用这个decorator，每次叫我的function的时候，就会自动记录下来上次返回的值，如果到了timeout，那么会重新去做请求，如果没有到达timeout，那么直接返回内存的值。

通过我们的unittest代码，可以看出如何使用这个 cache decorator

[test_cache.py](../src/decorator/test/test_cache.py)

~~~python
#!/usr/bin/python
import cache
import unittest
import time

class TestCache(unittest.TestCase):

    def test_cache(self):
        """test cache
        """
        @cache.Cache()
        def return_value():
            return time.time()
        value=return_value()
        self.assertEqual(value, return_value())

    def test_cache_passthrough(self):
        """test cache pass through
        """
        @cache.Cache()
        def return_value(value):
            return time.time()
        value=return_value(0)
        self.assertNotEqual(value, return_value(1))

    def test_cache_timeout(self):
        """test cache time out
        """
        @cache.Cache(timeout=1)
        def return_value(value):
            return time.time()
        value=return_value(0)
        time.sleep(2)
        self.assertNotEqual(value, return_value(0))
~~~

这里定义了三个testcase，第一个是test_cache，我们建立一个新的return_value的function，返回time.time()的值（这个次都是不同的）可以看到的是，我们定义value=return_value()，而第二次，我们是去对比value是否等于return_value(),这里是第二次叫return_value()了，因为值我们已经cache起来，所以返回的值跟第一次的是一样的

第二个testcase是测试paas through。也就是说，每次我们叫return_value()的时候是参数不同的，那么虽然叫的是同一个function，但是因为你参数不同，cache只有记录同参数，那么两次叫return_value()应该返回的值是不同的

第三个testcase是测试timeout=1，也就是说一秒钟后，这个cache会过期，再次叫return_value返回的值应该是跟第一次不同的。虽然两次叫function的时候给的参数是相同的，但是因为cache只有保持1秒钟**@cache.Cache(timeout=1)**

我们可以看到测试的结果，三个测试全部通过

~~~bash
# nosetests -v
test cache ... ok
test cache pass through ... ok
test cache time out ... ok

----------------------------------------------------------------------
Ran 3 tests in 2.012s

OK
~~~


