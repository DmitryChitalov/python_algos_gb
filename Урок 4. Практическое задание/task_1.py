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
    for i in range(2, len(nums), 2):
       new_arr.append(i)
    return new_arr


setup_code = '''from __main__ import func_1
nums=range(2000)'''

setup_code2 = '''from __main__ import func_2
nums=range(2000)'''

print(timeit('func_1(nums)', setup=setup_code, number=1000))
print(timeit('func_2(nums)', setup=setup_code2, number=1000))
