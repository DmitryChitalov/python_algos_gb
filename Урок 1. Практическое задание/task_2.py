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

list1 = [randint(1, 100) for i in range(10)]


# O(n^2):
def func_1(the_list):
    min_el = the_list[0]
    for i in the_list:
        for j in the_list:
            if j < i and j < min_el:
                min_el = j
    return min_el


# O(n):
def func_2(the_list):
    min_el = the_list[0]
    for i in range(1, len(the_list)):
        if the_list[i] < min_el:
            min_el = the_list[i]
    return min_el


print(f'{list1}\n{func_1(list1)}\n{func_2(list1)}')
