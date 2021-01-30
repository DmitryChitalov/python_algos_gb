"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции, равные по смыслу, с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import Timer


# Dict


def dct1():
    dct = {}
    dct[1] = 1
    dct[100000] = 1000000
    dct[2] = 'hi'

    return dct


def orddct():
    orddct = OrderedDict()
    orddct[1] = 1
    orddct[100000] = 1000000
    orddct[2] = 'hi'

    return orddct


# ord = OrderedDict()
# print(type(ord))

t1 = Timer('dct1()', globals=globals())
t2 = Timer('orddct()', globals=globals())
print(t1.timeit(number=100000))
print(t2.timeit(number=100000))
print(dct1())
print(orddct())

"""
У нас версия 3.9. В этой версии обычный dict также упорядоченный, как и OrderedDict.
Первым тестом я создал dict и OrderedDict:
-------test1---number=100000-------
dict = 0.0060973
OrderedDict = 0.013180899999999999

Обычное создание коллекции уже медленнее у OrderedDict, чем создание простого словаря dict.

Затем я просто добавил ключей в эти словари:
-------test2---number=100000-------
dict = 0.0150029
OrderedDict = 0.0316276

OrderedDict в 2 раза медленнее dict.

Не вижу смысла использовать OrderedDict в версии 3.9, тк он медленнее, и обычный dict уже упорядоченный.
"""
