"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
import timeit

from collections import OrderedDict

dict_for_test = {str(i): i for i in range(1000)}

o_dict_for_test = OrderedDict(dict_for_test)


def filling_dict(num):
    a = dict()
    for i in range(num):
        a[str(i)] = i


def filling_o_dict(num):
    a = OrderedDict()
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


name_list = 'filling_dict filling_o_dict for_every_kv_dict for_every_kv_o_dict list_sorting_dict ' \
            'list_sorting_o_dict popitem_dict popitem_o_dict get_dict get_o_dict'.split()

num_time = 10000

for id, func_name in enumerate(name_list):
    if id % 2 == 0:
        print("*" * 30)
    if id == 0 or id == 1:
        print(
            f"{func_name} - {timeit.timeit(stmt=func_name + f'(1000)', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")
    else:
        if id % 2 == 0:
            print(
                f"{func_name} - {timeit.timeit(stmt=func_name + f'(dict_for_test)', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")
        else:
            print(
                f"{func_name} - {timeit.timeit(stmt=func_name + f'(o_dict_for_test)', setup=f'from __main__ import {func_name}', number=num_time, globals=globals())}")

'''
Результаты одинаковы примерно, но в основном OrderDict хуже. Делаем вывод в современных версиях он не нужен.
******************************
filling_dict - 5.405226
filling_o_dict - 6.545415599999999
******************************
for_every_kv_dict - 0.8516072000000001
for_every_kv_o_dict - 1.6285382999999989
******************************
list_sorting_dict - 2.220783599999999
list_sorting_o_dict - 2.9019852999999998
******************************
popitem_dict - 0.004606200000001337
popitem_o_dict - 0.00502739999999946
******************************
get_dict - 0.0041440000000001476
get_o_dict - 0.004411699999998575
'''
