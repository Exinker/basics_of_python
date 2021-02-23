

def factorial(n):
    return n * factorial(n - 1) if n > 1 else 1


def fact(n):
    for i in range(n + 1):
        yield factorial(i)


n = int(input('input n: '))
for el in fact(n):
    print(el)
