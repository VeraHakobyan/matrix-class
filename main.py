class Matrix:
    matrix = [[]]

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        for row in self.matrix:
            for col in row:
                print(col, end=" ")
            print()
        return ""

    def __add__(self, other):
        new_matrix = [x[:] for x in self.matrix]
        for i in range(len(new_matrix)):
            for j in range(len(new_matrix[i])):
                new_matrix[i][j] += other.matrix[i][j]
        return Matrix(new_matrix)

    def __mul__(self, other):
        new_matrix = [x[:] for x in self.matrix]
        if isinstance(other, Matrix):
            for i in range(len(new_matrix)):
                for j in range(len(new_matrix[i])):
                    new_matrix[i][j] *= other.matrix[i][j]
        else:
            for i in range(len(new_matrix)):
                for j in range(len(new_matrix[i])):
                    new_matrix[i][j] *= other
        return Matrix(new_matrix)

    def __matmul__(self, other):
        new_matrix = [x[:] for x in self.matrix]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                new_matrix[i][j] = 0
                for z in range(len(other.matrix[i])):
                    new_matrix[i][j] += self.matrix[i][z] * other.matrix[z][j]
        return Matrix(new_matrix)

    def transpose(self):
        new_matrix = [list(i) for i in zip(*self.matrix)]
        return Matrix(new_matrix)

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])
result = m1 + m2
print(result)
print("--------------------------------------------------------")
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])
scalar = 2
result1 = m1 * scalar
result2 = m1 * m2
print(result1)
print(result2)
print("--------------------------------------------------------")
m = Matrix([[1, 2, 3], [4, 5, 6]])
result = m.transpose()
print(result)