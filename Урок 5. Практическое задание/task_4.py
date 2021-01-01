"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
import random
from collections import OrderedDict
from timeit import timeit

def key_gen(len = 4):
    return "".join(random.choice("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") for i in  range(len))



def fill_dict_with_keys(keys):
    __new_dict = dict()
    for key in keys:
        __new_dict[key] = key_gen(7)
    return __new_dict

def fill_orderdict_with_keys(keys):
    __new_dict = OrderedDict()
    for key in keys:
        __new_dict[key] = key_gen(7)
    return __new_dict

def remove_with_pop(keys,removal_dict):
    for key in keys:
        removal_dict.popitem()

def get_elem(keys,getter_dict):
    for key in keys:
        getter_dict[key]

KEYS_FOR_DICT = [key_gen() for i in range(1000)]#500000 для удаления элементов
SHUFFLE_KEYS = KEYS_FOR_DICT.copy()
random.shuffle(SHUFFLE_KEYS)
FILLED_DICT = fill_dict_with_keys(KEYS_FOR_DICT)
FILLED_ORDER_DICT = fill_orderdict_with_keys(KEYS_FOR_DICT)

if __name__ == '__main__':
    #print(timeit('fill_dict_with_keys(KEYS_FOR_DICT)', 'from __main__ import fill_dict_with_keys,KEYS_FOR_DICT'))
    #print(timeit('fill_orderdict_with_keys(KEYS_FOR_DICT)', 'from __main__ import fill_orderdict_with_keys,KEYS_FOR_DICT'))
    #print('Копирование словаря')
    #print(timeit('FILLED_DICT.copy()', 'from __main__ import remove_with_pop,KEYS_FOR_DICT,FILLED_DICT'))
    #print(timeit('FILLED_ORDER_DICT.copy()', 'from __main__ import remove_with_pop,KEYS_FOR_DICT,FILLED_ORDER_DICT'))
    #print(timeit(stmt='FILLED_DICT.popitem()', setup='from __main__ import remove_with_pop,KEYS_FOR_DICT,FILLED_DICT',number = 450000))
    #print(timeit(stmt='FILLED_ORDER_DICT.popitem()', setup='from __main__ import remove_with_pop,KEYS_FOR_DICT,FILLED_ORDER_DICT',number = 450000))
    print(timeit('get_elem(SHUFFLE_KEYS,FILLED_DICT)', 'from __main__ import get_elem,SHUFFLE_KEYS,FILLED_DICT'))
    print(timeit('get_elem(SHUFFLE_KEYS,FILLED_ORDER_DICT)', 'from __main__ import get_elem,SHUFFLE_KEYS,FILLED_ORDER_DICT'))
'''
Заполнение словаря
178.0026055
Заполнение ордер словаря
174.25447920000002

Чтенение рандомного ключа
dict
34.6193167
orderdict
34.9966792

Копирование словарей
копирование обычного словаря
0.26174379999999997
копирование orderdict
3.3432766

Очистка словарей через метод popitem

словарь
0.046608999999999234
orderdict
0.09224989999999966


Заполнение словарей и чтение радномного ключа происходит примерно за одинаковое время, в то время как копирование и изъятие элементов происходит 
медленнее
'''
