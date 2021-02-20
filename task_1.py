
class Matrix():

    def __init__(self, data):
        self.data = data

    def __str__(self):
        text = ''
        for row in self.data:
            for column in row:
                text += f'{column}\t'

            text += '\n'
        return text

    def __add__(self, other):
        data = []
        for row_1, row_2 in zip(self.data, other.data):
            data.append([])
            for col_1, col_2 in zip(row_1, row_2):
                data[-1].append(col_1 + col_2)

        return Matrix(data)


data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_1 = Matrix(data)

data = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
matrix_2 = Matrix(data)

matrix_3 = matrix_1 + matrix_2
print(matrix_3)
