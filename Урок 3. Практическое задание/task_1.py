"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

import time


def decor_time(func):
    def func_time(*args):
        start = time.time()
        res = func(*args)
        stop = time.time()
        return res, f'Потрачено  {stop - start} c для {func.__name__}'

    return func_time


# Функции для создания списков и словаря. Так как взял данные ключ - значение,
# то будет 2 списка

@decor_time
def lst_add(text_list):
    for date in text_list:
        list1.append(date.replace(')', '').split(' (')[0])
        list2.append(date.replace(')', '').split(' (')[1])
    return list1, list2


@decor_time
def dict_add(text_list):
    for note in text_list:
        note_list = note.replace(')', '').split(' (')
        dict1.update({note_list[0]: note_list[1]})
    return dict1


# В создании списков и словаря и добавлении значений время незначительное,
# операции схожи и имеют линейную сложность


@decor_time
def list_take_one(idx):
    return f'{list1[idx]} {list2[idx]}'


@decor_time
def dict_take_one(key):
    return f'{key} {dict1[key]}'


'''
Вычислительная сложность получения значений зависит от предмета поиска.

Если я ищу Томаса Джефферсона, то быстрее работает словарь - константная сложность,
а у двух списков - линейный поиск или логарифмический бинарный поиск. 

Если я ищу 3го президента США, то ситуация обратная - константный выбор из списков,
а поиск в словаре надежно вообще невозможен без указания номера президента
'''


# Попробуем задачу - найти всех президентов с 1900 по 1950 годы
@decor_time
def list_find(start, end):
    res = ''
    for idx, date in enumerate(list2):
        date_list = date.split('-')
        if len(date_list) > 1:
            pres_start, pres_stop = [int(date_list[0]), int(date_list[1])]
        else:
            pres_stop = pres_start = int(date_list[0])
        if start <= pres_stop and end >= pres_start:
            res += f'{list1[idx]} {list2[idx]}\n'
            continue
        else:
            continue
    return res


@decor_time
def dict_find(start, end):
    res = ''
    for key, val in dict1.items():
        date_list = val.split('-')
        if len(date_list) > 1:
            pres_start, pres_stop = [int(date_list[0]), int(date_list[1])]
        else:
            pres_stop = pres_start = int(date_list[0])
        if start <= pres_stop and end >= pres_start:
            res += f'{key} {val}\n'
            continue
        else:
            continue
    return res


'''
По результатам выполнения задачи у меня все свелось фактически к одним и тем же действиям
и для списков и для словаря.
Вывод: оба типа данных быстрые и удобные, если их использовать по назначению - список для 
упорядоченных данных, словари - для пар значений
'''


#############################################

text_presds = []
list1 = []
list2 = []
dict1 = {}

with open('presidents.txt', 'r', encoding='utf-8') as presidents:
    text_presds = presidents.read().split('\n')

print(lst_add(text_presds)[0], '\n', lst_add(text_presds)[1], '\n')
print(dict_add(text_presds)[0], '\n', dict_add(text_presds)[1], '\n')
print(list_take_one(2)[0], '\n', list_take_one(2)[1], '\n')
print(dict_take_one('Томас Джефферсон')[0], '\n', dict_take_one('Томас Джефферсон')[1], '\n')

print(list_find(1900, 1950)[0], '\n', list_find(1900, 1950)[1], '\n')
print(dict_find(1900, 1950)[0], '\n', dict_find(1900, 1950)[1])