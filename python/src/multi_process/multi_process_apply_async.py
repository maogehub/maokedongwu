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
