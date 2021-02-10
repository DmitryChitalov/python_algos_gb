"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from timeit import timeit
from collections import OrderedDict as ordereddict

dict_for_test_1 = {str(i): i for i in range(1000)}
dict_for_test_2 = {str(i): i for i in range(100000, 101000)}
o_dict_for_test_1 = ordereddict(dict_for_test_1)
o_dict_for_test_2 = ordereddict(dict_for_test_2)


def clear_dict(filled_dict):
    filled_dict.clear()


def clear_o_dict(filled_dict):
    filled_dict.clear()


def filling_dict(n):
    a = dict()
    for i in range(n):
        a[str(i)] = i


def filling_o_dict(n):
    a = ordereddict()
    for i in range(n):
        a[str(i)] = i


def for_every_kv_dict(filled_dict):
    for k, v in filled_dict.items():
        a = k
        b = v


def for_every_kv_o_dict(filled_dict):
    for k, v in filled_dict.items():
        a = k
        b = v


def list_sorting_dict(filled_dict):
    a = sorted(filled_dict.items(), key=lambda el: el[1])


def list_sorting_o_dict(filled_dict):
    a = sorted(filled_dict.items(), key=lambda el: el[1])


def popitem_dict(filled_dict):
    for i in range(len(filled_dict)):
        a = filled_dict.popitem()


def popitem_o_dict(filled_dict):
    for i in range(len(filled_dict)):
        a = filled_dict.popitem()


def get_dict(filled_dict):
    for i in range(len(filled_dict)):
        filled_dict.get(str(i))


def get_o_dict(filled_dict):
    for i in range(len(filled_dict)):
        filled_dict.get(str(i))


def update_dict(filled_dict_1, filled_dict_2):
    filled_dict_1.update(filled_dict_2)


def update_o_dict(filled_dict_1, filled_dict_2):
    filled_dict_1.update(filled_dict_2)


name_list = 'filling_dict filling_o_dict clear_dict clear_o_dict for_every_kv_dict ' \
            'for_every_kv_o_dict list_sorting_dict list_sorting_o_dict ' \
            'popitem_dict popitem_o_dict get_dict get_o_dict update_dict update_o_dict'.split()
num_time = 10000

for id, func_name in enumerate(name_list):
    if id % 2 == 0:
        print()
    if id == 0 or id == 1:
        print(
            f"{func_name} -\t{timeit(stmt=func_name + f'(1000)', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")
    elif id == 12:
        print(
            f"{func_name} -\t{timeit(stmt=func_name + f'(dict_for_test_1, dict_for_test_2)', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")
    elif id == 13:
        print(
            f"{func_name} -\t{timeit(stmt=func_name + f'(o_dict_for_test_1, o_dict_for_test_2)', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")
    else:
        if id % 2 == 0:
            print(
                f"{func_name} -\t{timeit(stmt=func_name + f'(dict_for_test_1)', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")
        else:
            print(
                f"{func_name} -\t{timeit(stmt=func_name + f'(o_dict_for_test_1)', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")

'''
Результаты везде получились +- одинаковые,
но ordereddict чуть хуже оптимизирован (особенно касательно функции update())

filling_dict -	3.572299244999158
filling_o_dict -	4.074209850999978

clear_dict -	0.0012925620012538275
clear_o_dict -	0.0014128549992165063

for_every_kv_dict -	0.002758590000667027
for_every_kv_o_dict -	0.0028598040007636882

list_sorting_dict -	0.006359962999340496
list_sorting_o_dict -	0.006417430999135831

popitem_dict -	0.004040210000312072
popitem_o_dict -	0.004185038998912205

get_dict -	0.0040625639994686935
get_o_dict -	0.004117409000173211

update_dict -	0.17732408799929544
update_o_dict -	0.7606308149988763
'''