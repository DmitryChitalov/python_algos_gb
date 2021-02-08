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

from timeit import timeit
from random import sample


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return list(idx for idx, el in enumerate(nums) if el % 2 == 0)


def func_3(nums):
    new_arr = []
    for i, num in enumerate(nums):
        if num % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_4(nums):
    return [idx for idx, el in enumerate(nums) if el % 2 == 0]


randomlist = sample(range(0, 1000000), 10000)

print("Замеры двух функций на случайном массиве из 10, 100 и 1000 элементов")

for arr_len in [10, 100, 1000]:
    randomlist = sample(range(0, 1000000), arr_len)
    print(f"func_1, {arr_len} элементов:", end=' ')
    print(timeit("func_1(randomlist)", number=10000, globals=globals()))

for arr_len in [10, 100, 1000]:
    randomlist = sample(range(0, 1000000), arr_len)
    print(f"func_2, {arr_len} элементов:", end=' ')
    print(timeit("func_2(randomlist)", number=10000, globals=globals()))

"""
Замеры двух функций на случайном массиве из 10, 100 и 1000 элементов
func_1, 10 элементов: 0.015154500000000008
func_1, 100 элементов: 0.2548268
func_1, 1000 элементов: 2.4395753
func_2, 10 элементов: 0.03149859999999993
func_2, 100 элементов: 0.15629420000000005
func_2, 1000 элементов: 1.5674729999999997

func2 иногда проигрывает на коротких списках, но с ростом длины списка 
становится видно, что она работает быстрее.
Вместо цикла и .append используется встроенная функции list и list comprehension.
Сложность алогоритма не меняется, остается O(n), но работает быстрее за счет
использования встроенных функций.
"""
