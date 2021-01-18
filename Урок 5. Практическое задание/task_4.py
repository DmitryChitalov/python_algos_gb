"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
import timeit

my_dict = {str(i): i for i in range(1000)}

my_ordered_dict = OrderedDict(my_dict)

other = {'100': 250000}


def popitem_d():
    my_dict.popitem()
    return my_dict


def popitem_ord():
    my_ordered_dict.popitem()
    return my_ordered_dict


def add_el_d():
    my_dict['1001'] = 1001
    return my_dict


def add_el_ord():
    my_ordered_dict['1001'] = 1001
    return my_ordered_dict


def values_el_d():
    return my_dict.values()


def values_el_ord():
    return my_ordered_dict.values()


def update_el_d():
    my_dict.update(other)
    return my_dict


def update_el_ord():
    my_ordered_dict.update(other)
    return my_ordered_dict


## Удаление элементов
print(
    timeit.timeit(
        "popitem_d()", setup="from __main__ import popitem_d",
        number=1000))  ## 0.00034482400224078447
print(
    timeit.timeit(
        "popitem_ord()", setup="from __main__ import popitem_ord",
        number=1000))  ## 0.0005095520027680323

print('####################')
## Добавление элементов
print(
    timeit.timeit(
        "add_el_d()", setup="from __main__ import add_el_d",
        number=10000))  ## 0.0025983039959101006
print(
    timeit.timeit(
        "add_el_ord()", setup="from __main__ import add_el_ord",
        number=10000))  ## 0.0029785860097035766

print('####################')
## Вывод значений
print(
    timeit.timeit(
        "values_el_d()",
        setup="from __main__ import values_el_d",
        number=10000))  ## 0.0028209489973960444
print(
    timeit.timeit(
        "values_el_ord()",
        setup="from __main__ import values_el_ord",
        number=10000))  ## 0.0028910319961141795

print('####################')
## Обновление
print(
    timeit.timeit(
        "update_el_d()",
        setup="from __main__ import update_el_d",
        number=10000))  ## 0.004922035994241014
print(
    timeit.timeit(
        "update_el_ord()",
        setup="from __main__ import update_el_ord",
        number=10000))  ## 0.006816560009610839
"""
В целом, затрачиваемое время на выполнение операций словаря и OrderedDict приблизительно одинаковое.
OrderedDict помнит порядок ключей, в котором они были даны в старых версиях python, однако в нынешних версиях такая функция стала не нужна. 
Тем не менее в OrderedDict есть интересный метод "move_to_end", который может пригодиться в работе.
"""
