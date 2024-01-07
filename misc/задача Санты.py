from datetime import datetime
from numba import njit, prange, cuda
n = int(input())
mass = 10 ** n
# @cuda.jit
@njit(parallel=True)
def foo():
    sum = 0
    for i in prange(1, mass+1):
        if i >= 10:
            while i >= 10:
                last_digit = i % 10
                sum += last_digit
                i = i // 10
            sum += i
        else:
            sum += i
    print(sum)
start_t = datetime.now()
foo()
print(datetime.now() - start_t)
