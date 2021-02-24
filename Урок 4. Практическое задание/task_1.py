"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание считается не принятым
"""

import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_1_fast(nums):
    return list(el for el in nums if not el % 2)


count = 10000
list1 = list(range(count))
print(timeit.repeat("func_1(list1)", globals=globals(), number=2000, repeat=3))
# [3.6538769, 3.5697413000000005, 3.4517485]
print(timeit.repeat("func_1_fast(list1)", globals=globals(), number=2000, repeat=3))
# [2.0572605999999993, 2.1885642, 2.159944099999999]
# судя по результатам - list comprehensions быстрее.
# repeat использовали для того, чтобы взять несколько результатов измерений
