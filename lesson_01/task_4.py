#  the first variante
n = input('Введите целое и положительное число: ')

i = 0
maximum = None
while i < len(n):
    number = int(n[i])
    
    if (maximum is None) or (number > maximum):
        maximum = number

    i += 1

print(maximum)

#  the second variante
n = input('Введите целое и положительное число: ')

maximum = None
while n:
    number = int(n[0])
    
    if (maximum is None) or (number > maximum):
        maximum = number

    n = n[1:]

print(maximum)

#  the third variante
n = int(input('Введите целое и положительное число: '))

maximum = 0
while n % 10:
    number = n % 10
    
    if number > maximum:
        maximum = number

    n //= 10

print(maximum)
