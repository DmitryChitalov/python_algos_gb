"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

import collections
from timeit import timeit
import cProfile


def dict_speed_test():
    s_dict = {'one': 'один',
              'two': 'два'}
    s_dict['three'] = 'три'
    s_dict.get('one')
    del s_dict['three']
    s_dict.items()

def orderdict_speed_test():
    s_dict = {'one': 'один',
              'two': 'два'}
    new_d = collections.OrderedDict(s_dict.items())
    new_d['three'] = 'три'
    new_d.get('one')
    s_dict.popitem()


print(timeit('dict_speed_test()', setup='from __main__ import dict_speed_test'))
print(timeit('orderdict_speed_test()', setup='from __main__ import orderdict_speed_test'))
print(cProfile.run('''def dict_speed_test():
    s_dict = {'one': 'один',
              'two': 'два'}
    s_dict['three'] = 'три'
    s_dict.get('one')
    del s_dict['three']
    s_dict.items()'''))

print(cProfile.run('''def orderdict_speed_test():
    s_dict = {'one': 'один',
              'two': 'два'}
    new_d = collections.OrderedDict(s_dict.items())
    new_d['three'] = 'три'
    new_d.get('one')
    s_dict.popitem()'''))

# order dict работает гораздо медленнее(как я понял исходя из вычислений по времени)
