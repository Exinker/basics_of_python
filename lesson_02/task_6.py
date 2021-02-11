# create the products data structure
# products = [
#     (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
#     (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}), 
#     (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
# ]

products = []
while True:
    properties = {}

    name = input('Введите название товара или нажмите Enter, если хотите остановиться: ')
    if name == '':
        break
    else:
        properties['name'] = name
        properties['price'] = float(input('Введите цену товара: '))
        properties['quantity'] = int(input('Введите количество товара: '))
        properties['unit'] = input('Введите единицy измерения товара: ')

    products.append((len(products) + 1, properties))

for product in products:
    print(product)

# create the analytics data structure
analytics = {}
for product in products:
    i, properties = product

    for key, value in properties.items():
        if key not in analytics:
            analytics[key] = []

        if value not in analytics[key]:
            analytics[key].append(value)

print(analytics)
