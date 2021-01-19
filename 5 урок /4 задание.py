"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
import timeit
dict = {'apple': 4, 'banana': 3, 'orange': 2, 'pear': 1}
orderdict = OrderedDict({'apple': 4, 'banana': 3, 'orange': 2, 'pear': 1})
i = 10000000

def create_dict():
    dict = {}
    return
def create_orderdict():
    dict = OrderedDict()
    return
def get_dict_keys():
    dict.keys()
    return
def get_Orderdic_keys():
    orderdict.keys()
    return
def uppend_dict_keys():
    dict['peach'] = 5
    return
def uppend_orderdict_keys():
    orderdict['peach'] = 5
    return

print(f'create_dict - {timeit.timeit("create_dict()", setup="from __main__ import create_dict", number = i)}')
print(f'create_orderdict{timeit.timeit("create_orderdict()", setup="from __main__ import create_orderdict", number = i)}')
print(f'get_dict_keys - {timeit.timeit("get_dict_keys()", setup="from __main__ import get_dict_keys")}')
print(f'get_Orderdic_keys - {timeit.timeit("get_Orderdic_keys()", setup="from __main__ import get_Orderdic_keys")}')
print(f'uppend_dict_keys - {timeit.timeit("uppend_dict_keys()", setup="from __main__ import uppend_dict_keys")}')
print(f'uppend_orderdict_keys - {timeit.timeit("uppend_orderdict_keys()", setup="from __main__ import uppend_orderdict_keys")}')

# Исходя из тестов можно сделать вывод, что скорость выполнения команд примерно одинаковая