"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from timeit import timeit
from collections import OrderedDict


def od_inserts():
    od = OrderedDict()
    for i, el in enumerate(l):
        od.update({el: i})


def dict_inserts():
    d = dict()
    for i, el in enumerate(l):
        d.update({el: i})


def od_val():
    od.values()


def dict_val():
    d.values()


def od_iter():
    for _ in od:
        pass


def dict_iter():
    for _ in d:
        pass



n = 1000000


l = [f'000{i}' for i in range(10)]
print('od_inserts()', timeit('od_inserts()', globals=globals(), number=n))
print('dict_inserts()', timeit('dict_inserts()', globals=globals(), number=n))
od = OrderedDict()
for i, el in enumerate(l):
    od.update({el: i})
print('od_val()', timeit('od_val()', globals=globals(), number=n))
d = dict()
for i, el in enumerate(l):
    d.update({el: i})
print('dict_val()', timeit('dict_val()', globals=globals(), number=n))
print('od_iter()', timeit('od_iter()', globals=globals(), number=n))
print('dict_iter()', timeit('dict_iter()', globals=globals(), number=n))

"""
Результаты:

od_inserts() 2.692646941053681
dict_inserts() 1.5977801930275746
OrderDict вдвое дольше выполняет добавление пары ключ-значение


od_val() 0.07729258795734495
dict_val() 0.0764442509971559
Значения возвращают примерно одинаковое время

od_iter() 0.2826567000010982
dict_iter() 0.1613556079682894
Цикл работает по OrderDict почти в два раза дольше

Вывод: OrderDict хуже оптимизирован, чем dict при остальных одинаковых свойствах

"""