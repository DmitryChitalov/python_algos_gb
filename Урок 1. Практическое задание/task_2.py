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


def find_min_in_list_quad(list_arg):
    length = len(list_arg)
    min_el = list_arg[0]
    for id1 in range(length):
        is_min = True
        for id2 in range(length):
            if list_arg[id1] > list_arg[id2]:
                is_min = False
                break
        if is_min:
            min_el = list_arg[id1]
    return min_el


def find_min_in_list_line(list_arg):
    min_el = list_arg[0]
    for id in range(1, len(list_arg)):
        if list_arg[id] < min_el:
            min_el = list_arg[id]
    return min_el


my_list = [random.randint(0, 1000) for _ in range(100)]

print(my_list)
print("Поиск минимального сложностью О(n**2) :", find_min_in_list_quad(my_list))
print("Поиск минимального сложностью О(n) :", find_min_in_list_line(my_list))
