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
import string

num = 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51
lst = list(num)
dqe = deque(num)

new_dqe = deque(string.ascii_uppercase)
new_lst = list(string.ascii_uppercase)
# проведены замеры каждого действия с списком и декой, содержащими как цифровые значения, так и строковые
# разницы во времени при цировых и строковых значениях не было,
# но при работе с декой почти все операции проходили в 2 раза быстрее, чем со списком

# функция реализует вставку в список в начало и в конец


def lst_appender(l):
    l.insert(0, 'start')
    l.append('end')
    return l

# функция реализует вставку в деку в начало и в конец


def dqe_appender(d):
    d.appendleft('start')
    d.append('end')
    return d

# функция реализует удаление из списка в начале и в конце


def lst_remover(l):
    for el in l[0:1]:
        l.remove(el)

    l.pop()
    return l

# функция реализует удаление из деки в начале и в конце


def dqe_remover(d):
    d.popleft()
    d.pop()
    return d

# функция реализует перемещение последних двух элементов из списка в начало


def lst_rotator(l):
    l.insert(0, l[-1])
    l.pop()
    l.insert(0, l[-1])
    l.pop()
    return l

# функция реализует перемещение последних двух элементов из деки в начало


def dqe_rotator(d):
    d.rotate(2)
    return d


print(lst_appender(lst))
print(dqe_appender(dqe))
print(lst_appender(new_lst))
print(dqe_appender(new_dqe))
print(lst_remover(lst))
print(dqe_remover(dqe))
print(lst_remover(new_lst))
print(dqe_remover(new_dqe))
print(lst_rotator(lst))
print(dqe_rotator(dqe))
print(lst_rotator(new_lst))
print(dqe_rotator(new_dqe))


print('lst_appender + lst', timeit("lst_appender(lst)",
                                   setup="from __main__ import lst_appender, lst", number=1000))
print('dqe_appender + dqe', timeit("dqe_appender(dqe)",
                                   setup="from __main__ import dqe_appender, dqe", number=1000))
print('lst_appender + new_lst', timeit("lst_appender(new_lst)",
                                       setup="from __main__ import lst_appender, new_lst", number=1000))
print('dqe_appender + dqe', timeit("dqe_appender(new_dqe)",
                                   setup="from __main__ import dqe_appender, new_dqe", number=1000))
print('lst_remover + lst', timeit("lst_remover(lst)",
                                  setup="from __main__ import lst_remover, lst", number=1000))
print('dqe_remover + dqe', timeit("dqe_remover(dqe)",
                                  setup="from __main__ import dqe_remover, dqe", number=1000))
print('lst_remover + new_lst', timeit("lst_remover(new_lst)",
                                      setup="from __main__ import lst_remover, new_lst", number=1000))
print('dqe_remover + new_dqe', timeit("dqe_remover(new_dqe)",
                                      setup="from __main__ import dqe_remover, new_dqe", number=1000))
print('lst_rotator + lst', timeit("lst_rotator(lst)",
                                  setup="from __main__ import lst_rotator, lst", number=1000))
print('dqe_rotator + dqe', timeit("dqe_rotator(dqe)",
                                  setup="from __main__ import dqe_rotator, dqe", number=1000))
print('lst_rotator + new_lst', timeit("lst_rotator(new_lst)",
                                      setup="from __main__ import lst_rotator, new_lst", number=1000))
print('dqe_remover + new_dqe', timeit("dqe_rotator(new_dqe)",
                                      setup="from __main__ import dqe_rotator, new_dqe", number=1000))
