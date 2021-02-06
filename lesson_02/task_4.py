string = input('Введите строку: ')

for i, word in enumerate(string.split(' ')):
    print(f'{str(i):>2s} {word[:10]}')
