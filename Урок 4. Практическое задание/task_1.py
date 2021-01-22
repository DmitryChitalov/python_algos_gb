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

nums = [i for i in range(20000)]



def func_2(nums):
    my_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return my_arr

print(timeit("func_1(nums)", setup="from __main__ import func_1, nums", number=1000))   # 2.196138555 def func_1()
print(timeit("func_2(nums)", setup="from __main__ import func_2, nums", number=1000)) # 1.757450167 def func_2()

# Функция func_2() содержит генераторное выражение, сравнивания две функции, видно, что функция func_2 работает быстрее, 
# при одних и тех же условиях, следовательно генераторное выражение работает быстрее цикла for in.