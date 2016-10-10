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
