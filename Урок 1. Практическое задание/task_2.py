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

from random import random


def min_elem_1(lst):  # O(n^2)
    inner_list = lst[:]  # O(n)
    for i in range(len(inner_list)):  # O(n)
        for j in range(len(inner_list)):  # O(n)
            if inner_list[i] < inner_list[j]:  # O(1)
                inner_list[i], inner_list[j] = inner_list[j], inner_list[i]  # O(1)
    print(inner_list)  # O(1)
    return inner_list[0]  # O(1)


def min_elem_2(lst):  # O(n)
    min_elem = lst[0]  # O(1)
    for i in lst[1:]:  # O(n)
        if i < min_elem:  # O(1)
            min_elem = i  # O(1)
    return min_elem  # O(1)


if __name__ == '__main__':
    lst = [int(100 * random()) for i in range(10)]  # O(n)
    print(lst)

    min_1 = min_elem_1(lst)
    min_2 = min_elem_2(lst)
    print(min_1, min_2)
