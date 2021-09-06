from typing import List
import random

def insertion_sort(arr: List) -> List:
    if len(arr) <= 1:
        print("got here")
        return arr
    key = arr[-1]
    result = insertion_sort(arr[:-1])
    if key < result[0]:
        result.insert(0, key)
    elif key >= result[-1]:
        result.append(key)
    else:
        for index, element in enumerate(result[:-1]):
            if key > element and key < result[index+1]:
                result.insert(index+1, key)
    return result
    
    
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

