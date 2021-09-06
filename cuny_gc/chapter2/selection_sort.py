from typing import List
import random

def selection_sort(arr: List) -> List:
    i = 0
    while i < len(arr):
        key = arr[i]
        j = i
        smallest = arr[j]
        smallest_index = j
        while j < len(arr):
            if arr[j] < smallest:
                smallest = arr[j]
                smallest_index = j
            j += 1
        arr[i] = smallest
        arr[smallest_index] = key
        i += 1
    return arr

if __name__ == '__main__':
    listing = list(range(16, 0, -1))
    sorted_list = listing[:]
    sorted_list.sort()
    assert selection_sort(listing) == sorted_list

    listing = [random.randint(0, 10000) for _ in range(10)]
    sorted_list = listing[:]
    sorted_list.sort()
    assert selection_sort(listing) == sorted_list

