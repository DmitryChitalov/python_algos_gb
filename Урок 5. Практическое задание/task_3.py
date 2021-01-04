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

from collections import deque
from timeit import timeit

lst_lst = [i for i in range(10000)]
print(lst_lst)
lst_deque = deque(lst_lst)
print(lst_deque)


def lst_insert_append(lst):
    lst.insert(0, 'x')
    lst.append('y')
    return lst


def deque_append(dq):
    dq.appendleft('x')
    dq.append('y')
    return dq


def for_lst(lst):
    summ = 0
    for el in lst:
        summ += el
    return summ


def for_in_deque(dq):
    summ = 0
    for el in dq:
        summ += el
    return summ


print(timeit('lst_insert_append(lst_lst)', setup='from __main__ import lst_insert_append, lst_lst', number=100000),
      'обычный список - добавление')
print(timeit('deque_append(lst_deque)', setup='from __main__ import deque_append, lst_deque', number=100000),
      'deque - добавление')

lst_lst = [i for i in range(10000)]
lst_deque = deque(lst_lst)
print(timeit('for_lst(lst_lst)', setup='from __main__ import for_lst, lst_lst', number=100000),
      'нахождение суммы элементов списка')
print(timeit('for_in_deque(lst_deque)', setup='from __main__ import for_in_deque, lst_deque', number=100000),
      'нахождение суммы элементов deque')

"""
Результат для последовательности из 100 элементов:

13.6511396 обычный список - добавление
0.02032939999999961 deque - добавление
0.45412059999999954 нахождение суммы элементов списка
0.47147190000000094 нахождение суммы элементов deque

Результат для последовательности из 1000 элементов:

13.40347 обычный список - добавление
0.02163819999999994 deque - добавление
4.640474599999999 нахождение суммы элементов списка
5.1302667 нахождение суммы элементов deque

Результат для последовательности из 10000 элементов:

14.959522100000001 обычный список - добавление
0.021143699999999654 deque - добавление
47.1160596 нахождение суммы элементов списка
49.291678999999995 нахождение суммы элементов deque

Вывод: взятие/вставка элементов deque быстрее обычного списка,
        операции с элементами deque медленнее обычного списка
"""