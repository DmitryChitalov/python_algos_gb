"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.
"""
from random import randint

# вложенный цикл O(n^2)
# lst = [2, 1, 3]


def search_min_value(lst):
    for i in lst:
        min_value = True
        for j in lst:
            if i > j:
                min_value = False
        if min_value:
            return i

# sort O(NlogN)
# в задании этого нет, но как вариант решения


def min_elem(lst):
    result_list = sorted(lst)
    return result_list[0]


# O(n) линейная сложность

def min_in_list(lst):
    min_value_n = lst[0]
    for i in lst:
        if i < min_value_n:
            min_value_n = i
    return min_value_n


lst2 = [randint(-10, 10) for i in range(10)]

print(lst2)
# print(search_min_value(lst))
print(search_min_value(lst2))
print(min_elem(lst2))
print(min_in_list(lst2))
