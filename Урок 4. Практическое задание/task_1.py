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


"""
2.	Во втором массиве сохранить индексы четных элементов первого массива.
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив
надо заполнить значениями 1, 4, 5, 6
(или 0, 3, 4, 5 - если индексация начинается с нуля),
т.к. именно в этих позициях первого массива стоят четные числа.
"""


def func_1(nums):
    """O(n) – линейная сложность"""
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    """O(n) – линейная сложность"""
    return [i for i, el in enumerate(nums) if el % 2 == 0]


# 1000
num_list = [el for el in range(1000)]

print(
    timeit.timeit(
        "func_1(num_list)",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "func_2(num_list)",
        globals=globals(),
        number=1000))


# 10000
NUMS = [el for el in range(10000)]

print(
    timeit.timeit(
        "func_1(num_list)",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "func_2(num_list)",
        globals=globals(),
        number=1000))

# 100000
num_list = [el for el in range(100000)]

print(
    timeit.timeit(
        "func_1(num_list)",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "func_2(num_list)",
        globals=globals(),
        number=1000))

"""
Результат:
---1000---
0.066784139
0.05436164199999999

---10000---
0.06450118499999999
0.05393159199999997

---100000---
6.746566669
6.005584626999999

Списковые включения отрабатывают быстрее, чем реализация через итераторы
"""
