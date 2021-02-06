items = input('Введите список: ').split()

for i in range(0, len(items) - 1, 2):
    items[i], items[i + 1] = items[i + 1], items[i]

print(items)
