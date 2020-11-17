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
n = (1, 2, 3, 4, 5, 6)


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]


print(f'Время исходного кода: {timeit.timeit("func_1(n)", setup="from __main__ import func_1, n", number=1000)}')
print('Для снижения скорости выполнения кода я воспользовалась генераторным выражением, тк он выполняется быстрее '
      'чем цикл')
print(f'Время измененного кода: {timeit.timeit("func_2(n)", setup="from __main__ import func_2, n", number=1000)}')
