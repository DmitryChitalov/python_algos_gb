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

from random import randrange

lst = [randrange(1,101) for i in range(10)]
print(lst)

reference = min(lst)      # O(n)
print(reference)

def min_n(lst):           # O(n)
    result = lst[0]
    for i in lst:         # O(n)
        if result > i:
            result = i
    return result

res_n = min_n(lst)
print(res_n, res_n == reference)

def min_n_2(lst):               # O(n^2)
    def is_min(n):              # O(n)
        for i in lst:           # O(n)
            if i<n:
                return False
        return True

    for i in lst:         # O(n^2)
        if is_min(i):     # O(n)
            return i

res_n_2 = min_n_2(lst)
print(res_n_2, res_n_2 == reference)
