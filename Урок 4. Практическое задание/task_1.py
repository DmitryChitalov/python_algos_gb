"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""

import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    return [i for i, el in enumerate(nums) if el % 2 == 0]

def dict_f1(n):
    dict_obj = dict()
    for i in range(n):
        dict_obj[i] = i
    return dict_obj

def dict_f2(n):
    return(i for i, j in n.items() if n.keys() % 4 != 0 )

# 1000
NUMS = [el for el in range(1000)]
n = {i: {j**2 % i for j in range(1, 1000)} for i in range(1, 100)}
print(
    timeit.timeit(
        "func_1(NUMS)",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "func_2(NUMS)",
        globals=globals(),
        number=1000))
print(
    timeit.timeit(
        "dict_f1",
        globals=globals(),
        number=100000))

print(
    timeit.timeit(
        "dict_f2",
        globals=globals(),
        number=100000))

# 10000
NUMS = [el for el in range(10000)]
n = {i: {j**2 % i for j in range(1, 10000)} for i in range(1, 100)}
print(
    timeit.timeit(
        "func_1(NUMS)",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "func_2(NUMS)",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "dict_f1",
        globals=globals(),
        number=100000))

print(
    timeit.timeit(
        "dict_f2",
        globals=globals(),
        number=100000))

# 100000
NUMS = [el for el in range(100000)]
n = {i: {j**2 % i for j in range(1, 100000)} for i in range(1, 100)}
print(
    timeit.timeit(
        "func_1(NUMS)",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "func_2(NUMS)",
        globals=globals(),
        number=1000))

print(
    timeit.timeit(
        "dict_f1",
        globals=globals(),
        number=1000000))

print(
    timeit.timeit(
        "dict_f2",
        globals=globals(),
        number=1000000))

"""
Замер времени:
---1000---
0.16842050000000003
0.12216520000000003
0.0033374999999999932
0.003080499999999986

---10000---
1.7433271000000001
1.2771898
0.003204899999999622
0.0030032000000002057

---100000---
22.853218599999998
16.928565
0.03406710000000146
0.031103999999999132

Использование enumirate() ускоряет работу функций, по моему, тк после генерации значений становятся пустыми, 
когда range() можно воспользоваться повторно
"""