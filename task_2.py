
from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def fabric(self):
        pass


class Coat(Clothes):

    def __init__(self, size):
        super().__init__()

        self.size = size
    
    @property
    def fabric(self):
        return f'{self.size/6.5 + 0.5:.2f}m'


class Suit(Clothes):

    def __init__(self, height):
        super().__init__()

        self.height = height
    
    @property
    def fabric(self):
        return f'{self.height*2 + 0.3:.2f}m'


coat = Coat(size=50)
print(coat.fabric)

suit = Suit(height=2)
print(suit.fabric)
