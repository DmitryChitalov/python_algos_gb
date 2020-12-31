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

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [el for el, elem in enumerate(nums) if el % 2 == 0]


def func_3(nums):
    for elem in range(len(nums)):
        if nums[elem] % 2 == 0:
            yield elem


print(timeit('func_1(nums)', 'from __main__ import func_1, nums'))
print(timeit('func_2(nums)', 'from __main__ import func_2, nums'))
print(timeit('func_3(nums)', 'from __main__ import func_3, nums'))


"""
Результат при 1 000 000 запусков:

1.1189160999999999
0.9828839
0.16879460000000002

Вывод. Генератор выполняется быстрее, чем генераторное выражение,
а генераторное выражение быстрее чем цикл.
"""