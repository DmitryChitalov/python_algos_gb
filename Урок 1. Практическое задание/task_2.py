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

from random import randint


def min1(lst):
    """Линейная сложность"""
    min_e = lst[0]
    for i in lst:
        if i < min_e:
            min_e = i
    return min_e


def min2(lst):
    """Квадратичная сложность"""
    for i in lst:
        min_e = True
        for j in lst:
            if i > j:
                min_e = False
        if min_e:
            return i


test_list = [randint(-100, 100) for i in range(0, 10)]
print(test_list)
print(min1(test_list))
print(min2(test_list))
