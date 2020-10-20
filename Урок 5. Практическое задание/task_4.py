"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
import timeit
from collections import OrderedDict

just_dict = {'a': 1, 'b': 2, 'c': 3}

order_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3)])


def just_dict_(just_dict):
    for i, k in just_dict.items():
        return i, k


def order_dict_(order_dict):
    for i, k in order_dict.items():
        return i, k


def just_dict_get(just_dict):
    return just_dict.get('a')


def order_dict_get(order_dict):
    return order_dict.get('a')


def just_dict_update(just_dict):
    return just_dict.update({'abc': 4})


def order_dict_update(order_dict):
    return order_dict.update({'abc': 4})


print(timeit.timeit('just_dict_(just_dict)', setup='from __main__ import just_dict_, just_dict', number=1000),
      'dict')

print(timeit.timeit('order_dict_(order_dict)', setup='from __main__ import order_dict_, order_dict', number=1000),
      'orderdict')

print(timeit.timeit('just_dict_get(just_dict)', setup='from __main__ import just_dict_get, just_dict', number=1000),
      'dict')

print(timeit.timeit('order_dict_get(order_dict)', setup='from __main__ import order_dict_get, order_dict', number=1000),
      'orderdict')

print(timeit.timeit('just_dict_update(just_dict)', setup='from __main__ import just_dict_update, just_dict',
                    number=1000), 'dict')

print(timeit.timeit('order_dict_update(order_dict)', setup='from __main__ import order_dict_update, order_dict',
                    number=1000), 'orderdict')


"""
Результат:
0.00033485299999999607 dict
0.0003861700000000051 orderdict
0.00015994299999999573 dict
0.0001629360000000024 orderdict
0.00039215800000000356 dict
0.0004464699999999905 orderdict

По логике orderdict не может быть быстрее он использует одинаковые методы с диктом,
и ко всему этому заточен под сортировку что естественно должно чучуть замедлять исполнение метода.
"""
