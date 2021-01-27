"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from timeit import Timer

from timeit import timeit


def original_func(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def gen_funk(nums):
    new_nums = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_nums


def enum_func(nums):
    new_nums = [i for i, el in enumerate(nums) if nums[i] % 2 == 0]
    return new_nums


array = [i for i in range(10000)]

print('\n1 вариация исполнения кода: t1')
print(
    timeit(
        "original_func(array)",
        globals=globals(),
        number=1000))
print('\n2 вариация исполнения кода: t2')
print(
    timeit(
        "gen_funk(array)",
        globals=globals(),
        number=1000))
print('\n3 вариация исполнения кода: t3')
print(
    timeit(
        "enum_func(array)",
        globals=globals(),
        number=1000))

"""
на больших объемах - генератор (t2)
работает быстрее остальных функций
enumerate (t3) - идет на 2ом месте,
оригинальная функция (t1) самая медлянная
"""
