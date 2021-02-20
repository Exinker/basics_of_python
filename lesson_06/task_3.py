
class Worker():

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        print(f'{self.surname} {self.name}')

    def get_total_income(self):
        total = sum([value for key, value in self._income.items()])
        print(f'total income: {total}$')


worker = Position(
    name='Pavel',
    surname='Vaschenko',
    position=None,
    income = {
        'wage': 100,
        'bonus': 15,
    },
)
worker.get_full_name()
worker.get_total_income()
