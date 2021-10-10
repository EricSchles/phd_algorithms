# https://www.programiz.com/dsa/heap-data-structure
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2 
    
    if l < n and arr[i] < arr[l]:
        largest = l
    
    if r < n and arr[largest] < arr[r]:
        largest = r
    
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        print(arr)
        heapify(arr, n, largest)

def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum);
        for i in range((size//2)-1, -1, -1):
            heapify(array, size, i)

def build_max_heap(A):
    arr = []
    for elem in A:
        insert(arr, elem)
    return arr

def max_heapsort(A):
    n = len(A)
    A = build_max_heap(A)
    for index in range(n-1, 0, -1):
        A[0], A[index] = A[index], A[0]
        heapify(A, index, 0)
    return A

if __name__ == '__main__':
    A = [5,3,17,10,84,19,6,22,9]
    A2 = A[:]
    print("start build max heap")
    arr2 = build_max_heap(A2)
    print(arr2)
    print("end build max heap")
    print()
    print("start heapsort")
    arr = max_heapsort(A)
    print(arr)
    print("end heapsort")
