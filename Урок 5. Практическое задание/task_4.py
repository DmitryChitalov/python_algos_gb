"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
import timeit

from collections import OrderedDict

test_dict = {str(i):i for i in range(10000)}
test_dict1 = {str(i):i for i in range(20000, 30000)}
test_o_dict = OrderedDict(test_dict)
test_o_dict1 = OrderedDict(test_dict1)

# получение значения ключа

def dict_get(test_dict):
    for i in range(len(test_dict)):
        test_dict.get(str(i))

def o_dict_get(test_o_dict):
    for i in range(len(test_o_dict)):
        test_o_dict.get(str(i))

print(f'Получение значения ключа (словарь) - {timeit.timeit("dict_get(test_dict)", setup="from __main__ import dict_get, test_dict", number=1000)}')
print(f'Получение значения ключа (OrderedDict) - {timeit.timeit("o_dict_get(test_o_dict)", setup="from __main__ import o_dict_get, test_o_dict", number=1000)}')

# удаление

def dict_popitems(test_dict):
    for i in range(len(test_dict)):
       el =  test_dict.popitem()

def o_dict_popitems(test_o_dict):
    for i in range(len(test_o_dict)):
        el = test_o_dict.popitem()

print(f'Удаление (словарь) - {timeit.timeit("dict_popitems(test_dict)", setup="from __main__ import dict_popitems, test_dict", number=1000)}')
print(f'Удаление (OrderedDict) - {timeit.timeit("o_dict_popitems(test_o_dict)", setup="from __main__ import o_dict_popitems, test_o_dict", number=1000)}')

# обновление

def dict_update(test_dict, test_dict1):
    test_dict.update(test_dict1)

def o_dict_update(test_o_dict, test_o_dict1):
    test_o_dict.update(test_o_dict1)

print(f'Обновление (словарь) - {timeit.timeit("dict_update(test_dict, test_dict1)", setup="from __main__ import dict_update, test_dict, test_dict1", number=1000)}')
print(f'Обновление (OrderedDict) - {timeit.timeit("o_dict_update(test_o_dict, test_o_dict1)", setup="from __main__ import o_dict_update, test_o_dict, test_o_dict1", number=1000)}')

"""
OrderedDict на операциях получения значений и удаления работает чуть хуже, 
а на операции обновления словоря значительно хуже стандартных словарей
"""