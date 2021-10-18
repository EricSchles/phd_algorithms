from typing import List

def quicksort(arr: List, p, r):
    if p < r:
        q = partition(arr, p, r)
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

if __name__ == '__main__':
    arr = list(range(10))
    arr2 = arr[:]
    arr2.sort()
    arr = arr[::-1]
    quicksort(arr, 0, len(arr)-1)
    assert arr == arr2
