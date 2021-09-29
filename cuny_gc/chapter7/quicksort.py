from typing import List
import random

def quicksort(arr: List):
    less = []
    equal = []
    greater = []

    if len(arr) > 1:
        pivot = arr[len(arr)//2]
        for elem in arr:
            if elem < pivot:
                less.append(elem)
            elif elem == pivot:
                equal.append(elem)
            elif elem > pivot:
                greater.append(elem)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return arr
    
if __name__ == '__main__':
    # case 1
    listing = list(range(15, 0, -1))
    sorted_list = listing[:]
    sorted_list.sort()
    assert quicksort(listing) == sorted_list

    # case 2
    listing = [random.randint(0, 10000) for _ in range(10)]
    sorted_list = listing[:]
    sorted_list.sort()
    assert quicksort(listing) == sorted_list

