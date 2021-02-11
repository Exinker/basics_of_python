ranking = [7, 5, 3, 3, 2]

while True:
    number = int(input('Введите натуральное число: '))

    for i, item in enumerate(ranking):
        if number > item:
            ranking.insert(i, number)
            break
    else:
        ranking.append(number)

    print(ranking)
