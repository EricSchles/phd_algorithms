from typing import List

# To Do
def quicksort(arr: List, p, r):
    if p < r:
        q, t = partition_prime(arr, p, r)
        quicksort(arr, p, q-1)
        quicksort(arr, t+1, r)

def partition_prime(arr, p, r):
    x = arr[p]
    low = p
    high = p
    for j in range(p+1, r):
        if arr[j] < x:
            arr[low], arr[high + 1] = arr[high + 1], arr[low] 
            low += 1
            high += 1
        elif arr[j] == x:
            arr[high + 1], arr[j] = arr[j], arr[high + 1]
            high += 1
    return low, high

if __name__ == '__main__':
    arr = list(range(10))
    arr2 = arr[:]
    arr2.sort()
    arr = arr[::-1]
    quicksort(arr, 0, len(arr)-1)
    print(arr)
    print(arr2)
    assert arr == arr2
