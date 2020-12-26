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


def bench(decor_func):
    def wrapper(*args, **kwargs):
        start = time.time()
        __result = decor_func(*args, **kwargs)
        end = time.time()
        print(f'Время исполнения: {end - start}')
        return __result
    return wrapper


@bench
def fill_list(num):
    completed_list = []
    for i in range(num):
        completed_list.append(i)
    return completed_list


@bench
def fill_dict(num):
    completed_dict = {}
    for i in range(num):
        completed_dict[i] = i
    return completed_dict

@bench
def from_list_by_key(list,key):
    return list[key]

@bench
def from_dict_by_key(dict,key):
    return dict[key]
@bench
def forloop_dict(dict):
    __count = 0
    for key in dict:
      __count += 1
    return __count
@bench
def forloop_list(list):
    __count = 0
    for elem in list:
        __count += 1
    return __count

print('Заполнение словаря')
filled_dict = fill_dict(1000000)
print('Заполнение списка')
filled_list = fill_list(1000000)

from_dict_by_key(filled_dict,102300)
from_list_by_key(filled_list,102300)

forloop_dict(filled_dict)
forloop_list(filled_list)

'''
Заполнение словаря
Время исполнения: 0.1775226593017578
Заполнение списка
Время исполнения: 0.17253923416137695
Заполнение списка происходит быстрее чем словаря, связано это с реализацией добавления нового ключа в словарь
при добавлении нового ключа вычисляется его хэш

Получение значения по ключу из словаря
Время исполнения: 0.0
Получение значения по ключу из списка
Время исполнения: 0.0

Доступ к элементам словаря и списка происходят одинаково по времени


'''