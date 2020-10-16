"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    return [el[0] for el in enumerate(nums) if not el[1] & 1]

def func_3(nums):
    return list(filter(lambda i: not nums[i] & 1, range(len(nums))))

nums = [i for i in range(1000)]
stmts = ('func_1', 'func_2', 'func_3')
for stmt in stmts:
    print(f'Алгоритм {stmt}:')
    print(timeit(f"{stmt}({nums})",
                 setup=f'from __main__ import {stmt}',
                    number=10000))

"""
Попытался решить задачу с помощью генераторного выражения и фильтрации,
т.к. читал, что генераторные выражения - это быстрейший способ работы со
списками, а фильтрация - встроенная функция Python. Однако существенного
прироста скорости эти способы не дали.
Также делал попытки решить с помощью map и lambda-функции, но это только
замедлило алгоритм.
В целом заметно оптимизировать алгоритм мне не удалось.
"""