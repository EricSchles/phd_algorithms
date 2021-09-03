import math
import numpy as np

def insertion_sort_num_ops(n):
    return 1/8*n

def merge_sort_num_ops(n):
    return math.log(n)

for i in np.arange(2, 10000):
    a = insertion_sort_num_ops(i)
    b = merge_sort_num_ops(i)
    if a > b:
        print(f"found: {i}")
        break

