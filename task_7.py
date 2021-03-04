
class ComplexNumber():

    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def __str__(self):
        return f'{self.re} + j{self.im}'

    def __add__(self, other):
        try:
            if isinstance(other, ComplexNumber):
                re = self.re + other.re
                im = self.im + other.im

                return ComplexNumber(re, im)

            else:
                raise TypeError(f'{other} is not a ComplexNumber object!')

        except TypeError as error:
            print(error)

    def __mul__(self, other):
        try:
            if isinstance(other, ComplexNumber):
                re = self.re*other.re - self.im*other.im
                im = self.re*other.im + other.re*self.im

                return ComplexNumber(re, im)

            else:
                raise TypeError(f'{other} is not a ComplexNumber object!')

        except TypeError as error:
            print(error)


a = ComplexNumber(1, 2)
b = ComplexNumber(3, 5)
print(f'a = {a}')
print(f'b = {b}')

print(f'a + b = ({a}) + ({b}) = {a + b}')
print(f'a * b = ({a}) * ({b}) = {a * b}')
