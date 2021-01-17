"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""
from timeit import timeit
from collections import deque


def func_list_insert(lst):          # Добавление в list элементов слева
    for i in range(1000):
        lst.insert(0, i)
    return lst


def func_list_append(lst):          # Добавление в list элементов справа
    for i in range(1000):
        lst.append(i)
    return lst


def func_deque_appendleft(deq):     # Добавление в deque элементов слева
    for i in range(1000):
        deq.appendleft(i)
    return deq


def func_deque_append(deq):         # Добавление в deque элементов справа
    for i in range(1000):
        deq.append(i)
    return deq


def func_list_cycle(lst):           # перебор всех элементов из list и добавление их в новый list
    res = []
    for el in lst:
        res.append(el)
    return res


def func_deque_cycle(deq):          # перебор всех элементов из deque и добавление их в новый deque/list
    # res = []                      # добавление в list
    res = deque(list())             # добавление в deque
    for el in deq:
        res.append(el)
    return res


lst_work = [range(1, 101)]
new_deque = deque(lst_work)

time_1 = timeit('func_list_insert(lst_work)',
                setup='from __main__ import func_list_insert, lst_work', number=100)
time_2 = timeit('func_list_append(lst_work)',
                setup='from __main__ import func_list_append, lst_work', number=100)
time_3 = timeit('func_deque_appendleft(new_deque)',
                setup='from __main__ import func_deque_appendleft, new_deque', number=100)
time_4 = timeit('func_deque_append(new_deque)',
                setup='from __main__ import func_deque_append, new_deque', number=100)
time_5 = timeit('func_list_cycle(lst_work)',
                setup='from __main__ import func_list_cycle, lst_work', number=100)
time_6 = timeit('func_deque_cycle(new_deque)',
                setup='from __main__ import func_deque_cycle, new_deque', number=100)

print('Время добавления элементов в начало list: {:.2f}'.format(time_1))
print('Время добавления элементов в начало deque: {:.2f}'.format(time_3))

print('\nВремя добавления элементов в конец list: {:.2f}'.format(time_2))
print('Время добавления элементов в конец deque: {:.2f}'.format(time_4))

print('\nВремя выполнения цикла в list: {:.2f}'.format(time_5))
print('Время выполнения цикла в deque: {:.2f}'.format(time_6))

"""Выводы: выполнение функции добавления элементов в начало простого списка (func_list_insert)
   занимает гораздо больше времени, нежели аналогичная функция (func_deque_appendleft), 
   использующая оптимизированный список deque (что и следовало ожидать).
   
   Операции добавления элементов в конец простого или оптимизированного списка deque занимают
   относительно одно и то же время.
   
   Время выполнения цикла перебора всех элементов list и поочередное добавление каждого этого
   элемента в новый list (res) занимает немного больше времени, чем аналогичный перебор элементов
   оптимизированного списка deque с добавлением этих элементов в новый список deque (res).
   Но если добавлять элементы из deque в обычный list, то время выполнения такое же как из list в list"""
