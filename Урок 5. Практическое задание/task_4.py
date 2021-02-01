"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""


from timeit import timeit
from collections import OrderedDict

#Заполнение словаря тест №1

def dict_test_1():
    dict_get = dict()
    for el in range(1000):
        dict_get[el] = el ** 2

def ordered_dict_test_1():
    o_dict_get = OrderedDict()
    for el in range(1000):
        o_dict_get[el] = el ** 2



print('dict_test_1 :', timeit('dict_test_1()',
                                globals=globals(),
                                number=1000))


print('ordered_dict_test_1 :', timeit('ordered_dict_test_1()',
                                globals=globals(),
                                number=1000))

#Заполнение словаря тест №2

def dict_test_2():
    dict_get = dict()
    for el in range(100, 10000):
        dict_get[el] = el * 2


def ordered_dict_test_2():
    o_dict_get = OrderedDict()
    for el in range(100, 10000):
        o_dict_get[el] = el * 2


print('dict_test_2 :', timeit('dict_test_2()',
                                globals=globals(),
                                number=1000))

print('ordered_dict_test_2 :', timeit('ordered_dict_test_2()',
                                globals=globals(),
                                number=1000))

#Вывод: Стандартный способ заполнения словаря показал лучий результат по сравнению с коллекцией OrderedDict.
