"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import timeit


def orderdict_check(n):
    orderdict_obj = OrderedDict((str(i), i) for i in range(n))
    orderdict_obj.popitem()
    orderdict_obj["key"] = "value"
    for k, v in orderdict_obj.items():
        k, v


def dict_check(n):
    dict_obj = {str(i):i for i in range(n)}
    dict_obj.popitem()
    dict_obj["key"] = "value"
    for k, v in dict_obj.items():
        k, v


n = 100
print(timeit(f'orderdict_check({n})', setup="from __main__ import orderdict_check", number=10000))
print(timeit(f'dict_check({n})', setup="from __main__ import dict_check", number=10000))

"""
По времени выполнения обычный словарь работает быстрее
"""
