

def my_func(a, b, c):
    numbers = [a, b, c]
    numbers.sort()

    return sum(numbers[1:])


answer = my_func(1, 2, 3)
print(answer)
