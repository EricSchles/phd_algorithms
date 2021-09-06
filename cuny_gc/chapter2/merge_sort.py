from typing import List
import random

def merge(left: List, right: List) -> List:
    left_index = 0
    right_index = 0
    final = []
    while (left_index < len(left)) and (right_index < len(right)):
        if (left[left_index] < right[right_index]):
            final.append(left[left_index])
            left_index += 1
        elif right[right_index] < left[left_index]:
            final.append(right[right_index])
            right_index += 1
    
    while left_index < len(left):
        final.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        final.append(right[right_index])
        right_index += 1

    return final

def mergesort(arr: List) -> List:
    if len(arr) <= 1:
        return arr
    mid_point = len(arr)//2
    left = mergesort(arr[:mid_point])
    right = mergesort(arr[mid_point:])
    return merge(left, right)

if __name__ == '__main__':
    # case 1
    listing = list(range(15, 0, -1))
    sorted_list = listing[:]
    sorted_list.sort()
    assert mergesort(listing) == sorted_list

    # case 2
    listing = [random.randint(0, 10000) for _ in range(10)]
    sorted_list = listing[:]
    sorted_list.sort()
    assert mergesort(listing) == sorted_list
