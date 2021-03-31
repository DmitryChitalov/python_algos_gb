# encoding: utf-8
from __future__ import print_function
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
from random import randint, seed


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [
        i
        for i, n in enumerate(nums)
        if n % 2 == 0
    ]


# обеспечим повторяемость при генерации массива
seed(1)
arr100 = [randint(1, 100) for i in range(100)]
arr1000000 = [randint(1, 100) for i in range(1000000)]

arr = arr100
N = 100000

print("func_1(<100>), 100 000")
print(timeit("func_1(arr)", "from __main__ import func_1, arr", number=N))

print("func_2(<100>), 100 000")
print(timeit("func_2(arr)", "from __main__ import func_2, arr", number=N))

arr = arr1000000
N = 10

print("func_1(<1 000 000>), 100")
print(timeit("func_1(arr)", "from __main__ import func_1, arr", number=N))

print("func_2(<1 000 000>), 100")
print(timeit("func_2(arr)", "from __main__ import func_2, arr", number=N))


# python --version
# Python 3.9.2
# результаты для python3
# ---
# func_1(<100>), 100 000
# 0.8526363730197772
# func_2(<100>), 100 000
# 0.7195342039922252
# func_1(<1 000 000>), 100
# 0.9767448229831643
# func_2(<1 000 000>), 100
# 0.8591583400266245
# ---

# python2 --version
# Python 2.7.18

# результаты для python2
# ---
# func_1(<100>), 100 000
# 0.980357170105
# func_2(<100>), 100 000
# 0.845843076706
# func_1(<1 000 000>), 100
# 2.45475101471
# func_2(<1 000 000>), 100
# 1.35260820389
# ---
# Остается поблагодарить разработчиков python за отличную
# оптимизацию виртуальной машины, python3 стал вообще
# быстрее, чем python2, при этом циклы for для больших
# массивов стали работать практически
# со скоростью list comprehension, в то время как в python2
# разница для больших списков была почти двукратной
