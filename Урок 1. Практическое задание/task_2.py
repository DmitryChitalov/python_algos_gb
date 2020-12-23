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


def linear_min_in_list(our_list):
    min_list_value = our_list[0]
    for el in our_list:
        if el < min_list_value:
            min_list_value = el
    return min_list_value


def quadratic_min_in_list(our_list):
    for el1 in our_list:
        check_box = True
        for el2 in our_list:
            if el1 > el2:
                check_box = False
        if check_box:
            return el1


our_min, our_max, gen_list_len = -100, 100, 30

gen_list = [randint(our_min, our_max) for _ in range(gen_list_len)]
print(gen_list)
print(linear_min_in_list(gen_list))
print(quadratic_min_in_list(gen_list))
