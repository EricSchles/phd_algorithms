def counting_sort(A, B, k):
    C = [0 for i in range(k)]
    for j in range(len(A)-1):
        C[A[j]] += 1
    for i in range(1, k):
        C[i] += C[i-1]
    for j in range(len(A)-1, -1, -1):
        B[C[A[j]]] = A[j]
        C[A[j]] -= 1
        
if __name__ == '__main__':
    arr = list(range(10))
    arr = arr[::-1]
    b = [0 for i in range(len(arr))]
    counting_sort(arr, b, max(arr)+1)
