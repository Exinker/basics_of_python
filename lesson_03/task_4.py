

def my_func(x, y):
    return x ** y


def my_func_updated_v1(x, y):
    if y < 0:
        return my_func_updated_v1(1/x, -y)

    answer = 1
    for _ in range(y):
        answer *= x

    return answer


def my_func_updated_v2(x, y):
    if y < 0:
        return my_func_updated_v2(1/x, -y)

    if y == 1:
        return x
    else:
        if y % 2 == 0:
            return my_func_updated_v2(x * x, y / 2)
        else:
            return x * my_func_updated_v2(x, y - 1)


x, y = 5, -2
print(my_func(x, y))
print(my_func_updated_v1(x, y))
print(my_func_updated_v2(x, y))
