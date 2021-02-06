# the first variant

flag = True
answer = 0

while flag:
    items = input('Введите строку чисел, разделенных пробелом: ').split(' ')

    for item in items:
        try: 
            answer += float(item)
        except ValueError:
            if item == '#':
                flag = False

            break

    print(answer)


# the second variant


def summarize(items, answer):
    numbers = [float(item) for item in items]
    answer += sum(numbers)

    print(answer)

    return answer


def run_recursion_v1(answer=0):
    items = input('Введите строку чисел, разделенных пробелом: ').split(' ')

    if '#' in items:
        items = items[:items.index('#')]
        answer = summarize(items, answer)

    else:
        answer = summarize(items, answer)

        run_recursion_v1(answer)


run_recursion_v1()

# the third variante


def run_recursion_v2(answer=0):
    items = input('Введите строку чисел, разделенных пробелом: ').split(' ')

    for item in items:
        try: 
            answer += float(item)
        except ValueError:
            if item == '#':
                print(answer)
                return

    print(answer)
    run_recursion_v2(answer)


run_recursion_v2()
