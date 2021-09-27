from matrix import Matrix
from random import randint

def square_matrix_multiply(A, B):
    n = len(A._matrix)
    C = Matrix((n, n))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                new_elem = C.get_at(i, j) + (A.get_at(i, k) * B.get_at(k, j))
                C.insert_at(new_elem, i, j)
    return C

if __name__ == '__main__':
    A = Matrix((2, 2))
    A.insert_at(1, 0, 0)
    A.insert_at(0, 1, 0)
    A.insert_at(0, 0, 1)
    A.insert_at(1, 1, 1)
    B = Matrix((2, 2))
    B.insert_at(randint(10, 1000), 0, 0)
    B.insert_at(randint(10, 1000), 1, 0)
    B.insert_at(randint(10, 1000), 0, 1)
    B.insert_at(randint(10, 1000), 1, 1)
    assert square_matrix_multiply(A, B).equals(B)
    
