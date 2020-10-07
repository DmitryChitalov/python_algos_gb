#! /bin/python3
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


def min1(lst):
    """Квадратичная сложность"""
    min_e = None
    for i in lst:
        for j in lst:
            if i < j:
                min_e = i
            else:
                min_e = j
        if i < 
    return min_e


def min2(lst):
    """Линейная сложность"""
    min_e = lst[0]
    for i in lst[1:]:
        if i < min_e:
            min_e = i
    return min_e


test_list = [random.randint(-100, 100) for i in range(0, 10)]
print(test_list)
print(min1(test_list))
print(min2(test_list))

