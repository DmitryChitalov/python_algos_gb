"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Примечание:
Построить список можно через генератор списка.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""

import random

def min_str_on2(ex_list):
    min = ex_list[0]
    for i in range(1, len(ex_list)):
        for j in range(i + 1, len(ex_list)):
            if ex_list[j] < min:
                min = ex_list[j]
    return min

list = [15, 12, 45, 454, 47, 789, 78, 99, 25, 6, 17, 2]

print(f'Minimum from the list {list} is {min_str_on2(list)}')


def min_str_on(ex_list):
    min_value = ex_list[0]
    for el in ex_list:
        if min_value > el:
            min_value = el
    return min_value


def list_gen(length):
    for i in range(0, length):
        yield random.randint(0, 1000)


init_list = [el for el in list_gen(25)]

print(f'Minimum from the list {init_list} is {min_str_on(init_list)}')
