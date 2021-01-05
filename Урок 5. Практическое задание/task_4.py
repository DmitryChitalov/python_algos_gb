"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

import collections
import timeit


domain1 = {"DE": "Germany", "SK": "Slovakia", "HU": "Hungary", "US": "United States", "NO": "Norway"}
domain2 = collections.OrderedDict([('DE', 'Germany'),
                                   ('SK', 'Slovakia'),
                                   ('HU', 'Hungary'),
                                   ('US', 'United States'),
                                   ('NO', 'Norway')])


def keys_from_usual_dict():
    return domain1.keys()


def keys_from_ordered_dict():
    return domain2.keys()


print('Getting keys from usual dict: ',
      timeit.timeit('keys_from_usual_dict()', setup='from __main__ import keys_from_usual_dict', number=100000))

print('Getting keys from ordered_dict: ',
      timeit.timeit('keys_from_ordered_dict()', setup='from __main__ import keys_from_ordered_dict', number=100000))

'''
Здесь по замерам выходит:
Getting keys from usual dict:  0.018011600000000003
Getting keys from ordered_dict:  0.01853889999999999
В данном случае разницы практически нет по скорости
'''

def items_from_usual_dict():
    return domain1.items()


def items_from_ordered_dict():
    return domain2.items()


print('Getting items from usual dict: ',
      timeit.timeit('items_from_usual_dict()', setup='from __main__ import items_from_usual_dict', number=100000))

print('Getting items from ordered_dict: ',
      timeit.timeit('items_from_ordered_dict()', setup='from __main__ import items_from_ordered_dict', number=100000))

'''
Здесь по замерам выходит:
Getting items from usual dict:  0.0176172
Getting items from ordered_dict:  0.0183435
Серьезной разницы по времени нет, чуть быстрее обычный словарь
'''

def get_value_from_usual_dict():
    return domain1.get("NO")


def get_value_from_ordered_dict():
    return domain2.get("NO")


print('Getting value from usual dict: ',
      timeit.timeit('get_value_from_usual_dict()', setup='from __main__ import get_value_from_usual_dict', number=100000))

print('Getting value from ordered_dict: ',
      timeit.timeit('get_value_from_ordered_dict()', setup='from __main__ import get_value_from_ordered_dict', number=100000))

'''
Здесь по замерам выходит:
Getting value from usual dict:  0.0171008
Getting value from ordered_dict:  0.0171597
Разницы по времени нет
'''

def update_usual_dict():
    return domain1.update({'NZ': 'New Zealand'})


def update_ordered_dict():
    return domain2.update({'NZ': 'New Zealand'})


print('Updating usual dict: ',
      timeit.timeit('update_usual_dict()', setup='from __main__ import update_usual_dict', number=100000))

print('Updating ordered_dict: ',
      timeit.timeit('update_ordered_dict()', setup='from __main__ import update_ordered_dict', number=100000))


'''
Здесь по замерам выходит вот что:
Updating usual dict:  0.03230759999999999
Updating ordered_dict:  0.044422199999999995
Разницы по времени довольно существенная в пользу обычных словарей. 


Если делать выводы, что лучше, то выбор однозначно в пользу обычных словарей. Пользуюсь версией python 3.8, здесь 
проблемы с неупорядоченностью словарей нет. Соответственно не вижу смысла в использовании OrderedDict. Существенное 
отличие между двумя словарями проявилось в добавлении в словари новой пары ключ-значение.  
'''
