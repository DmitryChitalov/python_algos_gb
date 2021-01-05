"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
from timeit import timeit


def test_get(dict):
    for _ in range(len(dict) - 1):
        dict.get(_)


def test_keys(dict):
    for _ in dict.keys():
        dict[_] += _ * 100
        return


def test_items(dict):
    for i, j in dict.items():
        return


def test_sort(dict):
    return {_: dict[_] for _ in sorted(dict)}


def test_go(dict):
    for _ in dict:
        dict[_]


regular_dict = {x: x for x in range(10000)}
ordered_dict = OrderedDict(regular_dict)

test_od_get = timeit('test_get(ordered_dict)',
                     'from __main__ import test_get, ordered_dict',
                     number=10000)
test_rd_get = timeit('test_get(regular_dict)',
                     'from __main__ import test_get, regular_dict',
                     number=10000)
print(f'{test_od_get}'
      f'\n{test_rd_get}'
      f'\nOrderedDict/Обычный в {test_od_get/test_rd_get:0.2f} раз\n')

test_od_keys = timeit('test_keys(ordered_dict)',
                      'from __main__ import test_keys, ordered_dict',
                      number=100000)
test_rd_keys = timeit('test_keys(regular_dict)',
                      'from __main__ import test_keys, regular_dict',
                      number=100000)
print(f'{test_od_keys}'
      f'\n{test_rd_keys}'
      f'\nOrderedDict/Обычный в {test_od_keys/test_rd_keys:0.2f} раз\n')

test_od_items = timeit('test_items(ordered_dict)',
                       'from __main__ import test_items, ordered_dict',
                       number=100000)
test_rd_items = timeit('test_items(regular_dict)',
                       'from __main__ import test_items, regular_dict',
                       number=100000)
print(f'{test_od_items}'
      f'\n{test_rd_items}'
      f'\nOrderedDict/Обычный в {test_od_items/test_rd_items:0.2f} раз\n')

test_od_sort = timeit('test_sort(ordered_dict)',
                      'from __main__ import test_sort, ordered_dict',
                      number=10000)
test_rd_sort = timeit('test_sort(regular_dict)',
                      'from __main__ import test_sort, regular_dict',
                      number=10000)
print(f'{test_od_sort}'
      f'\n{test_rd_sort}'
      f'\nOrderedDict/Обычный в {test_od_sort/test_rd_sort:0.2f} раз\n')

test_od_go = timeit('test_go(ordered_dict)',
                      'from __main__ import test_go, ordered_dict',
                      number=10000)
test_rd_go = timeit('test_go(regular_dict)',
                      'from __main__ import test_go, regular_dict',
                      number=10000)
print(f'{test_od_go}'
      f'\n{test_rd_go}'
      f'\nOrderedDict/Обычный в {test_od_go/test_rd_go:0.2f} раз')

"""
Результат:
11.325120432999999
10.984602483000002
OrderedDict/Обычный в 1.03 раз

0.04204235199999928
0.033179411999999076
OrderedDict/Обычный в 1.27 раз

0.03111271299999885
0.02681038100000066
OrderedDict/Обычный в 1.16 раз

10.175819788000002
8.437680628999999
OrderedDict/Обычный в 1.21 раз

5.103721307000001
3.8119321220000018
OrderedDict/Обычный в 1.34 раз

По итогу замеров получается что все медленнее... 
"""