
class Storage():

    def __init__(self, items=None):
        self.balance = {
            'printer': [],
            'scanner': [],
            'copier': [],
        }

        items = [] if items is None else items
        for item in items:
            self.add(item)

    def add(self, item):
        key = item.type_of_equipment

        self.balance[key].append(item)

    def remove(self, type_of_item, number_of_item=1):
        key = type_of_item

        for i in range(number_of_item):
            self.balance[key].pop()


class Equipment():

    def __init__(self, id, max_format='A4', ppm=21, dpi=600):
        self.id = id
        self.max_format = max_format  # maximum page format
        self.ppm = ppm  # pages per minute
        self.dpi = dpi  # dots per inch


class Printer(Equipment):

    def __init__(self, id, capacity=150, *args, **kwargs):
        super().__init__(id, args, kwargs)

        self.type_of_equipment = 'printer'
        self.capacity = capacity  # number of sheets of paper in a tray


class Scanner(Equipment):

    def __init__(self, id, *args, **kwargs):
        super().__init__(id, args, kwargs)

        self.type_of_equipment = 'scanner'


class Copier(Equipment):

    def __init__(self, id, capacity=150, *args, **kwargs):
        super().__init__(id, args, kwargs)

        self.type_of_equipment = 'copier'
        self.capacity = capacity  # number of sheets of paper in a tray


items = [
    Printer(id='544545'),
    Scanner(id='544541'),
]
storage = Storage(items)
storage.add(Printer(id='544546'))
storage.add(Printer(id='544547'))
storage.remove(type_of_item='printer', number_of_item=3)

for key, items in storage.balance.items():
    for item in items:
        print(item.type_of_equipment, item.id)
