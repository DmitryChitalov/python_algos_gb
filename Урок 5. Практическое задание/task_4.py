"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
from timeit import timeit

"""
    1) Заполнение словаря
"""


def f_dict_fill():
    v_base_dict = dict()
    for el in range(1000):
        v_base_dict[el] = el * 2


def f_ordered_fill():
    v_ordered_dict = OrderedDict()
    for el in range(1000):
        v_ordered_dict[el] = el * 2


print("f_dict_fill: ", timeit("f_dict_fill()",
                              globals=globals(),
                              number=1000))
print("f_ordered_fill: ", timeit("f_ordered_fill()",
                                 globals=globals(),
                                 number=1000))

"""
    Традиционный способ отработал быстрее.
    f_dict_fill:     0.13075240000000002     
    f_ordered_fill:  0.16187110000000005
"""
#############################################
"""
    2) Объединение словарей
"""


def f_base_dict_join():
    base_dict_1 = dict()
    base_dict_2 = dict()
    for a in range(1000):
        base_dict_1[a] = a + 2
    for b in range(1000, 2000):
        base_dict_2[b] = b + 3
    base_dict_1.update(base_dict_2)


def f_ord_dict_join():
    ordered_dict_1 = OrderedDict()
    ordered_dict_2 = OrderedDict()
    for a in range(1000):
        ordered_dict_1[a] = a + 2
    for b in range(1000, 2000):
        ordered_dict_2[b] = b + 3
    ordered_dict_1.update(ordered_dict_2)


print("f_base_dict_join: ", timeit("f_base_dict_join()",
                                   globals=globals(),
                                   number=1000))
print("f_ord_dict_join: ", timeit("f_ord_dict_join(),",
                                  globals=globals(),
                                  number=1000))
"""
    Традиционный способ отработал быстрее.
    f_base_dict_join:  0.4443246    
    f_ord_dict_join:   0.5264557999999999
"""
#############################################
"""
    3) Возврат коллекции значений в словаре
"""

v_base_dict = dict()
v_ordered_dict = OrderedDict()
for el in range(1000):
    v_base_dict[el] = chr(el)
    v_ordered_dict[el] = chr(el)


def f_base_values(v_base_dict: dict):
    return v_base_dict.values()


def f_ordered_values(v_ordered_dict: OrderedDict):
    return v_ordered_dict.values()


print("f_base_values: ", timeit("f_base_values(v_base_dict)",
                                globals=globals(),
                                number=1000))
print("f_ordered_values: ", timeit("f_ordered_values(v_ordered_dict)",
                                   globals=globals(),
                                   number=1000))

"""
    Традиционный способ отработал медленее.
    f_base_values:     0.0001634999999999831     
    f_ordered_values:  0.00015969999999998485
"""
