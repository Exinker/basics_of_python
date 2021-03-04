
class MyZeroDivisionError(Exception):

    def __init__(self, text):
        self.text = text


a, b = [float(x) for x in input('Input a fraction (a/b):').split('/')]

try:
    if b == 0:
        raise MyZeroDivisionError('b should be a non zero value!')

    answer = a / b

except MyZeroDivisionError as error:
    print(error)
