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

num = int(input('Введите число'))
list_example = [i for i in range(num)]
deque_list = deque(list_example)


def list_insert(list):
    list_example.insert(0, 'insert')
    return list_example


def deque_appl(list):
    deque_list.appendleft('insert')
    return deque_list


def list_pop(lst):
    lst.pop()
    return lst


def deque_poplf(d_lst):
    d_lst.poplest()
    return(d_lst)


print("добавим элемент в конец очереди")
print(timeit("list_example.append('append')",
             setup="from __main__ import list_example"))

print(timeit('deque_list.append("append")',
             setup='from __main__ import deque_list'))


print('добавим элемент в начало очереди')
print(timeit("list_insert(list_example)",
             setup="from __main__ import list_insert,list_example"))

print(timeit('deque_appl(deque_example)',
             setup='from __main__ import deque_appl,deque_example'))


print(timeit("list_pop(list_example)",
             setup="from __main__ import list_pop,list_example", number=1000))
print(timeit("deque_poplf(deque_example)",
             setup="from __main__ import deque_poplf,deque_example", number=1000))


""" 0.0793550999999999 фунцкия Deque отрабатывает быстрее
0.0673366999999998"""
