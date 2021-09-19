from typing import List
import random

def merge_sort(k: int, arr: List) -> List:
    if len(arr) <= k:
        return insertion_sort(arr)
    else:
        mid = len(arr)//2
        left = merge_sort(k, arr[:mid])
        right = merge_sort(k, arr[mid:])
        return merge(left, right)

def merge(left, right):
    left_index = 0
    right_index = 0
    new_arr = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            new_arr.append(left[left_index])
            left_index += 1
        else:
            new_arr.append(right[right_index])
            right_index += 1
    while left_index < len(left):
        new_arr.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        new_arr.append(right[right_index])
        right_index += 1
    return new_arr

def insertion_sort(arr: List) -> List:
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
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

    # case 1
    listing = list(range(15, 0, -1))
    sorted_list = listing[:]
    sorted_list.sort()
    assert merge_sort(listing, 5) == sorted_list

    # case 2
    listing = [random.randint(0, 10000) for _ in range(10)]
    sorted_list = listing[:]
    sorted_list.sort()
    assert merge_sort(listing, 5) == sorted_list

            
