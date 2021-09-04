import time
start_time = time.time()
def factorial(n):
    #cdef int fact = 1
    #cdef int x
    fact = 1
    for x in range(1, n+1):
        fact = fact*x
    return fact

print(factorial(5))
print("time taken is = ", time.time() - start_time)
print("test1")
print("test2")
