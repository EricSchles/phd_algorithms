from typing import List
import time

def iterative_binary_search(arr: List, value: int) -> int:
    low = 0
    high = len(arr)-1
    while low < high:
        mid_point = (high + low)//2
        if arr[mid_point] < value:
            low = mid_point + 1
        elif arr[mid_point] > value:
            high = mid_point - 1
        elif arr[mid_point] == value:
            return mid_point 
    return -1

listing = list(range(200))
print(iterative_binary_search(listing, 204))

