"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from timeit import timeit
from collections import OrderedDict
from random import randint


def fill_dict(my_dict, counter):
    my_dict = {i: chr(i) for i in range(counter)}
    return my_dict


def get_slice(my_dict, counter):
    return list(my_dict.get(randint(0, 99)) for i in range(counter))


def get_pops(my_dict, counter):
    return [my_dict.popitem() for i in range(counter)]


if __name__ == '__main__':
    simple_dict = {}
    ordered_dict = OrderedDict()
    # fill_dict(simple_dict, 100)
    # fill_dict(ordered_dict, 100)
    print(timeit(
        'fill_dict(simple_dict, 100)',
        setup='from __main__ import fill_dict,simple_dict',
        number=100))
    print(timeit(
        'fill_dict(ordered_dict, 100)',
        setup='from __main__ import fill_dict,ordered_dict',
        number=100))
    """ 
    0.0009533999999999931
    0.0009438000000000085
    Заполнение по времени если и отличается то на грани погрешности
    """
    simple_dict = fill_dict(simple_dict, 1010)
    ordered_dict = fill_dict(ordered_dict, 1010)
    # print(get_slice(simple_dict, 10))
    # print(get_slice(ordered_dict, 10))
    print(timeit(
        'get_slice(simple_dict, 10)',
        setup='from __main__ import get_slice,simple_dict',
        number=100))
    print(timeit(
        'get_slice(ordered_dict, 10)',
        setup='from __main__ import get_slice,ordered_dict',
        number=100))
    """ 
    0.0009532000000000013
    0.0009336000000000066
    выбрать 10 рандомных значений тоже по времени не отличается, немножко пляшет из-за рандома
    # """
    print(get_pops(simple_dict, 10))
    print(get_pops(ordered_dict, 10))
    """ возвращаются списки один в один сопадающие"""

    print(timeit(
        'get_pops(simple_dict, 10)',
        setup='from __main__ import get_pops,simple_dict',
        number=100))
    print(timeit(
        'get_pops(ordered_dict, 10)',
        setup='from __main__ import get_pops,ordered_dict',
        number=100))
    # а тут была неожиданность в виде окончания словаря, который на старте был 100,
    # и закончился после 100 прогонов по 10 pop-ов. Пришлось расширить изначальный словарь до 1010
"""
    0.0001562999999999981
    0.0001527000000000056
    Также разница на уровне погрешности
    Общий вывод - обычный словарь и OrderDict ничем не отличаются в данной версии python (3.9.0) и скорее всего 
    это одно и тоже, а коллекция OrderDict в collections осталена для обратной совместимости легаси кода
"""
