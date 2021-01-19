"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

import time
from collections import OrderedDict


def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return res

    return wrapper


@benchmark
def init_dist():
    default_dict = dict()
    for i in range(1000):
        default_dict[str(i)] = i
    return default_dict


@benchmark
def init_ordered_dict():
    ordered_dict = OrderedDict()
    for i in range(1000):
        ordered_dict[str(i)] = i
    return ordered_dict


@benchmark
def pop_from_default_dict(default_dict):
    for i in range(len(default_dict)):
        a = default_dict.popitem()


@benchmark
def pop_from_ordered_dict(ordered_dict):
    for i in range(len(ordered_dict)):
        a = ordered_dict.popitem()


@benchmark
def key_value_default_dict(default_dict):
    for key, value in default_dict.items():
        k = key
        v = value


@benchmark
def key_value_ordered_dict(ordered_dict):
    for key, value in ordered_dict.items():
        k = key
        v = value


@benchmark
def get_item_default_dict(default_dict):
    a = default_dict.get('900')


@benchmark
def get_item_ordered_dict(ordered_dict):
    a = ordered_dict.get('900')


default_dict = init_dist()
ordered_dict = init_ordered_dict()
pop_from_default_dict(default_dict)
pop_from_ordered_dict(ordered_dict)
key_value_default_dict(default_dict)
key_value_ordered_dict(ordered_dict)
get_item_default_dict(default_dict)
get_item_ordered_dict(ordered_dict)

"""
довольно похожие по производительности коллекции, 
но OrderedDict в среднем чуть медленнее во всех операциях, чем обычный словарь
"""