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
