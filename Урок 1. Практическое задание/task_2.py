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

length = 10
my_list = random.sample(range(100), length)
print(my_list)

# Алгоритм 1 - сложность O(n^2)

def check_min1(lst):
    for i in lst:
        found_smaller = False
        for j in lst:
            if j < i:
                found_smaller = True
                break
        if found_smaller is not True:
            return i


# Алгоритм 2 - сложность O(n)


def check_min2(lst):
    res = lst[0]
    for i in range(1, length):
        if lst[i] < res:
            res = lst[i]
    return res


# Алгоритм 3 - сложность O(n)


def check_min3(lst):
    min1 = min(lst)
    return min1


print(check_min1(my_list))
print(check_min2(my_list))
print(check_min3(my_list))
