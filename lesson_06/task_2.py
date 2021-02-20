
class Road():

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_weight(self, density, thickness):
        return self._length * self._width * density * thickness


road = Road(5000, 20)
print(road.calculate_weight(density=25, thickness=5))
