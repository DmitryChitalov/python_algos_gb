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
import time


def min_1(my_list):
    min_value = my_list[0]
    min_index = 0

    for i in range(1, len(my_list)):
        if my_list[i] < min_value:
            min_value = my_list[i]
            min_index = i

    return min_index


def lst_sort(my_list):
    newlst = []
    start_val = time.time()

    for i in range(len(my_list)):
        min_i = min_1(my_list)
        newlst.append(my_list.pop(min_i))

    end_val = time.time()
    print("время алгоритма O(N^2): ", end_val - start_val)

    return newlst[0]


def min_2(my_list):
    min_value = my_list[0]
    start_val = time.time()

    for i in range(len(my_list)):
        if my_list[i] < min_value:
            min_value = my_list[i]

    end_val = time.time()
    print("время алгоритма O(N): ", end_val - start_val)

    return min_value


my_list = [random.randint(1, 100) for i in range(1, 10000)]
print(my_list)

print(min_2(my_list))

print(lst_sort(my_list))
