

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
        print('Ошибка деления на ноль!')

    return result


a = float(input('Введите числитель: '))
b = float(input('Введите знаменатель: '))

print(divide(a, b))
