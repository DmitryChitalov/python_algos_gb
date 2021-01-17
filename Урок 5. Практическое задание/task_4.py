"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import Timer


def dict_creation():
    data = {
        'mercedes': 4,
        'audi': 2,
        'bmw': 1,
        'lexus': 5,
        'toyota': 3,
        'ford': 7,
        'chevrolet': 9,
        'citroen': 10,
        'jaguar': 6,
        'honda': 8
    }
    return data


def ord_dict_creation():
    data = OrderedDict({
        'mercedes': 4,
        'audi': 2,
        'bmw': 1,
        'lexus': 5,
        'toyota': 3,
        'ford': 7,
        'chevrolet': 9,
        'citroen': 10,
        'jaguar': 6,
        'honda': 8
    })
    return data


first_dict = dict_creation()
second_dict = ord_dict_creation()

time_1 = Timer('dict_creation()', 'from __main__ import dict_creation')
print(f'1st Program execution time: {round(time_1.timeit(number=100000), 7)} milliseconds')

time_2 = Timer('ord_dict_creation()', 'from __main__ import ord_dict_creation')
print(f'1st Program execution time: {round(time_2.timeit(number=100000), 7)} milliseconds')

'''
Операция создания обычного словаря происходит быстрее создания словаря OrderedDict
'''


def sorted_keys_dict(dictionary):
    return sorted(dictionary.items())


def sorted_keys_ord_dict(dictionary):
    return sorted(dictionary.items())


time_3 = Timer('sorted_keys_dict(first_dict)', 'from __main__ import first_dict, sorted_keys_dict')
print(f'2nd Program execution time: {round(time_3.timeit(number=100000), 7)} milliseconds')

time_4 = Timer('sorted_keys_ord_dict(second_dict)', 'from __main__ import second_dict, sorted_keys_ord_dict')
print(f'2nd Program execution time: {round(time_4.timeit(number=100000), 7)} milliseconds')

'''
Операция сотировки обычного словаря происходит чуть быстрее операции сортировки словаря OrderedDict
'''


def append_dict_array(dictionary, array=[]):
    for key, value in dictionary.items():
        array.append(key)
    return array


def append_ord_dict_array(dictionary, array=[]):
    for key, value in dictionary.items():
        array.append(key)
    return array


time_5 = Timer('append_dict_array(first_dict)', 'from __main__ import first_dict, append_dict_array')
print(f'3rd Program execution time: {round(time_5.timeit(number=10000), 7)} milliseconds')

time_6 = Timer('append_ord_dict_array(second_dict)', 'from __main__ import second_dict, append_ord_dict_array')
print(f'3rd Program execution time: {round(time_6.timeit(number=10000), 7)} milliseconds')

'''
Операция добавления ключей обычного словаря в список происходит чуть быстрее аналогичной операции со словарем
OrderedDict
'''

'''
Вывод: словарь OrderedDict позволяет запоминать порядок вставки, однако сейчас это стало менее необходимым, когда класс
dict получил возможность делать то же самое (в Python 3.7). Вместе с тем операции добавления, извлечения, обновления
данных в обычном словаре происходят быстрее аналогичных операций в OrderedDict, что дает первому (dict) преимущество
над вторым (OrderedDict)'''