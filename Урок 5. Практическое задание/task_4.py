"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""


from collections import OrderedDict
from random import randint
from timeit import timeit

dic_obj = dict()
ord_obj = OrderedDict()
ARRAY_SIZE = 500


def dic_fill(obj):
    for i in range(ARRAY_SIZE):
        obj[randint(0, 1000)] = randint(0, 1000)


print("\n1) Проверка заполнения словаря.\n")
print("dict: ", timeit("dic_fill(dic_obj)", setup="from __main__ import dic_fill, dic_obj", number=1000))
print("OrderedDict: ", timeit("dic_fill(ord_obj)", setup="from __main__ import dic_fill, ord_obj", number=1000))

print("\n2) Проверка извлечения ключей.\n")
print("dict: ", timeit("dic_obj.keys()", setup="from __main__ import dic_obj"))
print("OrderedDict: ", timeit("ord_obj.keys()", setup="from __main__ import ord_obj"))

print("\n3) Проверка извлечения значений.\n")
print("dict: ", timeit("dic_obj.values()", setup="from __main__ import dic_obj"))
print("OrderedDict: ", timeit("ord_obj.values()", setup="from __main__ import ord_obj"))

print("\n4) Проверка извлечения ключей и значений.\n")
print("dict: ", timeit("dic_obj.items()", setup="from __main__ import dic_obj"))
print("OrderedDict: ", timeit("ord_obj.items()", setup="from __main__ import ord_obj"))

print("\n5) Проверка удаления ключей и значений.\n")
print("dict: ", timeit("dic_obj.popitem()", setup="from __main__ import dic_obj", number=ARRAY_SIZE))
print("OrderedDict: ", timeit("ord_obj.popitem()", setup="from __main__ import ord_obj", number=ARRAY_SIZE))

"""
Все проверенные функции имеют примерно одинаковое время исполнения как на dict, так и на OrderedDict.
То есть нет серьёзных причин использовать OrderedDict на современных реализациях python
"""
