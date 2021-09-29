def get_left(index):
    return (2*index) + 1

def get_right(index):
    return (2*index) + 2

def max_heapify(A, index):
    left = get_left(index)
    right = get_right(index)
    if left < len(A) and A[left] > A[index]:
        largest = left
    else:
        largest = index
    if right < len(A) and A[right] > A[largest]:
        largest = right
    if largest != index:
        A[index], A[largest] = A[largest], A[index]
        max_heapify(A, largest)

def build_max_heap(A):
    mid = int((len(A) // 2) - 1)
    for index in range(mid, -1, -1):
        max_heapify(A, index)

def heap_extract_max(A):
    if len(A) < 1:
        return A
    max_value = A[0]
    A[0] = A[-1]
    max_heapify(A, 0)
    return max_value

if __name__ == '__main__':
    A = [3, 9, 2, 1, 4, 5]
    build_max_heap(A)
    print(A)

    # A = list(range(10))
    # build_max_heap(A)
    # print(A)
    
