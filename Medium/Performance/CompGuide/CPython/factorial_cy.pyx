def factorial(long n):
    cdef long result = 1
    cdef long i
    for i in range(2, n+1):
        result *= i
    return result