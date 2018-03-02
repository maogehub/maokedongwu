def unique(func):
    u = {}
    def inner(*args, **kwargs):
        if args in u:
            return u[args]
        else:
            v = func(*args, **kwargs)
            u.setdefault(args, v)
            return v
    return inner

@unique
def add(x,y):
    print ("I am running:", x,y)
    return x+y

print add(1,1)
print add(1,1)
print add(2,2,)
print add(2,2,)
