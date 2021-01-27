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
    return [i for i, x in enumerate(nums) if not x % 2]


list = [i for i in range(100)]  # список из 100 элементов
print(timeit(stmt='func_1(list)', globals=globals()))  # 18.2287617 сек.
print(timeit(stmt='func_2(list)', globals=globals()))  # 10.306235500000003 сек.

# вариант c enumerate работает быстрее, так как в этом случае не нужно
# обращаться к элементу по индексу, вместо этого функция сама создаёт
# дополнительный счетчик
