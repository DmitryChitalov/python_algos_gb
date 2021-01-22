"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""
from collections import OrderedDict
from timeit import timeit
import cProfile

simple_dict = {}
ordered_dict = OrderedDict()

"""
Для замеров создадим функуции: заполнение словаря, удаление пар, взяти пары ключ и создание из них нового 
словаря.
"""


def make_dict(my_dict):
    for i in range(1000000):
        my_dict[i] = i
    return my_dict


print(f'Скорость наполнения простого словаря\n',
      timeit('make_dict(simple_dict)', setup='from __main__ import make_dict, simple_dict', number=100))
print(f'Скорость наполнения словаря с памятью порядка элементов\n',
      timeit('make_dict(ordered_dict)', setup='from __main__ import make_dict, ordered_dict', number=100))


def del_half_dict(my_dict):
    for i in range(500000, 1000000):
        my_dict.pop(i)
    return my_dict

"""
Расчет времени для pop не хочет выполнять KeyError 500.Вроде все правильно.Не смог понять, в чем причина, воспользовался
cProfile
"""
# print(f'Скорость удаления половины пар простого словаря\n',
#       timeit('del_half_dict(simple_dict)', setup='from __main__ import del_half_dict, simple_dict', number=10000))
# print(f'Скорость удаления половины пар словаря с памятью порядка элементов\n',
#       timeit('del_half_dict(ordered_dict)', setup='from __main__ import del_half_dict, ordered_dict', number=10000))


def take_items_dict(my_dict):
    new_dict = {}
    for i in range(150000, 450000):
        new_dict[i] = my_dict.get(i)
    return new_dict


print(f'Скорость взятия по ключу простого словаря\n',
      timeit('take_items_dict(simple_dict)', setup='from __main__ import take_items_dict, simple_dict', number=100))
print(f'Скорость взятия по ключу словаря с памятью порядка элементов\n',
      timeit('take_items_dict(ordered_dict)', setup='from __main__ import take_items_dict, ordered_dict', number=100))


def main_simp():
    make_dict(simple_dict)
    del_half_dict(simple_dict)
    take_items_dict(simple_dict)


def main_ord():
    make_dict(ordered_dict)
    del_half_dict(ordered_dict)
    take_items_dict(simple_dict)


cProfile.run('main_simp()')
cProfile.run('main_ord()')

"""
Данные приведенные ниже показывают что:
- скорость наполнения простого словаря быстрее, чем словаря с памятью порядка.
- удаление значений происходит так же быстрее.
- взятие по ключу практически одинаковое.
Вывод: использование словаря с памятью порядка (OrderedDict) в Python версии выше 3.6 не имеет смысла. Так как после 
этой версии словари по умолчанию упорядочные и отрабатывают быстрее.
Скорость наполнения простого словаря
 6.8099888470000005
Скорость наполнения словаря с памятью порядка элементов
 9.567274791
Скорость взятия пар простого словаря
 5.136048624000001
Скорость взятия пар словаря с памятью порядка элементов
 5.174831221000002
         800007 function calls in 0.291 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.291    0.291 <string>:1(<module>)
        1    0.066    0.066    0.066    0.066 task_4.py:20(make_dict)
        1    0.072    0.072    0.128    0.128 task_4.py:32(del_half_dict)
        1    0.064    0.064    0.094    0.094 task_4.py:47(take_items_dict)
        1    0.004    0.004    0.291    0.291 task_4.py:60(main_simp)
        1    0.000    0.000    0.291    0.291 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   300000    0.030    0.000    0.030    0.000 {method 'get' of 'dict' objects}
   500000    0.056    0.000    0.056    0.000 {method 'pop' of 'dict' objects}


         800007 function calls in 0.409 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.409    0.409 <string>:1(<module>)
        1    0.096    0.096    0.096    0.096 task_4.py:20(make_dict)
        1    0.079    0.079    0.217    0.217 task_4.py:32(del_half_dict)
        1    0.063    0.063    0.092    0.092 task_4.py:47(take_items_dict)
        1    0.004    0.004    0.409    0.409 task_4.py:66(main_ord)
        1    0.000    0.000    0.409    0.409 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   300000    0.029    0.000    0.029    0.000 {method 'get' of 'dict' objects}
   500000    0.138    0.000    0.138    0.000 {method 'pop' of 'collections.OrderedDict' objects}

"""
