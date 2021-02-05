seconds = int(input('Введите время в секундах: '))

hours = seconds // 3600
seconds %= 3600

minutes = seconds // 60
seconds %= 60

print(f'{hours:>02d}:{minutes:>02d}:{seconds:>02d}')
