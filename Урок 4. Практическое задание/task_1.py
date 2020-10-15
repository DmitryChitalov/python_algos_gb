"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

from timeit import timeit, repeat


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

my_num = [i for i in range(0, 100)]

print(func_1(my_num))
print(timeit('func_1(my_num)', setup="from __main__ import func_1; from __main__ import my_num ", number=10000))
# 6.240210713000124
print(repeat('func_1(my_num)', setup="from __main__ import func_1; from __main__ import my_num ", repeat=5, number=10000))
# [6.305441824999434, 6.273107855999115, 6.3074074249998375, 6.246076170002198, 6.229232941001101]
def func_2(nums):
    return [i for i in range(len(nums)) if nums[i] % 2 == 0]

print(func_2(my_num))
print(timeit('func_2(my_num)', setup="from __main__ import func_2; from __main__ import my_num ", number=10000))
# 5.495959821000724
print(repeat('func_2(my_num)', setup="from __main__ import func_2; from __main__ import my_num ", repeat=5, number=10000))
# [5.507961403000081, 5.511396752001019, 5.505242994000582, 5.507853768001951, 5.658421536001697]
"""
Генераторы и генераторные выражения выполняются быстрее нежели сопоставимые функции на циклах.
Число циклов сократил до 10 000
"""