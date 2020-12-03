"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from timeit import timeit
from collections import OrderedDict

def dict_keys():
    a = test_dict.keys()

def OrderedDict_keys():
    a = test_OrderedDict.keys()

def dict_values():
    b = test_dict.values()

def OrderedDict_values():
    b = test_OrderedDict.values()


def dict_items():
    b = test_dict.items()

def OrderedDict_items():
    b = test_OrderedDict.items()


def dict_get():
    b = test_dict.get(1)

def OrderedDict_get():
    b = test_OrderedDict.get(1)


col = 1000000

test_dict = {str(i): i for i in range(int(col / 10))}
test_OrderedDict = OrderedDict(test_dict)

print(
    timeit(
        'dict_keys()',
        setup='from __main__ import dict_keys',
        number=col))

print(
    timeit(
        'OrderedDict_keys()',
        setup='from __main__ import OrderedDict_keys',
        number=col))

print(
    timeit(
        'dict_values()',
        setup='from __main__ import dict_values',
        number=col))

print(
    timeit(
        'OrderedDict_values()',
        setup='from __main__ import OrderedDict_values',
        number=col))

print(
    timeit(
        'dict_items()',
        setup='from __main__ import dict_items',
        number=col))

print(
    timeit(
        'OrderedDict_items()',
        setup='from __main__ import OrderedDict_items',
        number=col))

print(
    timeit(
        'dict_get()',
        setup='from __main__ import dict_get',
        number=col))

print(
    timeit(
        'OrderedDict_get()',
        setup='from __main__ import OrderedDict_get',
        number=col))

"""
Выводы: OrderedDict и Dict близки по своим скоростным параметрам. Незаметил явного лидера, при запуске несколько раз иногда меняются местами лидеры по разным методам
В частности OrderedDict быстре при возврате списка ключей, но медленее при возврате значений.
Получение списока кортежей быстрее у OrderedDict
А получение значения по ключу быстрее у обычного Dict


0.2748569
0.21802610000000006
0.18773799999999996
0.3274499999999999
0.3134652
0.21251050000000005
0.16645700000000008
0.2270219

0.18371500000000002
0.17058510000000005
0.2215359
0.20685109999999995
0.2698631
0.24936369999999997
0.16704699999999995
0.20068660000000005
"""
