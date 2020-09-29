"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from timeit import timeit
from collections import OrderedDict


MY_DICT = {one: one for one in range(1000)}
MY_ODICT = OrderedDict(MY_DICT)


def fill_dict():
    my_dict = {}
    for numb in range(1000):
        my_dict[numb] = numb


def get_dict(new_dict):
    for idx in range(len(new_dict)):
        new_dict[idx]


def pop_dict(new_dict):
    length = len(new_dict)
    for idx in range(length):
        new_dict.pop(idx)


def fill_odict():
    my_odict = OrderedDict()
    for numb in range(1000):
        my_odict[numb] = numb


def get_odict(new_odict):
    for idx in range(len(new_odict)):
        new_odict[idx]


def pop_odict(new_odict):
    length = len(new_odict)
    for idx in range(length):
        new_odict.pop(idx)


result_fill_dict = timeit("fill_dict()", "from __main__ import fill_dict", number=10000)
result_fill_odict = timeit("fill_odict()", "from __main__ import fill_odict", number=10000)

result_get_dict = timeit("get_dict(MY_DICT)", "from __main__ import get_dict, MY_DICT", number=10000)
result_get_odict = timeit("get_odict(MY_ODICT)", "from __main__ import get_odict, MY_ODICT", number=10000)

result_pop_dict = timeit("pop_dict(MY_DICT)", "from __main__ import pop_dict, MY_DICT", number=1000000)
result_pop_odict = timeit("pop_odict(MY_ODICT)", "from __main__ import pop_odict, MY_ODICT", number=1000000)

print(f'Результат выполнения fill_dict(): \t{result_fill_dict}')
print(f'Результат выполнения fill_odict(): \t{result_fill_odict}')
print()
print(f'Результат выполнения get_dict(): \t{result_get_dict}')
print(f'Результат выполнения get_odict(): \t{result_get_odict}')
print()
print(f'Результат выполнения pop_dict(): \t{result_pop_dict}')
print(f'Результат выполнения pop_odict(): \t{result_pop_odict}')

"""
Результат выполнения fill_dict():       0.45076696699999996
Результат выполнения fill_odict():      0.738773321         -> Заполнение OrderedDict происходит на 63% медленнее, чем словаря.

Результат выполнения get_dict():        0.39550392700000003
Результат выполнения get_odict():       0.4065114049999998  -> Получение элементов из OrderedDict происходит на 3% медленнее, чем из словаря.
                                                               Различием времени в 3% можно пренебречь.
Результат выполнения pop_dict():        0.24129999200000007
Результат выполнения pop_odict():       0.2477760670000002  -> Получение элементов с удалением из OrderedDict происходит на 3% медленнее, чем из словаря.
                                                               Различием времени в 3% можно пренебречь.
"""
