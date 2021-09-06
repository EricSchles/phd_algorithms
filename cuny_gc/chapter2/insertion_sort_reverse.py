from typing import List
import random

def insertion_sort(arr: List) -> List:
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while (i >= 0) and (arr[i] < key):
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
    return arr

if __name__ == '__main__':
    # case 1
    listing = list(range(15))
    sorted_list = listing[:]
    sorted_list.sort(reverse=True)
    assert insertion_sort(listing) == sorted_list

    # # case 2
    listing = [random.randint(0, 10000) for _ in range(10)]
    sorted_list = listing[:]
    sorted_list.sort(reverse=True)
    assert insertion_sort(listing) == sorted_list
