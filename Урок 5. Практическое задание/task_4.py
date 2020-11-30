"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
import collections
from timeit import timeit


d = {str(a + 1) + ' dic': a for a in range(10)}
#Создание словаря
def creature_dict():
    d_1 = {str(a + 1) + ' dic': a for a in range(10)}
    return d_1

#Возвращение пары- ключ:значение
def items_dict():
    d.items()
    return d

# Возвращение ключей
def key_dict():
    d.keys()
    return d

#Обновляем словарь
def update_dict():
    a = {'11 dic': 10, '12 dic': 11}
    d.update(a)
    return d


##########################################################################
od = collections.OrderedDict([(x, x**2) for x in range(10)])

#создание OrderedDict
def creature_od():
    o_d_1 = collections.OrderedDict([(x, x**2) for x in range(10)])
    return o_d_1

# возвращение пар
def items_od():
    od.items()
    return od

# Возвращение ключей
def key_od():
    od.keys()
    return od

# Добавляем занчения в OD
def update_od():
    a = [(10, 100), (11, 121)]
    od.update(a)
    return od

##################################################
print('сравнительная скорость работы по заполениею словаря и OrderedDict')
print(timeit('creature_dict()', setup='from __main__ import creature_dict', number=10000))
print(timeit('creature_od()', setup='from __main__ import creature_od', number=10000))

print('сравнительная скорость работы по возвращению пары ключ:значение словаря и OrderedDict')
print(timeit('items_dict()', setup='from __main__ import items_dict', number=10000))
print(timeit('items_od()', setup='from __main__ import items_od', number=10000))

print('сравнительная скорость работы по возвращению ключей словаря и OrderedDict')
print(timeit('key_dict()', setup='from __main__ import key_dict', number=10000))
print(timeit('key_od()', setup='from __main__ import key_od', number=10000))

print('сравнительная скорость работы по добавлению значений в словарь и OrderedDict')
print(timeit('update_dict()', setup='from __main__ import update_dict', number=10000))
print(timeit('update_dict()', setup='from __main__ import update_dict', number=10000))



