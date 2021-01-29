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


def check_1(lst_obj):
    """Функция должна создать множество из списка.
    """
    lst_to_set = set(lst_obj)  # O(n)
    return lst_to_set


def min_value_long(lst_obj):
    """Функция должна искать минимальное значение из списка,
    путем сравнения каждого числа со всеми другими элементами списка.
    """
    min_val = lst_obj[0]

    for j in range(len(lst_obj)):
        for i in range(len(lst_obj)):
            if lst_obj[i] < lst_obj[j] and lst_obj[i] < min_val:
                min_val = lst_obj[i]
    return min_val


def min_value_fast(lst_obj):
    """Функция должна искать минимальное значение из списка.
    """

    min_val = lst_obj[0]

    for j in range(len(lst_obj)):
        if lst_obj[j] < min_val:
            min_val = lst_obj[j]
    return min_val


for k in (50, 500, 1000, 5000, 1000):
    # Из 100000 чисел возьмем 'j' случайно выбранных
    # Всего 10 тыс. чисел
    lst = random.sample(range(-100000, 100000), k)

print(check_1(lst))
print("O(n**2): ", min_value_long(lst))
print("O(n): ", min_value_fast(lst))
print("Python min: ", min(lst))
