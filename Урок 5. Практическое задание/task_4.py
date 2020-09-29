"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

import collections
import timeit


print('исходные словари')
test_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6}
print(test_dict)
test_ordered_dict = collections.OrderedDict(test_dict)
print(test_ordered_dict)
print()

print('тестируем нахождение значения по ключу')

def find_dict_value(key='C'):
    return test_dict[key]

print(f'dict: '
      f'{timeit.timeit("find_dict_value()", setup="from __main__ import find_dict_value", number=1000)}')

def find_ordered_dict_value(key='C'):
    return test_ordered_dict[key]

print(f'ordered_dict: '
      f'{timeit.timeit("find_ordered_dict_value()", setup="from __main__ import find_ordered_dict_value", number=1000)}')

'''
тестируем нахождение значения по ключу
dict: 0.00010530000000000001
ordered_dict: 9.81e-05
нахождение значения по ключу в большинстве случаев происходит немного быстрее в ordered dictionary
'''

print()
print('тестируем popitem')

def popitem_dict():
    test_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6}
    test_dict.popitem()

print(f'dict: '
      f'{timeit.timeit("popitem_dict()", setup="from __main__ import popitem_dict", number=1000)}')

def popitem_ordered_dict():
    test_ordered_dict = OrderedDict([('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5), ('F', 6)])
    test_ordered_dict.popitem()

print(f'ordered_dict: '
      f'{timeit.timeit("popitem_dict()", setup="from __main__ import popitem_dict", number=1000)}')

'''
тестируем popitem
dict: 0.000492
ordered_dict: 0.0003277
popitem работает примерно одинаково
'''

print()
print('тестируем update')

def update_dict():
    test_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6}
    test_dict.update({'A': 7, 'B': 8, 'C': 9})

print(f'update_dict: '
      f'{timeit.timeit("update_dict()", setup="from __main__ import update_dict", number=1000)}')

def update_ordered_dict():
    test_ordered_dict = collections.OrderedDict([('A', 1), ('B', 2), ('C', 3), ('D', 4), ('E', 5), ('F', 6)])
    test_ordered_dict.update(collections.OrderedDict([('A', 7), ('B', 8), ('C', 9)]))

print(f'update_ordered_dict: '
      f'{timeit.timeit("update_ordered_dict()", setup="from __main__ import update_ordered_dict", number=1000)}')


'''
тестируем update
update_dict: 0.0005615999999999998
update_ordered_dict: 0.0038485
update работает примерно одинаково
'''