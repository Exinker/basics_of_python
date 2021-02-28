import re


dictionary = {}
filename = 'task_6.txt'

with open(filename, 'r') as file:
    for line in file:
        subject, lessons = line.strip().split(': ')
        dictionary[subject] = sum([
            int(hour) for hour in re.findall(r'\d{1,}', lessons)
        ])

print(dictionary)
