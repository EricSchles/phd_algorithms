import math
import numpy as np

def algo_one(n):
    return 100*n*n

def algo_two(n):
    return 2**n

for i in np.arange(2, 10000):
    a = algo_one(i)
    b = algo_two(i)
    if b > a:
        print(f"found: {i}")
        break
