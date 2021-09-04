from numba import jit
import time
start_time = time.time()

@jit
def factorial(n):                                                               
    fact = 1                                                                    
    for x in range(1, n+1):                                                     
        fact = fact*x                                                           
    return fact   

print("factorial is %s"%(factorial(100000)))
print("time taken %s"%(time.time() - start_time))
