from functools import reduce

numbers = [number for number in range(100, 1000 + 1) if (number % 2 == 0)]
print(reduce(lambda x, y: x * y, numbers))
