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

nums = list(range(1000))
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

def func_2(nums):
    new_arr = [x for x in nums if x % 2 == 0]

t1 = Timer("func_1(nums)", "from __main__ import func_1, nums")
print("list cicle ", t1.timeit(number=1000))

t2 = Timer("func_2(nums)", "from __main__ import func_2, nums")
print("list gen_statement ", t2.timeit(number=1000))

'''Я создал функцию, основанную на генераторном выражении, потому, что оно является встроенным, соответственно 
более оптимизированным'''
