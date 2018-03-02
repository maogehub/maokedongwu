#!/usr/bin/python
import functools

class Cache(object):
    """Decorator. Caches a function's return value each time it is called.
    """

    def __init__(self):
        self.cache={}

    def __call__(self, func):
        @functools.wraps(func)
        def decorated(*args, **kwargs):
            if args in self.cache:
                    return self.cache[args]['value']
            value = func(*args, **kwargs)
            self.cache[args]={'value': value}
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

count=0
@Cache()
def add(x,y):
    global count
    count+=1
    return x+y

print add(1,2)
print add(1,2)
print add(1,2)
print add(1,2)
print "function add called: %s times" %count

count=0
def add2(x,y):
    global count
    count+=1
    return x+y

print add2(1,2)
print add2(1,2)
print add2(1,2)
print add2(1,2)
print "function add2 called: %s times" %count

class T(object):
    def __init__(self):
        self.count=0
    @Cache()
    def add(self, x, y):
        self.count+=1
        return x+y

test = T()
print test.add(1,2)
print test.add(1,2)
print test.add(1,2)
print test.add(1,2)
print "class T method add called: %s times" %test.count

