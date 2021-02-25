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

from random import randint

# Вариант 1  O(n^2) - квадратичная
def list_min_v1(list):
    for i in list:
        is_min = True
        for j in list:
            if i > j:
                is_min = False
        if is_min:
            return i

# Вариант 2  O(n) - линейная
def list_min_v2(list):
    min_value = list[0]
    for i in list:
        if i < min_value:
            min_value = i
    return min_value


list1 = [randint(0, 100) for i in range(20)]
print(list1)
print(list_min_v1(list1))
print(list_min_v2(list1))