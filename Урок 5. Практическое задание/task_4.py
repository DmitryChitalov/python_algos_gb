"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from timeit import timeit
from collections import OrderedDict as ord_d

dict1 = 1000
dict2 = {str(i): i for i in range(1000)}
dict3 = {str(i): i for i in range(100000, 100000)}

ord_dict1 = ord_d(dict2)
ord_dict2 = ord_d(dict3)


def fill_dict(num):
    d = dict()
    for i in range(num):
        d[str(i)] = i

def fill_ord_d(num):
    d = ord_d()
    for i in range(num):
        d[str(i)] = i

def sort_dict(dict):
    d = sorted(dict.items(), key=lambda item: item[1])

def sort_ord_d(dict):
    d = sorted(dict.items(), key=lambda item: item[1])

def get_dict(dict):
    for i in range(len(dict)):
        dict.get(str(i))

def get_ord_d(dict):
    for i in range(len(dict)):
        dict.get(str(i))

def update_dict(dict_1, dict_2):
    dict_1.update(dict_2)

def update_ord_d(dict_1, dict_2):
    dict_1.update(dict_2)

def pop_dict(dict):
    for i in range(len(dict)):
        d = dict.popitem()

def pop_ord_d(dict):
    for i in range(len(dict)):
        d = dict.popitem()


print('fill_dict -',
    timeit(
        'fill_dict(dict1)', globals=globals(), number=10000))
print('fill_ord_d -',
    timeit(
        'fill_ord_d(dict1)', globals=globals(), number=10000))
print('sort_dict -',
    timeit(
        'sort_dict(dict2)', globals=globals(), number=10000))
print('sort_ord_d -',
    timeit(
        'sort_ord_d(dict2)', globals=globals(), number=10000))
print('get_dict -',
    timeit(
        'get_dict(dict2)', globals=globals(), number=10000))
print('get_ord_d -',
    timeit(
        'get_ord_d(dict2)', globals=globals(), number=10000))
print('update_dict -',
    timeit(
        'update_dict(dict2, dict3)', globals=globals(), number=10000))
print('update_ord_d -',
    timeit(
        'update_ord_d(dict2, dict3)', globals=globals(), number=10000))
print('pop_dict -',
    timeit(
        'pop_dict(dict2)', globals=globals(), number=10000))
print('pop_ord_d -',
    timeit(
        'pop_ord_d(dict2)', globals=globals(), number=10000))

'''
Замеры очень близки по показателям, немного выбивается заполнение словаря

fill_dict - 4.8075568
fill_ord_d - 5.5965471

sort_dict - 1.4189903000000008
sort_ord_d - 1.3862094000000003

get_dict - 4.901506800000002
get_ord_d - 4.9839342

update_dict - 0.002828300000000894
update_ord_d - 0.0027681000000008282

pop_dict - 0.004577699999998686
pop_ord_d - 0.004605200000000309
'''
