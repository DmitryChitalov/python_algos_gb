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

rand_list = random.sample(range(1, 1001), 10)


# O(n^2):
def min_in_list(arg_list):
    min_el = arg_list[0]
    for i in arg_list:
        for j in arg_list:
            if j < i and j < min_el:
                min_el = j
    return min_el


# O(n):
def optimal_min_in_list(arg_list):
    min_el = arg_list[0]
    for el in arg_list:
        if el < min_el:
            min_el = el
    return min_el


print(f"Поиск минимальнго значения в списке: {rand_list}")
print(f"min_in_list: {min_in_list(rand_list)}")
print(f"opriman_min_in_list: {optimal_min_in_list(rand_list)}")
