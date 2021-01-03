"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
from timeit import timeit


def common_dict_creation():
    return dict(zip([i for i in range(10000)], [i for i in range(10000)]))


def ordered_dict_creation():
    return OrderedDict(zip([i for i in range(10000)], [i for i in range(10000)]))


def pop_items(raw_dict):
    while len(raw_dict):
        raw_dict.popitem()


def copy_dict(raw_dict):
    result = raw_dict.copy()


def get_values(raw_dict):
    raw_dict.values()


def get_keys(raw_dict):
    raw_dict.keys()


def run_dict(raw_dict):
    for i in raw_dict:
        raw_dict[i]


common_dict = common_dict_creation()
ordered_dict = ordered_dict_creation()

for func in ['common_dict_creation', 'ordered_dict_creation']:
    print(f'{func}: '
          f'{timeit(f"{func}()",f"from __main__ import {func} ",number=1000)}')

for elem in ['common_dict', 'ordered_dict']:
    print(f'-------{elem}-------')
    for func in ['pop_items', 'copy_dict', 'get_values', 'get_keys', 'run_dict']:
        print(f'{func}: {timeit(f"{func}({elem})", f"from __main__ import {func}, {elem}", number=100000)}')

"""
common_dict_creation: 1.2417648000000001
ordered_dict_creation: 1.8964139
-------common_dict-------
pop_items: 0.011300599999999772
copy_dict: 0.011288299999999918
get_values: 0.01184689999999966
get_keys: 0.012025599999999859
run_dict: 0.019838299999999975
-------ordered_dict-------
pop_items: 0.017329400000000383
copy_dict: 0.01642179999999982
get_values: 0.012170999999999932
get_keys: 0.012167599999999723
run_dict: 0.012591499999999645

Как видно из замеров к коду, который приведен выше:
1. OrderedDict создается немного дольше стандартного словаря;
2. Операции popitem() и copy() для OrderedDict происходят также немного дольше;
3. Проход в цикле по OrderedDict c получением значения соотвествующего ключу происходит быстрее, скорее всего 
за счет того что он упорядоченый.
"""