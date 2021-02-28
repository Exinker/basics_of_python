filename = 'task_2.txt'

lines_number = 0
words_number = []
with open(filename, 'r') as file:
    for line in file:
        lines_number += 1
        words_number.append(len(line.split()))

print(f'lines number: {lines_number}')
print(f'words number: {words_number}')
