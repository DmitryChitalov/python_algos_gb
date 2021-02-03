"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Примечание:
Построить список можно через списковое включение.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""


def search1(source_list):  # o(n)
    if len(source_list) == 0:
        return None
    minimum = source_list[0]
    for element in source_list:
        if element < element2:
            minimum = element1
    return minimum


def search2(source_list):  # o(n*n)
    if len(source_list) == 0:
        return None
    minimum = source_list[0]
    for element1 in source_list:
        nested_minimum = element1
        for element2 in source_list:
            if element2 < element1:
                nested_minimum = element2
        if nested_minimum < minimum:
            minimum = nested_minimum
    return minimum
