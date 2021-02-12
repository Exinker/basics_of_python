

def translate(text, delimiter=' — '):
    words = text.split(delimiter)
    words[0] = dictionary.get(words[0], words[0])

    return delimiter.join(words)


dictionary = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

#
filename = 'task_4 (incoming).txt'
with open(filename, 'r') as file:
    data_incoming = file.readlines()

data_outgoing = ''.join([translate(datum) for datum in data_incoming])

#
filename = 'task_4 (outgoing).txt'
with open(filename, 'w') as file:
    file.write(data_outgoing)
