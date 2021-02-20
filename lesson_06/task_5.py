

class Stationery():

    def __init__(self, title=None):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):

    def draw(self):
        print('Запуск отрисовки карандашом')


class Handle(Stationery):

    def draw(self):
        print('Запуск отрисовки маркером')


pen = Pen()
pen.draw()

pencil = Pencil()
pencil.draw()

handle = Handle()
handle.draw()
