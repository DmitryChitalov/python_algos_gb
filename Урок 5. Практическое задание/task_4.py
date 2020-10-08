"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
########################################################################################################################

from collections import OrderedDict
from timeit import timeit

simple_dict = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
order_dict = OrderedDict({0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 5})


def a():
    simple_dict.items()
    simple_dict.values()
    simple_dict.keys()
    simple_dict.get(1)
    return


print(
    timeit(
        'a()',
        setup='from __main__ import a',
        number=1000
    )
)


def b():
    order_dict.items()
    order_dict.values()
    order_dict.keys()
    order_dict.get(1)


print(
    timeit(
        'b()',
        setup='from __main__ import b',
        number=1000
    )
)


"""
Вывод:

Нет никакой разницы во времени работы, как и пользы, если конечно у вас не старая версия интерпретатора.
Версия 3.7 даже не предложит его вам, так как не видит, надобность в данной функции исчезла. 
"""