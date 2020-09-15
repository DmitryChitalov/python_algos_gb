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


# algorithm_1

def bad_search(_list):
    _var = 0
    while True:
        if _var not in _list:
            _var += 1
        else:
            return _var


# algorithm_2

def good_search(_list):
    return min(_list)


work_list = [random.randint(1, 200) for x in range(1, 200)]

# check

print(f'Наименьшее значение в рандомном списке: {bad_search(work_list)}')
print(f'Наименьшее значение в рандомном списке: {good_search(work_list)}')
