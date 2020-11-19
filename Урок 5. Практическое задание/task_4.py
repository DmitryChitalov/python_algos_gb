"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from timeit import timeit
from collections import OrderedDict
from random import randint

# заполнение случайными заглавными английскими (или латинскими) буквами:
list_1 = [chr(randint(65, 90)) for i in range(10)]
dict_1 = {}
dict_1 = dict_1.fromkeys(list_1)


for k in dict_1.keys():
    dict_1[k] = randint(1, 100)

dict_2 = OrderedDict(dict_1.items())

item_d1 = chr(randint(65, 90))
while item_d1 not in dict_1.keys():
    item_d1 = chr(randint(65, 90))

item_d2 = chr(randint(65, 90))
while item_d2 not in dict_1.keys():
    item_d2 = chr(randint(65, 90))


def dict_out():
    for key, value in dict_1.items():
        a = key
        b = value


def ordered_dict_out():
    for key, value in dict_2.items():
        c = key
        d = value


def add_el_to_dict():
    dict_1['x'] = randint(101, 200)


def add_el_to_ordered_dict():
    dict_2['y'] = randint(101, 200)


def dict_del_el():
    dict_1 = {}.fromkeys(list_1)
    dict_1.popitem()


def ordered_dict_del_el():
    dict_1 = {}.fromkeys(list_1)
    dict_2 = OrderedDict(dict_1.items())
    dict_2.popitem()


def dict_move_to_end():
    def give_me_el():
        for i in dict_1.keys():
            yield i

    el = next(give_me_el())
    dict_1[el] = dict_1.pop(el)


def dict_move_to_start():
    dict_1 = {}.fromkeys(list_1)
    new_dict_1 = {}
    last_item = dict_1.popitem()
    new_dict_1 = new_dict_1.fromkeys(last_item[0], last_item[1])
    new_dict_1.update(dict_1)


def dict_move_to_end_2():
    temp_dict, temp_dict_2 = dict(), dict()
    needed_val = {}

    next_stage = False
    for k in dict_1.keys():
        if k == item_d1:
            needed_val[k] = dict_1[k]
            next_stage = True
        if next_stage is False:
            temp_dict[k] = dict_1[k]
        else:
            if k != item_d1:
                temp_dict_2[k] = dict_1[k]
    temp_dict.update(temp_dict_2)
    temp_dict.update(needed_val)


def ordered_dict_move_to_end():
    dict_2.move_to_end(item_d2)


def ordered_dict_move_to_start():
    dict_2.move_to_end(item_d2, False)


print(f'Перебор dict:'
      f'\n{timeit("dict_out()", setup="from __main__ import dict_out", number=10000)}\n'
      f'Перебор OrderedDict:\n'
      f'{timeit("ordered_dict_out()", setup="from __main__ import ordered_dict_out", number=10000)}\n'
      f'Добавление элемента в dict:\n'
      f'{timeit("add_el_to_dict()", setup="from __main__ import add_el_to_dict", number=10000)}\n'
      f'Добавление элемента в OrderedDict:\n'
      f'{timeit("add_el_to_ordered_dict()", setup="from __main__ import add_el_to_ordered_dict", number=10000)}\n'
      f'Удаление элемента из dict:\n'
      f'{timeit("dict_del_el()", setup="from __main__ import dict_del_el", number=10000)}\n'
      f'Удаление элемента из Ordered dict:\n'
      f'{timeit("ordered_dict_del_el()", setup="from __main__ import ordered_dict_del_el", number=10000)}\n'
      f'Перемещение элемента в начало в dict:\n'
      f'{timeit("dict_move_to_start()", setup="from __main__ import dict_move_to_start", number=10000)}\n'
      f'Перемещение элемента в конец в dict:\n'
      f'{timeit("dict_move_to_end()", setup="from __main__ import dict_move_to_end", number=10000)}\n'
      f'Перемещение элемента в конец с любой позиции в dict:\n'
      f'{timeit("dict_move_to_end_2()", setup="from __main__ import dict_move_to_end_2", number=10000)}\n'
      f'Перемещение первого элемента в конец в OrderedDict:\n'
      f'{timeit("ordered_dict_move_to_end()", setup="from __main__ import ordered_dict_move_to_end", number=10000)}\n'
      f'Перемещение элемента в начало с любой позиции в OrderedDict:\n'
      f'{timeit("ordered_dict_move_to_start()", setup="from __main__ import ordered_dict_move_to_start", number=10000)}\n')

'''
Наблюдения и выводы:
использовать OrderedDict нет необходимости ввиду упорядоченности словарей в новой версии Python;
если в проекте нужно периодически перемещать быстро (во всех смыслах) элементы в начало или в
конец словаря, то OrderedDict делает это одной строкой кода и за короткое время.
'''
