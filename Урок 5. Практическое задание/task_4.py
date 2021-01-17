"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
import collections
from timeit import timeit


def func_with_dict():               # Заполнение словаря dict (простой словарь)
    d = dict()
    for i in range(1, 1000):
        name = f'key_{i}'
        d[name] = i
    return d


def func_with_ordereddict():        # Заполнение словаря OrderedDict
    d = collections.OrderedDict()   # Словарь с памятью порядка добавления элементов
    for i in range(1, 1000):
        name = f'key_{i}'
        d[name] = i
    return d


def cycle_dict():                   # Перебор пар простого словаря и сохранение в новом простом словаре
    d = func_with_dict()            # только четных ключей и их значений
    new_d = dict()
    for key, value in d.items():
        if int(key[-1]) % 2 == 0:
            new_d[key] = value * 2
    return new_d


def cycle_ordereddict():            # Перебор пар словаря OrderedDict и сохранение в новом словаре OrderedDict
    d = func_with_ordereddict()         # только четных ключей и их значений
    new_d = collections.OrderedDict()
    for key, value in d.items():
        if int(key[-1]) % 2 == 0:
            new_d[key] = value * 2
    return new_d


time_1 = timeit('func_with_dict()',
                setup='from __main__ import func_with_dict', number=1000)
time_2 = timeit('func_with_ordereddict()',
                setup='from __main__ import func_with_ordereddict', number=1000)

time_3 = timeit('cycle_dict()',
                setup='from __main__ import cycle_dict', number=1000)
time_4 = timeit('cycle_ordereddict()',
                setup='from __main__ import cycle_ordereddict', number=1000)

print(f'Заполненный список dict (простой словарь):\n {func_with_dict()}')
print(f'Заполненный список OrderedDict:\n {func_with_ordereddict()}')

print('\nВремя заполнения пустого dict ключами со значениями: {:.2f}'.format(time_1))
print('Время заполнения пустого OrderedDict ключами со значениями: {:.2f}'.format(time_2))

print('\nВремя заполнения и перебора пар из dict, а также добавление только \n'
      'четных ключей со значениями в новый словарь dict (new_d): {:.2f}'.format(time_3))
print('\nВремя заполнения и перебора пар из OrderedDict, а также добавление только \n'
      'четных ключей со значениями в новый словарь OrderedDict (new_d): {:.2f}'.format(time_4))

"""Выводы: Заполнение и перебор пар в простом словаре (dict) занимает немного меньше времени,
   чем аналогичные операции со словарем OrderedDict. К тому же, при выводе двух параллельно созданных
   словарей видно, что оба словаря имеют память порядка добавления элементов.
   Поэтому использование OrderedDict перестает быть необходимым."""
