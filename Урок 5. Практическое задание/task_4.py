"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from timeit import timeit

from collections import OrderedDict

dct = {str(i): i for i in range(10000)}
ord_dict = OrderedDict(dct)


def dict_fill(num):
    a = dict()
    for i in range(num):
        a[str(i)] = i


def dict_order_fill(num):
    a = OrderedDict()
    for i in range(num):
        a[str(i)] = i


def dict_get(filled_dict):
    for i in range(len(filled_dict)):
        filled_dict.get(str(i))


def dict_order_get(filled_dict):
    for i in range(len(filled_dict)):
        filled_dict.get(str(i))


name_list = 'dict_fill dict_order_fill dict_get dict_order_get'.split()


for id, func_name in enumerate(name_list):
    if id == 0 or id == 1:
        print(f"{func_name} -",
              timeit(stmt=func_name + f'(1000)',
                      number=10000, globals=globals()))

    else:
        print(
            f"{func_name} -",
            timeit(stmt=func_name + f'(dct.copy())',
                    number=10000, globals=globals()))
"""
dict_fill - 1.8057179
dict_order_fill - 2.1481104
dict_get - 18.6697373
dict_order_get - 18.5669871

order dict заполняется дольше, выборка примерно одинаковая, у ордера чуть лучше

"""