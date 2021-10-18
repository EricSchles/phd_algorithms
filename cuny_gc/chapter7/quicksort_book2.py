from typing import List
from random import randint

def quicksort(arr: List, p, r):
    if p < r:
        q = random_partition(arr, p, r)
        quicksort(arr, p, q-1)
        quicksort(arr,q+1,r)

def partition(arr, p, r):
    x = arr[r]
    i = p-1
    for j in range(p, r):
        if arr[j] <= x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i + 1

def random_partition(arr, p, r):
    i = randint(p, r)
    arr[r], arr[i] = arr[i], arr[r]
    return partition(arr, p, r)
    
if __name__ == '__main__':
    arr = list(range(10))
    arr2 = arr[:]
    arr2.sort()
    arr = arr[::-1]
    quicksort(arr, 0, len(arr)-1)
    assert arr == arr2
