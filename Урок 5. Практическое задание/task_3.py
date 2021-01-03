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
from random import randint
from timeit import timeit


def fill_list(quantity):
    my_list = []
    for i in range(quantity):
        my_list.append(randint(0, 5))
    return my_list


def fill_deque(quantity):
    my_deque = deque()
    for i in range(quantity):
        my_deque.append(randint(0, 5))
    return my_deque


def pop_list_el(my_list):
    my_list.pop()
    return my_list


def pop_deque_el(my_deque):
    my_deque.pop()
    return my_deque


def rand_list_el(my_list):
    x = my_list[randint(0, len(my_list)-1)]
    return x


def rand_deque_el(my_deque):
    x = my_deque[randint(0, len(my_deque)-1)]
    return x


quantity = 100
my_list = fill_list(1000)
my_deque = fill_deque(1000)

print(timeit("fill_list(quantity)", setup="from __main__ import fill_list, quantity", number=1000))
print(timeit("fill_deque(quantity)", setup="from __main__ import fill_deque, quantity", number=1000))
print(timeit("rand_list_el(my_list)", setup="from __main__ import rand_list_el, my_list", number=1000))
print(timeit("rand_deque_el(my_deque)", setup="from __main__ import rand_deque_el, my_deque", number=1000))
print(timeit("pop_list_el(my_list)", setup="from __main__ import pop_list_el, my_list", number=1000))
print(timeit("pop_deque_el(my_deque)", setup="from __main__ import pop_deque_el, my_deque", number=1000))

"""
Время заполнение дека при помощи .append() несколько меньше времени заполнения списка, что соответствует информации в
документации:
fill_list:  0.0670323
fill_deque: 0.0655105

Время доступа к случайному элементу дека больше относительно времени доступа к случайному элементу
списка, что соответствует информации в документации:
rand_list_el:  0.00079
rand_deque_el: 0.00083

Время удаления элемента с помощью .pop() меньше в случае с деком, что соответствует информации в документации:
pop_list_el:    9.419999999998874e-05
pop_deque_el:   8.890000000000287e-05


"""
