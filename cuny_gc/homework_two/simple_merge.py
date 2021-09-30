import random
from min_heap import MinHeap

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return repr(self.data)
    
def sort_lists(lists):
    final_list = []
    heap = MinHeap()
    for l in lists:
        heap.push((l.data, l))
    while not heap.is_empty():
        data, node = heap.pop()
        final_list.append(data)
        node = node.next
        if node:
            heap.push((node.data, node))
    return final_list

def to_linked_lists(lists):
    linked_lists = []
    # get heads
    for l in lists:
        linked_lists.append(Node(l[0]))
    for index, l in enumerate(lists):
        head = linked_lists[index]
        cur = head
        for elem in l[1:]:
            cur.next = Node(elem)
            cur = cur.next
    return linked_lists
        
# Driver function
if __name__ == "__main__":
    # case 1
    arr1 = [1,3,4,5]  
    arr2 = [2,4,6,8]
    other_arr1 = arr1[:]
    other_arr2 = arr2[:]
    lists = [arr1, arr2]
    linked_lists = to_linked_lists(lists)
    new_list = sort_lists(linked_lists)
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
    linked_lists = to_linked_lists(lists)
    new_list = sort_lists(linked_lists)
    second.sort()
    assert new_list  == second
    
