"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def list_generator(elem):
    k = 1
    l = [1]
    for i in range(elem):
        k = -k
        k = k / 2
        l.append(k)
    return l


def sum_recursion(l, n_els, ittrs):
    ittrs += 1
    if len(l) == 1:
        print(1)
        exit()
    else:
        tmp_sum = l[0] + l[1]
        del l[0:2]
        if len(l) == 0:
            print(tmp_sum)
            exit()
        l.insert(0, tmp_sum)
    if ittrs >= n_els:
        print(tmp_sum)
        exit()
    else:
        sum_recursion(l, n_els, ittrs)


try:
    user_elem = int(input("Введите количество элементов: "))
    list_numbers = list_generator(user_elem - 1)
    sum_recursion(list_numbers, user_elem, 1)
    # print(list_numbers)
except ValueError:
    print('введена строка !')
