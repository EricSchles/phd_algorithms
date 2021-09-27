class Matrix:
    def __init__(self, shape):
        self._matrix = []
        for col_index in range(shape[1]):
            self._matrix.append([])
            for row_index in range(shape[0]):
                self._matrix[col_index].append(0)

    def insert_at(self, elem, row_index, col_index):
        self._matrix[col_index][row_index] = elem

    def get_at(self, row_index, col_index):
        return self._matrix[col_index][row_index]

    def equals(self, other_matrix):
        equality = []
        for col_index in range(len(self._matrix)):
            for row_index in range(len(self._matrix)):
                equality.append(
                    self.get_at(
                        row_index, col_index
                    ) == other_matrix.get_at(
                        row_index, col_index
                    ))
        return all(equality)
            
    def __str__(self):
        return repr(self._matrix)
    
    

     
    
