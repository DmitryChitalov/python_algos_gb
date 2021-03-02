"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

 
И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from random import randint
from timeit import timeit

easy_dict = {}
order_dict = OrderedDict()
example_list = [randint(el, el * el) for el in range(10000)]
example_key = ["key" + str(el) for el in range(10000)]


def chck_append_dict():
    for i in range(len(example_list)):
        easy_dict[example_key[i]] = example_list[i]
    return


def chck_append_orddict():
    for i in range(len(example_list)):
        order_dict[example_key[i]] = example_list[i]
    return


def chck_popitem_dict():
    easy_dict.popitem()
    return


def chck_popitem_orddict():
    order_dict.popitem()
    return


def chck_getnone_dic():
    easy_dict.get("qwer")
    return


def chck_getnone_orderdict():
    order_dict.get("qwer")
    return


def chck_sorted_dic():
    sorted(easy_dict.items(), reverse=True)
    return


def chck_sorted_orderdict():
    sorted(order_dict.items(), reverse=True)
    return


n_timeit = 10000  # количество тестов для timeit
print("-------------- замеры --------------------------")

print("append")
print("chck_append_dict", timeit('chck_append_dict()', setup='from __main__ import chck_append_dict', number=n_timeit))
print("chck_append_orddict",
      timeit('chck_append_orddict()', setup='from __main__ import chck_append_orddict', number=n_timeit))

print("popitem")
print("chck_popitem_dict",
      timeit('chck_popitem_dict()', setup='from __main__ import chck_popitem_dict', number=n_timeit))
print("chck_popitem_orddict",
      timeit('chck_popitem_orddict()', setup='from __main__ import chck_popitem_orddict', number=n_timeit))

print("get none key")
print("chck_getnone_dic", timeit('chck_getnone_dic()', setup='from __main__ import chck_getnone_dic', number=n_timeit))
print("chck_getnone_orderdict",
      timeit('chck_getnone_orderdict()', setup='from __main__ import chck_getnone_orderdict', number=n_timeit))

print("sorted")
print("chck_sorted_dic", timeit('chck_sorted_dic()', setup='from __main__ import chck_sorted_dic', number=n_timeit))
print("chck_sorted_orderdict",
      timeit('chck_sorted_orderdict()', setup='from __main__ import chck_sorted_orderdict', number=n_timeit))

"""
-------------- замеры --------------------------
append  заполнение коллекции оказалось быстрее
chck_append_dict 15.846673
chck_append_orddict 17.888457600000002
popitem     время одинаковое
chck_popitem_dict 0.0019852000000000203
chck_popitem_orddict 0.0029018999999976813
get none key  время одинаковое
chck_getnone_dic 0.0015036000000065997
chck_getnone_orderdict 0.002265299999997694
sorted      время одинаковое
chck_sorted_dic 0.004427499999998474
chck_sorted_orderdict 0.004626899999998102
не вижу смысла испльзовать OrderedDict в современных версиях интерпретатора 
"""