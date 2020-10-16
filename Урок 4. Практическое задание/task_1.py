"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

import timeit
nums = [56, 56, 5657, 56423564]


def func_1(num):
    new_arr = []
    for i in range(len(num)):
        if num[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(num):
    new_arr = []
    for el in num:
        if el % 2 == 0:
            new_arr.append(el)
    return new_arr


print(timeit.timeit("func_1(nums)", setup="from __main__ import func_1, nums", number=1000))
print(timeit.timeit("func_2(nums)", setup="from __main__ import func_2, nums", number=1000))

"""
func_2 практически в два раза быстрее. в цикле for идет перебор самих элементов списка непосредственно. в следствии
чего нет взятия элемента по индексу чтобы выяснить четное или не четное число
"""