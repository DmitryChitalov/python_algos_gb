"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

"""
Кэш не дает заметного прироста производительности, как и использование бинарных операций вместо арифметических. 
Самый значительный прирост дало создание массива через механизм list comprehension 
"""

from timeit import timeit
from random import randint

num_100 = [randint(1, 9), randint(0, 9), randint(0, 9)]
num_1000 = [randint(1, 9), randint(0, 9), randint(0, 9), randint(0, 9)]
num_10000000 = [randint(1, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9),
                randint(0, 9)]

odd_cache = {1, 3, 5, 7, 9}
even_cache = {0, 2, 4, 6, 8}


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = list(filter(lambda x: (x % 2 == 0), nums))
    return new_arr


def func_3(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] in even_cache:
            new_arr.append(i)
    return new_arr

def func_4(nums):
    new_arr = [x for x in nums if x & 1 == 0]
    return new_arr

def func_5(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] & 1 == 0:
            new_arr.append(i)
    return new_arr

def func_6(nums):
    new_arr = []
    gen_exp = (x for x in nums if x & 1 == 0)
    for i in gen_exp:
        new_arr.append(i)
    return new_arr

print(num_10000000)
print(
    timeit(
        "func_1(num_100)",
        setup='from __main__ import func_1, num_100',
        number=10000))
print(
    timeit(
        "func_1(num_1000)",
        setup='from __main__ import func_1, num_1000',
        number=10000))
print(
    timeit(
        "func_1(num_10000000)",
        setup='from __main__ import func_1, num_10000000',
        number=10000))
print(
    timeit(
        "func_2(num_10000000)",
        setup='from __main__ import func_2, num_10000000',
        number=10000))
print(
    timeit(
        "func_3(num_10000000)",
        setup='from __main__ import func_3, num_10000000',
        number=10000))
print(
    timeit(
        "func_4(num_10000000)",
        setup='from __main__ import func_4, num_10000000',
        number=10000))
print(
    timeit(
        "func_5(num_10000000)",
        setup='from __main__ import func_5, num_10000000',
        number=10000))
print(
    timeit(
        "func_6(num_10000000)",
        setup='from __main__ import func_6, num_10000000',
        number=10000))
