from itertools import count, cycle

n = int(input('input n: '))

for number in count(n):
    print(number)

    if number >= 10:
        break
