revenue = float(input('Введите доход: '))
cost = float(input('Введите издержки: '))

profit = revenue - cost

if profit > 0:
    print('Вы работаете с прибылью')
    print(f'Рентабельность выручки: {profit / revenue}')

    employers = int(input('Введите количество сотрудников: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника: {profit / employers}')

else:
    print('Вы работаете с убытками')
