import random

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


def search_min_1(lst):                  # Сложность: O(N^2) - квадратичная
    res = lst[0]                        # O(1) - присваивание константы
    for i in range(len(lst) - 1):       # O(N) - перебор всех индексов списка (перебор множества чисел)
        for j in lst[i+1:]:             # O(N) - цикл, перебор всех элементов списка
            if j < res:                 # O(len(...)) - сравнение значений
                res = j                 # O(1) - присваивание константы
    return res                          # O(1) - возвращение константы


def search_min_2(lst):      # Сложность: O(N) - линейная
    x = lst[0]              # O(1) - присваивание константы
    for el in lst[1:]:      # O(N) - цикл, перебор всех элементов списка
        if el < x:          # O(len(...)) - сравнение значений
            x = el          # O(1) - присваивание константы
    return x                # O(1) - возвращение константы


def search_min_2_2(lst):    # Сложность: O(N) - линейная
    res = min(lst)          # O(N) - использование стандартной функции поиска минимума + присваивание константы
    return res              # O(1) - возвращение константы


lst_1 = [random.randint(1, 100) for x in range(1, 10)]
print(search_min_1(lst_1))
print(search_min_2(lst_1))
print(search_min_2_2(lst_1))
print()
print(lst_1)

"""Вывод: 2 и 3 алгоритмы оказались менее сложными (линейные), тогда как у 1го сложность - квадратичная.
Но самым эфффективным является 3й алгоритм, так как он использует стандартную функцию поиска минимума"""
