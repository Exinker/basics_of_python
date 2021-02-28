from random import randint


delimiter = ', '
filename = 'task_5.txt'

# write numbers
n = 10
numbers = [randint(0, 100) for _ in range(n)]

with open(filename, 'w') as file:
    text = delimiter.join([str(number) for number in numbers])
    file.write(text)

# read and sum up numbers
with open(filename, 'r') as file:
    text = file.readline()
    
numbers = [int(number) for number in text.split(delimiter)]
print(f'Sum of numbers is {sum(numbers)}.')
