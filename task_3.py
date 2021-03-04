
class NotNumberError(Exception):

    def __init__(self, text):
        self.text = text


numbers = []
while True:
    number = input('Please, input a number (or Enter to stop): ')

    if number == '':
        break

    try:
        if number.isdigit():
            numbers.append(int(number))
        else:
            raise NotNumberError(f'{number} is not a number!')

    except NotNumberError as error:
        print(error)

print(numbers)
