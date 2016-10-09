def deco(func):
    def inner(*args, **kwargs):
        print ("before calling func")
        func(*args, **kwargs)
        print ("after calling func")
    return inner

@deco
def myfunc(a):
    print ("myfunc() called. a=%s" %a)

myfunc("hello")
