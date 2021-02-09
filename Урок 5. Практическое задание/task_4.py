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


def base_dict_fill():
    base_dict = dict()
    for el in range(1000):
        base_dict[el] = el * 2


def ordered_dict_fill():
    ordered_dict = OrderedDict()
    for el in range(1000):
        ordered_dict[el] = el * 2


print("base_dict_fill: ", timeit("base_dict_fill()",
                                 globals=globals(),
                                 number=1000))
print("ordered_dict_fill: ", timeit("ordered_dict_fill()",
                                    globals=globals(),
                                    number=1000))

"""
    Традиционный способ заполнения словаря показал лучий результат по сравнению с коллекцией.
    base_dict_fill:  0.098164   VS  ordered_dict_fill:  0.128627
"""
#############################################
"""
    2) Объединение словарей
"""


def base_dict_merger():
    base_dict_1 = dict()
    base_dict_2 = dict()
    for a in range(1000):
        base_dict_1[a] = a + 2
    for b in range(1000, 2000):
        base_dict_2[b] = b + 3
    base_dict_1.update(base_dict_2)


def ordered_dict_merger():
    ordered_dict_1 = OrderedDict()
    ordered_dict_2 = OrderedDict()
    for a in range(1000):
        ordered_dict_1[a] = a + 2
    for b in range(1000, 2000):
        ordered_dict_2[b] = b + 3
    ordered_dict_1.update(ordered_dict_2)


print("base_dict_merger: ", timeit("base_dict_merger()",
                                   globals=globals(),
                                   number=1000))
print("ordered_dict_merger: ", timeit("ordered_dict_merger(),",
                                      globals=globals(),
                                      number=1000))
"""
    В случае объединения словарей коллекция отработала медленее.
    base_dict_merger:  0.2525524    VS  ordered_dict_merger:  0.3533279
"""
#############################################
"""
    3) Возврат коллекции значений в словаре
"""


base_dict = dict()
ordered_dict = OrderedDict()
for el in range(1000):
    base_dict[el] = chr(el)
    ordered_dict[el] = chr(el)

def base_dict_values(base_dict:dict):
    return base_dict.values()


def ordered_dict_values(ordered_dict:OrderedDict):
    return ordered_dict.values()


print("base_dict_values: ", timeit("base_dict_values(base_dict)",
                                 globals=globals(),
                                 number=1000))
print("ordered_dict_values: ", timeit("ordered_dict_values(ordered_dict)",
                                    globals=globals(),
                                    number=1000))

"""
    В случае возврата значений принципиальной разницы не заметил.
    base_dict_values:  0.0001106    VS  ordered_dict_values:  0.0001179
"""
