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

lst = [i for i in range(0, 10, 2)]
print(lst)


def min_n2(lst):
    for i1 in lst:
        is_min = True
        for i2 in lst:
            if i1 > i2:
                is_min = False
        if is_min:
            return i1


def min_n(lst):
    min = lst[0]

    for i in lst:
        if min > i:
            min = i
    return min


print(min_n2(lst))
print(min_n(lst))
