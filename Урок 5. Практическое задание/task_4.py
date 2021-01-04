"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from timeit import timeit
from collections import OrderedDict

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
my_ord_dict = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4)])

# my_ord_dict.move_to_end('e', last=True)
# Почему-то не работает у меня... что я делаю не так? Поработаю тогда со стандартными методами.


def upd_dict(dict):
    dict.update({'e': 5})


def upd_ord_dict(ord_dict):
    ord_dict.update({'e': 5})


print('Добавление пары в обычный словарь: ', timeit(
        'upd_dict(my_dict)',
        setup='from __main__ import upd_dict, my_dict',
        number=10000))
print('Добавление пары в нумированный словарь: ', timeit(
        'upd_ord_dict(my_ord_dict)',
        setup='from __main__ import upd_ord_dict, my_ord_dict',
        number=10000))

# 0.004423500000000004    0.003956799999999996   0.003914000000000001
# 0.0062914999999999985   0.005482099999999997   0.0053440000000000015
# Обычный быстрее.


def keys_dict(dict):
    return dict.keys()


def keys_ord_dict(ord_dict):
    return ord_dict.keys()


print('Получение клчючей, обычный словарь: ', timeit(
        'keys_dict(my_dict)',
        setup='from __main__ import keys_dict, my_dict',
        number=10000))
print('Получение клчючей, нумированный словарь: ', timeit(
        'keys_ord_dict(my_ord_dict)',
        setup='from __main__ import keys_ord_dict, my_ord_dict',
        number=10000))

# 0.002589099999999997    0.0020821999999999993   0.0020850000000000035
# 0.0025151999999999952   0.0019661000000000053   0.002087699999999998
# Примерно одинаково.


def copy_dict(dict):
    return dict.copy()


def copy_ord_dict(ord_dict):
    return ord_dict.copy()


print('Вернуть копию, обычный словарь: ', timeit(
        'copy_dict(my_dict)',
        setup='from __main__ import copy_dict, my_dict',
        number=10000))
print('Вернуть копию, нумированный словарь: ', timeit(
        'copy_ord_dict(my_ord_dict)',
        setup='from __main__ import copy_ord_dict, my_ord_dict',
        number=10000))

# 0.0027015000000000025   0.002095599999999996   0.0025277999999999967
# 0.006587700000000002    0.0064245              0.007802400000000001
# Обычный имеет приемущество почти в три раза. Думаю, это потому, что помимо ключ-значение нумированный словарь еще
# должен хранить и копировать порядок, как индексация.


def items_dict(dict):
    return dict.items()


def items_ord_dict(ord_dict):
    return ord_dict.items()


print('Вернуть кортежи пар, обычный словарь: ', timeit(
        'items_dict(my_dict)',
        setup='from __main__ import items_dict, my_dict',
        number=10000))
print('Вернуть кортежи пар, нумированный словарь: ', timeit(
        'items_ord_dict(my_ord_dict)',
        setup='from __main__ import items_ord_dict, my_ord_dict',
        number=10000))

# 0.0020962000000000064   0.0019490000000000063   0.0018973000000000045
# 0.0018317000000000055   0.0019022000000000067   0.0017984000000000055
# Примерно одно и то же.

# Сейчас подумала, что проанализировать методы .move_to_end() и popitem() и не получится. Думаю, их невозможно
# сравнить с обычным словарем, ведь в обычном в принципе не существует понятия последний и первый добаленный,
# как я понимаю. Там доступ идет только по ключу.

# Вывод: Обычный словарь работает быстрее нумерованного или примерно так же. Думаю, это из-за отсутствия необходимости
# хранить и анализировать порядок вхождения. Поэтому для методов, которые поддерживает обычный словарь, лучше выбирать
# обычный. Но при какой-то специфической ситуации, где у пар важен быдет именно порядок вхождения -
# тут нумированный может пригодиться.
