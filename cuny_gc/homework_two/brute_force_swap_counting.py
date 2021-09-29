from typing import List
import random

def brute_force_swap_count(arr: List) -> int:
    inversion_count = 0
    for index_i, value_i in enumerate(arr):
        for index_j, value_j in enumerate(arr):
            if index_i < index_j and value_i > value_j:
                inversion_count += 1
    return inversion_count
    
def fac(n):
    if n == 1:
        return 1
    else:
        return n + fac(n-1)
    
if __name__ == '__main__':
    # case 1
    listing = list(range(15, 0, -1))
    inversions = brute_force_swap_count(listing)
    print(inversions, fac(len(listing)-1))

    # case 2
    listing = [1,2,4,3,5]
    inversions = brute_force_swap_count(listing)
    print(inversions, 1)
