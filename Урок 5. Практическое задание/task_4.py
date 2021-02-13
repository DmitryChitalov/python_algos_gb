"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from timeit import timeit

from collections import OrderedDict

test_dict = {a: "AAAAA" + str(a) for a in range(10000)}

test_ordered_dict = OrderedDict(test_dict)


def dict_append(num):
    var = dict()
    for i in range(num):
        var[i] = "AAA"


def ordered_dict_append(num):
    var = OrderedDict()
    for i in range(num):
        var[i] = "AAA"


def dict_pop(array):
    array.popitem()


def dict_get(array):
    for i in range(len(array)):
        array.get(i)


print(
    f'Dict append : {timeit(stmt="dict_append(1000)",number=10000,globals=globals())} sec'
)
print(
    f'Ordered dict append : {timeit(stmt="ordered_dict_append(1000)",number=10000,globals=globals())} sec'
)
print(
    f'Dict pop : {timeit(stmt="dict_pop(test_dict)",number=10000,globals=globals())} sec'
)
print(
    f'Ordered dict pop : {timeit(stmt="dict_pop(test_ordered_dict)",number=10000,globals=globals())} sec'
)
print(
    f'Dict get : {timeit(stmt="dict_get(test_dict)",number=10000,globals=globals())} sec'
)
print(
    f'Ordered dict get : {timeit(stmt="dict_get(test_ordered_dict)",number=10000,globals=globals())} sec'
)

# Начиная с версии 3.6 использовать OrderedDict смысла нет, т.к. то же функционал есть и в обычном словаре,
# при этом простой dict в некоторых операциях работает быстрее.
