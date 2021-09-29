def get_left(index):
    return (2 * index) + 1

def get_right(index):
    return (2 * index) + 2

def min_heapify(arr, index):
    left = get_left(index)
    right = get_right(index)

    if left < len(arr) and arr[left] < arr[index]:
        smallest = left
    else:
        smallest = index
    if right < len(arr) and arr[right] < arr[smallest]:
        smallest = right
    if smallest != index:
        arr[index], arr[smallest] = arr[smallest], arr[index]
        min_heapify(arr, smallest)

def build_min_heap(arr):
    n = int((len(arr) // 2) - 1)
    for index in range(n, -1, -1):
        min_heapify(arr, index)

def heap_extract_min(A):
    if len(A) < 1:
        return A
    min_value = A[0]
    A[0] = A[-1]
    min_heapify(A, 0)
    return min_value

if __name__ == '__main__':
    a = [3, 9, 2, 1, 4, 5]
    build_min_heap(a)
    print(a)
