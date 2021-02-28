import json


# part I
firms, profit = {}, {}

filename = 'task_7.txt'
with open(filename, 'r') as file:
    for line in file:
        name, form, revenue, cost = line.strip().split(' ')

        firms[name] = float(revenue) - float(cost)

    items = [value for key, value in firms.items() if value > 0]
    profit['average_profit'] = sum(items) / len(items)

# part II
filename = 'task_7.json'
with open(filename, 'w') as file:
    json.dump([firms, profit], file)
