"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""


from collections import OrderedDict
import timeit


dict = {}
order_dict = OrderedDict(dict)
print(dict)
print(order_dict)


def fill_dict(number):
    dict = {i: i * 2 for i in range(number)}
    return dict

def fill_orderdict(number):
    order_dict = {i: i * 2 for i in range(number)}
    return order_dict

def popitem_dict():
    for i in dict:
        dict.pop(i)
    return dict


def popitem_orderdict():
    for i in order_dict:
        order_dict.pop(i)
    return order_dict


def dict_get():
    for i in dict:
        dict.get(i)



def orderdict_get():
    for i in order_dict:
        order_dict.get(i)



number = 100
fill_dict(number)
fill_orderdict(number)

fill_dict_time = timeit.timeit('fill_dict(number)', setup='from __main__ import fill_dict, number', number=1000)
fill_orderdict_time = timeit.timeit('fill_orderdict(number)', setup='from __main__ import fill_orderdict, number', number=1000)
popitem_dict_time = timeit.timeit('popitem_dict', setup='from __main__ import popitem_dict', number=1000)
popitem_orderdict_time = timeit.timeit('popitem_orderdict', setup='from __main__ import popitem_orderdict', number=1000)
get_dict_time = timeit.timeit('dict_get', setup='from __main__ import dict_get', number=1000)
orderget_dict_time = timeit.timeit('orderdict_get', setup='from __main__ import orderdict_get', number=1000)

print(f'Заполнение словаря - {fill_dict_time}')
print(f'Заполнение orderdict - {fill_orderdict_time}')
print(f'Удаление элементов из словаря - {popitem_dict_time}')
print(f'Удаление элементов из orderdict - {popitem_orderdict_time}')
print(f'Значение ключа из словаря - {get_dict_time}')
print(f'Значение ключа из словаря - {orderget_dict_time}')

'''
Опрации с словарем проходят enm быстрее чем с orderdict, но разница незначительная
'''