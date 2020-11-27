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

nums = [deus for deus in range(1000)]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def comper_var(nums):
    ind_arr = [i for i, deus in enumerate(nums) if deus % 2 == 0]
    return ind_arr


print(
    timeit.timeit(
        "func_1(nums)",
        setup="from __main__ import func_1, nums",
        number=1000))
print(timeit.timeit("comper_var(nums)",
                    setup="from __main__ import comper_var,nums",
                    number=1000))


""" Начальный массив сгенерирован выражением
Время выполнения  func_1 : 0.1627264
Время выполнения  func_2 : 0.1103990
Вариант 2 enumerate для индекса элемента и самого элемента( получения индекса)
Генераторное выражение , которое отрабатывает быстрее  конструкции цикла for """
