from typing import List
import random

def quicksort(arr: List):
    less = []
    equal = []
    greater = []

    if len(arr) > 1:
        pivot = arr[len(arr)//2]
        print(f"First we find the middle number: {pivot}")
        print()
        print(f"this is at position: {len(arr)//2}")
        print()
        print("then we put each element in a less list, a greater list, or a list equal to the pivot")
        print()
        for elem in arr:
            if elem < pivot:
                less.append(elem)
            elif elem == pivot:
                equal.append(elem)
            elif elem > pivot:
                greater.append(elem)
        print(f"This time the less list is: {less}")
        print()
        print(f"This time the greater list is: {greater}")
        print()
        print(f"this time the equal list is: {equal}")
        print()
        print("Then we recurse and the whole process starts all over again")
        print()
        print()
        return quicksort(less) + equal + quicksort(greater)
    else:
        return arr
    
if __name__ == '__main__':
    # case 1
    # listing = list(range(15, 0, -1))
    # sorted_list = listing[:]
    # sorted_list.sort()
    # assert quicksort(listing) == sorted_list

    # # case 2
    # listing = [random.randint(0, 10000) for _ in range(10)]
    # sorted_list = listing[:]
    # sorted_list.sort()
    # assert quicksort(listing) == sorted_list
    listing = [5,3,17,10,84,19,6,22]
    quicksort(listing)
