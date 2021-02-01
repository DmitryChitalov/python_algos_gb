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


def min_quad(lst_target):
    if lst_target is None:
        return
    for i in range(len(lst_target)):
        for j in range(len(lst_target)):
            if lst_target[i] > lst_target[j]:
                break
            if j == len(lst_target)-1:
                return lst_target[i]


def min_lin(lst_target):
    if lst_target is None:
        return
    curr_min = lst_target[0]
    for i in range(1, len(lst_target)):
        if lst_target[i] < curr_min:
            curr_min = lst_target[i]
    return curr_min


for k in (50, 500, 1000, 5000, 1000):
    # Из 100000 чисел возьмем 'k' случайно выбранных
    # Всего 10 тыс. чисел
    lst = random.sample(range(-100000, 100000), k)

    print(min_quad(lst))
    print(min_lin(lst))
    print(min(lst))
