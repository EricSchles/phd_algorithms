# https://fullyunderstood.com/pseudocodes/heap-sort/

def get_left(index):
    return (2*index) 

def get_right(index):
    return (2*index) + 1

def max_heapify(A, n, index):
    largest = index
    left = get_left(index)
    right = get_right(index)

    if left < n and A[left] > A[index]:
        largest = left
    if right < n and A[right] > A[largest]:
        largest = right
    if largest != index:
        A[index], A[largest] = A[largest], A[index]
        # print(A)
        # print("index", index)
        # print("left", left)
        # print("right", right)
        # print("largest", largest)
        max_heapify(A, n, largest)
        
def build_max_heap(A):
    n = len(A)    
    for index in range(n, 0, -1):
        #print("mid", index)
        max_heapify(A, n, index)

def max_heapsort(A):
    n = len(A)
    build_max_heap(A)
    for index in range(n-1, 0, -1):
        A[0], A[index] = A[index], A[0]
        max_heapify(A, index, 0)
        
def heap_extract_max(A):
    if len(A) < 1:
        return A
    max_value = A[0]
    A[0] = A[-1]
    max_heapify(A, 0)
    return max_value

if __name__ == '__main__':
    #A = [5,3,17,10,84,19,6,22,9]
    import random
    A = [random.randint(0, 1000) for _ in range(100)]
    #print(A)
    build_max_heap(A)
    #print(A)
    sorted_A = A[:]
    sorted_A.sort()
    try:
        max_heapsort(A)
        assert A == sorted_A
    except:
        print("failed")
        import code
        code.interact(local=locals())
        #print(max_heapsort(A))
        #print(sorted_A)
    
