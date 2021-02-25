"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from timeit import timeit
from collections import OrderedDict

test_dict = {str(i): i for i in range(1000)}
test_odict = OrderedDict(test_dict)


def access_dict(dict):
    for key, value in dict.items():
        a = key
        b = value


def access_odict(odict):
    for key, value in odict.items():
        a = key
        b = value


def pop_dict(dict):
    for i in range(len(dict)):
        a = dict.popitem()


def pop_odict(odict):
    for i in range(len(odict)):
        a = odict.popitem()


def get_dict(dict):
    for i in range(len(dict)):
        dict.get(str(i))


def get_odict(odict):
    for i in range(len(odict)):
        odict.get(str(i))


def update_dict(dict):
    dict.update({str(i): i for i in range(1000, 1100)})


def update_odict(odict):
    odict.update({str(i): i for i in range(1000, 1100)})


print('=== access ===')
print(timeit("access_dict(test_dict)",
             number=1000,
             globals=globals()))
print(timeit("access_odict(test_odict)",
             number=1000,
             globals=globals()))
print('=== pop ===')
print(timeit("pop_dict(test_dict)",
             number=1000,
             globals=globals()))
print(timeit("pop_odict(test_odict)",
             number=1000,
             globals=globals()))
print('=== get ===')
print(timeit("get_dict(test_dict)",
             number=1000,
             globals=globals()))
print(timeit("get_dict(test_odict)",
             number=1000,
             globals=globals()))
print('=== update ===')
print(timeit("update_dict(test_dict)",
             number=1000,
             globals=globals()))
print(timeit("update_odict(test_odict)",
             number=1000,
             globals=globals()))
#В целом, Order Dict оптимизирован хуже
