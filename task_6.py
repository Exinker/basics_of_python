
class Storage():

    def __init__(self, items=None):
        self.balance = {key: [] for key in ['printer', 'scanner', 'copier']}
        self.id = []

        #
        items = [] if items is None else items
        for item in items:
            self.add(item)

    def add(self, item):
        category = item.category

        # validate
        if not isinstance(item, Equipment):
            raise TypeError(f'{item} should be a instance of Equipment!')

        #
        self.balance[category].append(item)

    def remove(self, category, quantity=1):

        # validate
        if not isinstance(quantity, int):
            raise TypeError(f'{category} quantity should be a number!')

        if not quantity > 0:
            raise TypeError(f'{category} quantity should be a positive number!')

        if len(self.balance[category]) < quantity:
            raise ValueError(f'not enough {category} on the storage!')

        #
        for i in range(quantity):
            self.balance[category].pop()


class Equipment():

    def __init__(self, id, max_format='A4', ppm=21, dpi=600):
        self.id = id
        self.max_format = max_format  # maximum page format
        self.ppm = ppm  # pages per minute
        self.dpi = dpi  # dots per inch


class Printer(Equipment):

    def __init__(self, id, capacity=150, *args, **kwargs):
        super().__init__(id, args, kwargs)

        self.category = 'printer'
        self.capacity = capacity  # number of sheets of paper in a tray


class Scanner(Equipment):

    def __init__(self, id, *args, **kwargs):
        super().__init__(id, args, kwargs)

        self.category = 'scanner'


class Copier(Equipment):

    def __init__(self, id, capacity=150, *args, **kwargs):
        super().__init__(id, args, kwargs)

        self.category = 'copier'
        self.capacity = capacity  # number of sheets of paper in a tray


items = [
    Printer(id='544545'),
    Scanner(id='544541'),
]
storage = Storage(items)
storage.add(Printer(id='544546'))
storage.add(Printer(id='544547'))
storage.remove(category='copier', quantity=2)

for key, items in storage.balance.items():
    for item in items:
        print(item.category, item.id)
