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
    return [i for i, val in enumerate(nums) if val % 2 == 0]


if __name__ == '__main__':
    cycles = 10
    src_lst = [i for i in range(1000000)]

    # print(func_1(src_lst) == func_2(src_lst))

    # Time 0.452863638
    print(
        timeit(
            f'func_1(src_lst)',
            'from __main__ import func_1, src_lst',
            number=cycles)
        / cycles)

    # Time 0.35142758900000004
    print(
        timeit(
            f'func_2(src_lst)',
            'from __main__ import func_2, src_lst',
            number=cycles)
        / cycles)

    # Доработки: убрал получение по индексу, для создания нового использовал list comprehansion.
