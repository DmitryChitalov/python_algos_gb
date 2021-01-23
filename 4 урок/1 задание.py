"""
Задание 1.
Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива
Сделайте замеры времени выполнения кода с помощью модуля timeit
Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры
Добавьте аналитику: что вы сделали и почему
"""

from timeit import timeit, Timer

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if int(nums[i]) % 2 == 0:
            new_arr.append(i)
    return new_arr

t_1 = Timer('func_1("23456702020208")', 'from __main__ import func_1')
print(f'func_1: {t_1.timeit(number = 100000)} milliseconds')

def func_2(nums):
    new_arr = []
    for i in range(len(nums)):
        if int(nums[i]) in {2,4,6,8}:
            new_arr.append(i)
    return new_arr

t_2 = Timer('func_2("23456702020208")', 'from __main__ import func_2')
print(f'func_2: {t_2.timeit(number = 100000)} milliseconds')
# Мое решение работает немного быстрее только если подаются большие числа,
# так как сравнение происходит быстрее чем деление.


