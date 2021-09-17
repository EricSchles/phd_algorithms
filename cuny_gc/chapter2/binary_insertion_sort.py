from typing import List
import random

def binary_search(arr, val, start, end):
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1

    mid = (start+end)//2
    if arr[mid] < val:
        if mid != end:
            return binary_search(arr, val, mid+1, end)
        else:
            return binary_search(arr, val, mid, end)
    elif arr[mid] > val:
        if mid != start:
            return binary_search(arr, val, start, mid-1)
        else:
            return binary_search(arr, val, start, mid)
    else:
        return mid
    
def insertion_sort(arr: List) -> List:
    for i in range(1, len(arr)):
        val = arr[i]
        j = binary_search(arr, val, 0, i-1)
        arr = arr[:j] + [val] + arr[j:i] + arr[i+1:]
    return arr
        
if __name__ == '__main__':
    # case 1
    listing = list(range(15, 0, -1))
    sorted_list = listing[:]
    sorted_list.sort()
    assert insertion_sort(listing) == sorted_list

    # case 2
    listing = [random.randint(0, 10000) for _ in range(10)]
    sorted_list = listing[:]
    sorted_list.sort()
    assert insertion_sort(listing) == sorted_list
