"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import timeit



def dict_add(cyclces):
    test_dict = {}
    for i in range(cyclces):
        test_dict[i] = i


def ord_dict_add(cyclces):
    test_orderedDict = OrderedDict()
    for i in range(cyclces):
        test_orderedDict[i] = i


def dict_get(cyclces):
    test_dict = {}
    for _, _ in test_dict.items():
        pass


def ord_dict_get(cyclces):
    test_orderedDict = OrderedDict()
    for _, _ in test_orderedDict.items():
        pass


def dict_pop(cyclces):
    test_dict = {}
    for i in range(cyclces):
        test_dict[i] = i
    for i in range(cyclces):
        test_dict.popitem()


def ord_dict_pop(cyclces):
    test_orderedDict = OrderedDict()
    for i in range(cyclces):
        test_orderedDict[i] = i
    for i in range(cyclces):
        test_orderedDict.popitem()

funcs_dict = {'add': 'dict_add',
              'get': 'dict_get',
              'pop': 'dict_pop'}

funcs_ord_dict = {'add': 'ord_dict_add',
               'get': 'ord_dict_get',
               'pop': 'ord_dict_pop'}

setup = f"""from __main__ import {", ".join(funcs_dict.values())}, {", ".join(funcs_ord_dict.values())}"""

print(f'{"":>15}{"dict":>15}{"ordered dict":>15}')
for item in funcs_dict:
    dict_result = timeit(f'{funcs_dict[item]}(1000)', setup, number=10000)
    ord_dict_result = timeit(f'{funcs_ord_dict[item]}(1000)', setup, number=10000)
    print(f'{item:>15}{dict_result:>15.6f}{ord_dict_result:>15.6f}')


"""
              dict   ordered dict
add       0.648303       0.974937
get       0.002110       0.003003
pop       1.395424       2.372976

ordered dict работает чуть медленнее чем dict. Иногда стоит пожертвовать скоростью ради удобства 
"""