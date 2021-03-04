
class Storage():

    def __init__(self, items=None):
        self.items = [] if items is None else items


class Equipment():

    def __init__(self, id, max_format='A4', ppm=21, dpi=600):
        self.id = id
        self.max_format = max_format  # maximum page format
        self.ppm = ppm  # pages per minute
        self.dpi = dpi  # dots per inch


class Printer(Equipment):

    def __init__(self, id, capacity=150, *args, **kwargs):
        super().__init__(id, args, kwargs)

        self.type = 'printer'
        self.capacity = capacity  # number of sheets of paper in a tray


class Scanner(Equipment):

    def __init__(self, id, *args, **kwargs):
        super().__init__(id, args, kwargs)

        self.type = 'scanner'


class Copier(Equipment):

    def __init__(self, id, capacity=150, *args, **kwargs):
        super().__init__(id, args, kwargs)

        self.type = 'copier'
        self.capacity = capacity  # number of sheets of paper in a tray


items = [
    Printer(id='544545'),
    Scanner(id='544541'),
]
storage = Storage(items)
