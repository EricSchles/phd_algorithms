import random
from min_heap import MinHeap

def pop_first(listing):
    if listing == []:
        return None
    value = listing[0]
    listing.remove(value)
    return value

def sort_lists_check(lists):
    final_list = []
    heap = MinHeap()
    for l in lists:
        for elem in l:
            heap.push(elem)
    while not heap.is_empty():
        final_list.append(heap.pop())
    return final_list

def sort_lists(lists):
    final_list = []
    heap = MinHeap()
    for l in lists:
        heap.push(l[0])
    index = 0
    while not heap.is_empty():
        cur = pop_first(lists)
        if cur is not None:
            final_list.append(heap.pop())
        else:
            index += 1      
    return final_list

# Driver function
if __name__ == "__main__":
    # case 1
    arr1 = [1,3,4,5]  
    arr2 = [2,4,6,8]
    other_arr1 = arr1[:]
    other_arr2 = arr2[:]
    new_list = sort_lists([arr1, arr2])
    other_arr = other_arr1 + other_arr2
    other_arr.sort()
    assert new_list  == other_arr

    # case 2
    master_list = [random.randint(0, 1000) for _ in range(1000)]
    first = master_list[:]
    second = master_list[:]
    lists = []
    for i in range(100, 1100, 100):
        lists.append(first[i-100: i])
    for l in lists:
        l.sort()
    new_list = sort_lists(lists)
    second.sort()
    try:
        assert new_list  == second
    except:
        import code
        code.interact(local=locals())
    
