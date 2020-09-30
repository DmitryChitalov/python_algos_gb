"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
"""
   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
   
    10000    0.015    0.000   22.180    0.002 task_4.py:12(dict_create)
    10000    1.161    0.000   23.291    0.002 task_4.py:16(ordereddict_create)
    
    10000    0.004    0.000    0.004    0.000 task_4.py:20(dict_ap)
    10000    0.003    0.000    0.003    0.000 task_4.py:24(ordereddict_ap)
    
    10000    0.002    0.000    0.002    0.000 task_4.py:28(dist_get)
    10000    0.002    0.000    0.002    0.000 task_4.py:32(ordereddict_get)
    
    10000    0.005    0.000    0.008    0.000 task_4.py:36(dist_keys)
    10000    0.004    0.000    0.006    0.000 task_4.py:40(ordereddict_keys)
    
    10000    0.005    0.000    0.008    0.000 task_4.py:44(dist_pop)
    10000    0.008    0.000    0.018    0.000 task_4.py:47(ordereddict_pop)
    
    10000    0.004    0.000    0.006    0.000 task_4.py:69(dict_by_func_get)
    10000    0.004    0.000    0.005    0.000 task_4.py:73(ordereddict_by_func_get)
    
операция                -   кто быстрее
создание                -   словарь
добавление              -   упорядоченный словарь
удаление                -   словарь
получение               -   одинаково
получение  .get()       -   упорядоченный словарь
получение ключей        -   упорядоченный словарь

OrderedDict - дольше создаеться и очень долго удаляет элементы. Чуть быстрее получает значения.
Применять можно для ускорения, но только там где нет удаления элеметов из словаря.
"""
import cProfile
import random
from collections import OrderedDict


def dict_create():
    return {x: random.randint(1000, 2000) for x in range(1000)}


def ordereddict_create():
    return OrderedDict({x: random.randint(1000, 2000) for x in range(1000)})


def dict_ap(my_dict_in):
    my_dict_in[2000] = '0'


def ordereddict_ap(my_ordereddict_in):
    my_ordereddict_in[2000] = '0'


def dist_get(my_dict_in):
    return my_dict_in[2000]


def ordereddict_get(my_ordereddict_in):
    return my_ordereddict_in[2000]


def dist_keys(my_dict_in):
    return my_dict_in.keys()


def dict_by_func_get(my_dict_in):
    return my_dict_in.get(500)


def ordereddict_by_func_get(my_ordereddict_in):
    return my_ordereddict_in.get(500)


def ordereddict_keys(my_ordereddict_in):
    return my_ordereddict_in.keys()


def dist_pop(my_dict_in):
    return my_dict_in.pop(2000)


def ordereddict_pop(my_ordereddict_in):
    return my_ordereddict_in.pop(2000)


def main():
    for _ in range(10000):
        x = dict_create()
        y = ordereddict_create()
        dict_ap(x)
        ordereddict_ap(y)
        dist_get(x)
        ordereddict_get(y)
        dist_keys(x)
        ordereddict_keys(y)
        dist_pop(x)
        ordereddict_pop(y)
        dict_by_func_get(x)
        ordereddict_by_func_get(y)


if __name__ == '__main__':
    cProfile.run('main()')
