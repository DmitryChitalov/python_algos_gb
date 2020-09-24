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
    new_arr = []
    for el in nums:
        if not el % 2:
            new_arr.append(el)
    return new_arr


result_1 = timeit("func_1(range(10))", "from __main__ import func_1", number=100000)
result_2 = timeit("func_2(range(10))", "from __main__ import func_2", number=100000)
print(f'Результат выполнения func_1: {result_1}')
print(f'Результат выполнения func_2: {result_2}')

"""
После замены цикла с получением каждого элемента по индексу на цикл for in (более быстрый)
функция начала работать быстрее в 2 раза.
"""
