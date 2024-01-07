from datetime import datetime
from numba import jit, njit, prange

# @jit
# @njit(parallel=True)
def foo():
    sum = 0
    for i in range(1, 1_00000_001):
        i = str(i)
        for j in i:
            j = int(j)
            sum += j

    return sum
start_t = datetime.now()
foo()
print(datetime.now() - start_t)
print(sum)