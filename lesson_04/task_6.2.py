from itertools import count, cycle

numbers = [1, 2, 3]

i = 0
for number in cycle(numbers):
    i += 1
    print(number)

    if i >= 10:
        break
