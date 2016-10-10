cdef int fib(int n):
    cdef int a
    cdef int b
    a,b = 1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
fib(500000)
