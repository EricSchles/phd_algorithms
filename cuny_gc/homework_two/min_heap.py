class MinHeap:
    def __init__(self):
        self.arr = []
        
    def min_heapify(self, k):
        l = self.left(k)
        r = self.right(k)
        if l < len(self.arr) and self.arr[l] < self.arr[k]:
            smallest = l
        else:
            smallest = k
        if r < len(self.arr) and self.arr[r] < self.arr[smallest]:
            smallest = r
        if smallest != k:
            self.arr[k], self.arr[smallest] = self.arr[smallest], self.arr[k]
            self.min_heapify(smallest)

    def left(self, k):
        return 2 * k + 1

    def right(self, k):
        return 2 * k + 2

    def build_min_heap(self):
        n = int((len(self.arr) // 2) - 1)
        for k in range(n, -1, -1):
            self.min_heapify(k)
 
    def pop(self):
        if len(self.arr) == 0:
            raise Exception("Empty Heap")
        root = self.arr[0]
        self.arr.remove(root)
        self.build_min_heap()
        return root

    def push(self, elem):
        self.arr.append(elem)
        self.build_min_heap()

    def is_empty(self):
        return self.arr == []

if __name__ == '__main__':
    # Same tree as above example.
    my_heap = MinHeap()
    my_heap.push(5)
    my_heap.push(6)
    my_heap.push(7)
    my_heap.push(9)
    my_heap.push(13)
    my_heap.push(11)
    my_heap.push(10)

    print(my_heap.pop()) # removing min node i.e 5 
    print(my_heap.pop())
    print(my_heap.pop())
    print(my_heap.pop())
    print(my_heap.pop())
    print(my_heap.pop())
    print(my_heap.pop())
    print(my_heap.pop())
