filename = 'task_1.txt'

with open(filename, 'w') as file:
    while True:
        data = input('Input data (to end press Enter): ')

        if data == '':
            break
        else:
            file.write(data + '\n')
