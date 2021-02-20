

class Cell():

    def __init__(self, number=0):
        self.number = number

    def __add__(self, other):
        '''Сложение. Объединение двух клеток.
        При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
        '''

        if isinstance(other, Cell):
            return Cell(self.number + other.number)
        else:
            raise 'операция определена только на клетках!'

    def __sub__(self, other):
        '''Вычитание. Участвуют две клетки.
        Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля,
        иначе выводить соответствующее сообщение.
        '''

        if isinstance(other, Cell):
            if self.number > other.number:
                return Cell(self.number - other.number)
            else:
                print('разность количества ячеек двух клеток меньше нуля!')
        else:
            raise 'операция определена только на клетках!'

    def __mul__(self, other):
        '''Умножение. Создается общая клетка из двух.
        Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
        '''

        if isinstance(other, Cell):
            return Cell(self.number * other.number)
        else:
            raise 'операция определена только на клетках!'

    def __truediv__(self, other):
        '''Деление. Создается общая клетка из двух.
        Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
        '''

        if isinstance(other, Cell):
            return Cell(round(self.number / other.number))
        else:
            raise 'операция определена только на клетках!'

    def make_order(self, n):
        body = ['*' * n + '\n' for _ in range(self.number // n)]
        modulo = ['*' for _ in range(self.number % n)]
        return ''.join(body + modulo)


cell_1 = Cell(14)
cell_2 = Cell(5)

cell_3 = cell_1 + cell_2
print(f'check add:\n{cell_3.make_order(10)}', end='\n\n')

cell_3 = cell_1 - cell_2
print(f'check sub:\n{cell_3.make_order(10)}', end='\n\n')

cell_3 = cell_1 * cell_2
print(f'check mul:\n{cell_3.make_order(10)}', end='\n\n')

cell_3 = cell_1 / cell_2
print(f'check truediv:\n{cell_3.make_order(10)}', end='\n\n')
