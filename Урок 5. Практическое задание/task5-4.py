"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

import timeit

from collections import OrderedDict as o_dict

dict_for_test_one = {str(i):i for i in range(1000)}
dict_for_test_two = {str(i):i for i in range(100000, 101000)}

o_dict_for_test_one = o_dict(dict_for_test_one)

o_dict_for_test_two = o_dict(dict_for_test_two)

def filling_dict(num):
    a = dict()
    for i in range(num):
        a[str(i)]=i


def filling_o_dict(num):
    a = o_dict()
    for i in range(num):
        a[str(i)] = i

def for_every_kv_dict(filled_dict):
    for key, value in filled_dict.items():
        a = key
        b = value

def for_every_kv_o_dict(filled_dict):
    for key, value in filled_dict.items():
        a = key
        b = value

def list_sorting_dict(filled_dict):
    a = sorted(filled_dict.items(), key=lambda item: item[1])

def list_sorting_o_dict(filled_dict):
    a = sorted(filled_dict.items(), key=lambda item: item[1])

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

def update_dict(filled_dict_one, filled_dict_two):
    filled_dict_one.update(filled_dict_two)

def update_o_dict(filled_dict_one, filled_dict_two):
    filled_dict_one.update(filled_dict_two)





name_list = 'filling_dict filling_o_dict for_every_kv_dict for_every_kv_o_dict list_sorting_dict list_sorting_o_dict popitem_dict popitem_o_dict get_dict get_o_dict update_dict update_o_dict'.split()


num_time = 10000

for id, func_name in enumerate(name_list):
    if id%2==0:
        print()
    if id == 0 or id == 1:
        print(f"{func_name} -\t{timeit.timeit(stmt=func_name + f'(1000)', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")
    elif id == 10 :
        print(f"{func_name} -\t{timeit.timeit(stmt=func_name + f'(dict_for_test_one, dict_for_test_two)', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")
    elif id == 11:
        print(f"{func_name} -\t{timeit.timeit(stmt=func_name + f'(o_dict_for_test_one, o_dict_for_test_two)', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")
    else:
        if id%2==0:
            print(f"{func_name} -\t{timeit.timeit(stmt=func_name + f'(dict_for_test_one)', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")
        else:
            print(f"{func_name} -\t{timeit.timeit(stmt=func_name + f'(o_dict_for_test_one)', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")



'''
filling_dict -	6.6361854
filling_o_dict -	7.371119800000001
Разница небольшая

for_every_kv_dict -	0.7411387000000005
for_every_kv_o_dict -	1.2060062999999985
OrderedDict в 2 раза медленнее

list_sorting_dict -	2.0904188999999995
list_sorting_o_dict -	2.5540935000000005
почти одинаково

popitem_dict -	0.005467100000000613
popitem_o_dict -	0.005551600000000434
почти одинаково

get_dict -	0.005176699999999812
get_o_dict -	0.005711099999999192
почти одинаково

update_dict -	0.3655494000000026
update_o_dict -	1.3387697000000003
OrderedDict в 3,5 медленнее

'''
