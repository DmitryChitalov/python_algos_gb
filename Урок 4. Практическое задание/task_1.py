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
from random import randint

my_list = [randint(1, 100) for _ in range(20)]

print(dict(enumerate(my_list)))

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr
setup = "from __main__ import func_1, my_list"

print(func_1(my_list))

setup1 = "from __main__ import func_2, my_list"
def func_2(nums):
    new_arr = [ind for ind, x in enumerate(nums) if x % 2 == 0]
    return new_arr

print(func_2(my_list))

print(timeit("func_1(my_list)", setup=setup))
print(timeit("func_2(my_list)", setup= setup1))


""" Аналитика. 
В программе я заменил консрукцию for - append на генератор и enumerate. Генератор работет быстрее, что и подтверждается тестами 
2.3177980959999998 - время работы 1 функции
1.908051875 - время работы 2 функции
"""