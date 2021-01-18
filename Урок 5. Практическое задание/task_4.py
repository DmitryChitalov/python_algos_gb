"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
import timeit

int_dict = {x: (x + 2) for x in range(0, 100)}
int_ordered = OrderedDict(int_dict)
other_dict = {x: (x+2) for x in range(200, 210)}

print(f'update_Dict - {timeit.timeit(lambda: int_dict.update(other_dict), number=100)}')
print(f'update_OrderedDict - {timeit.timeit(lambda: int_ordered.update(other_dict), number=100)}')

print(f'get_keys_Dict - {timeit.timeit(lambda: int_dict.keys(), number=100)}')
print(f'get_keys_OrderedDict - {timeit.timeit(lambda: int_ordered.keys(), number=100)}')

print(f'get_items_Dict - {timeit.timeit(lambda: int_dict.items(), number=100)}')
print(f'get_items_OrderedDict - {timeit.timeit(lambda: int_ordered.items(), number=100)}')

print(f'del_last_item_OrderedDict - {timeit.timeit(lambda: int_ordered.popitem(), number=100)}')
print(f'del_last_item_Dict - {timeit.timeit(lambda: int_dict.popitem(), number=100)}')


'''
результаты замеров не дают однозначный ответ что лучше Dict или OrderDict. Каждый имеет свои приемущества в различных 
операциях. OrderDict лучше подходит для сохранения порядка элементов в словаре. Существенное приемущество по времени 
при выполнении операции обновления
update_Dict - 5.759999999999099e-05
update_OrderedDict - 0.00018689999999998985
get_keys_Dict - 2.0499999999992746e-05
get_keys_OrderedDict - 2.5200000000002998e-05
get_items_Dict - 3.849999999999687e-05
get_items_OrderedDict - 2.0199999999997997e-05
del_last_item_OrderedDict - 4.300000000000137e-05
del_last_item_Dict - 2.2499999999994746e-05
'''