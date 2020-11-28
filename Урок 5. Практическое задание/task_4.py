"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from timeit import timeit
from collections import OrderedDict

dict_one = {str(i): i for i in range(1, 100, 2)}
dict_two = {str(i): i for i in range(1, 100, 3)}

order_dict_one = OrderedDict(dict_one)
order_dict_two = OrderedDict(dict_two)

def filling_dict():
    my_dict = dict()
    for i in range(20):
        my_dict[str(i)] = i

def filling_order_dict():
    my_dict = OrderedDict()
    for i in range(20):
        my_dict[str(i)] = i

print(timeit("filling_dict()", setup="from __main__ import filling_dict"))
print(timeit("filling_order_dict()", setup="from __main__ import filling_order_dict"))

'''
Результат замеров:
6.366248353
7.208912933
Вывод: order_dict работает медленее
'''

def update_dict():
    dict_one = {str(i): i for i in range(1, 20, 2)}
    dict_two = {str(i): i for i in range(1, 20, 3)}
    dict_one.update(dict_two)

def update_order_dict():
    dict_one = {str(i): i for i in range(1, 20, 2)}
    dict_two = {str(i): i for i in range(1, 20, 3)}
    order_dict_one = OrderedDict(dict_one)
    order_dict_two = OrderedDict(dict_two)
    order_dict_one.update(order_dict_two)

print(timeit("update_dict()", setup="from __main__ import update_dict"))
print(timeit("update_order_dict()", setup="from __main__ import update_order_dict"))

'''Результат замеров:
6.114145746
9.957325223999998
Вывод: order_dict работает медленее. Использование этого модуля в новом Питоне не целесообразно'''