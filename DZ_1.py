class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

        
    def __add__(self, other):
        result = ([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        
        for i in range(len(self.matrix)):                                    
            for el in range(len(self.matrix[i])):
                result[i][el] = self.matrix[i][el] + other.matrix[i][el]
        return Matrix(result)
        
    def __str__(self):
        return '\n'.join(map(str, self.matrix))


matrix_1 = Matrix ([[5, 2, 8], [1, 6, 9], [7, 4, 8]])
matrix_2 = Matrix ([[2, 3, 15], [4, 3, 11], [2, 1, 26]])
print(matrix_1 + matrix_2)
