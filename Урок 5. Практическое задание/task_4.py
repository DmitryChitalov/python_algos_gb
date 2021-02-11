"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
from timeit import timeit


def create_dict(num):
    my_dict = dict()
    for i in range(num):
        my_dict[i] = i
    return my_dict


def create_ordered_dict(num):
    my_dict = OrderedDict()
    for i in range(num):
        my_dict[i] = i
    return my_dict


def pop_dict(my_dict):
    for i in range(len(my_dict)):
        el = my_dict.popitem()


def pop_ordered_dict(my_dict):
    for i in range(len(my_dict)):
        el = my_dict.popitem()


def get_dict(my_dict):
    for i in range(len(my_dict)):
        el = my_dict.get(i)


def get_ordered_dict(my_dict):
    for i in range(len(my_dict)):
        el = my_dict.get(i)


def print_timeint(func_name, n):
    print(f'{func_name} {timeit(f"{func_name}({n})", globals=globals(), number=10000)}')

n = 1000
simple_dict = create_dict(n)
ordered_dict = create_ordered_dict(n)

print_timeint('create_dict', n)
print_timeint('create_ordered_dict', n)
print_timeint('pop_dict', simple_dict)
print_timeint('pop_ordered_dict', ordered_dict)
print_timeint('get_dict', simple_dict)
print_timeint('get_ordered_dict', ordered_dict)

"""
create_dict 0.6007888
create_ordered_dict 1.2769747
pop_dict 1.1560505
pop_ordered_dict 2.5944715
get_dict 0.9619989000000002
get_ordered_dict 1.8534487000000004

По всем показателям OrderedDict существенно хуже чем обычный словарь. 
"""
