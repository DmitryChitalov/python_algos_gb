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
import timeit
from collections import deque

x = [i for i in range(1000)]

lst = [x]

new_deque = deque(x)


def lst_ins(lst):
    return lst.insert(0, x)


def deque_add(new_deque):
    return new_deque.appendleft(x)


def lst_switch(lst):
    lst_rotate = lst[-1], lst[0] = lst[0], lst[-1]
    return lst_rotate


def deque_rotate(new_deque):
    return new_deque.rotate(1)


print(timeit.timeit('lst_ins(lst)', setup='from __main__ import lst_ins, x, lst',
                    number=1000))

print(timeit.timeit('deque_add(new_deque)', setup='from __main__ import deque_add, x, new_deque',
                    number=1000))

print(timeit.timeit('lst_switch(lst)', setup='from __main__ import lst_switch, x, lst',
                    number=1000))
print(timeit.timeit('deque_rotate(new_deque)', setup='from __main__ import deque_rotate, x, new_deque',
                    number=1000))

"""
Рузультаты замеров:
0.0004191000000000056 list
0.00017833200000000327 deque
0.00030534399999999906 list
0.00021382699999999977 deque

Информация соответствует диствительность.
"""
