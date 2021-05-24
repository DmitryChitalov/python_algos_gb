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

n = 20000
my_list = [element for element in range(n)]
my_deque = deque(my_list)


def list_add():
    my_list.append(1)


def deque_add():
    my_deque.append(1)


def deque_add_left():
    my_deque.appendleft(1)


def list_add_left():
    global my_list
    my_list = [1] + my_list


def deque_del():
    my_deque.pop()


def list_del():
    my_list.pop()


def deque_del_left():
    my_deque.popleft()


def list_del_left():
    global my_list
    my_list = my_list[1:]


print('Добавление через list: ',
      timeit("list_add()", setup="from __main__ import list_add", number=n))
print('Добавление через deque: ',
      timeit("deque_add()", setup="from __main__ import deque_add", number=n))
print('Добавление слева через list: ',
      timeit("list_add_left()", setup="from __main__ import list_add_left", number=n))
print('Добавление слева через deque: ',
      timeit("deque_add_left()", setup="from __main__ import deque_add_left", number=n))
print('Удаление через list: ',
      timeit("list_del()", setup="from __main__ import list_del", number=n))
print('Удаление через deque: ',
      timeit("deque_del()", setup="from __main__ import deque_del", number=n))
print('Удаление слева через list: ',
      timeit("list_del_left()", setup="from __main__ import list_del_left", number=n))
print('Удаление слева через deque: ',
      timeit("deque_del_left()", setup="from __main__ import deque_del_left", number=n))

"""
При обычном добавлении разница минимальная, но при удалении и добавлении слева разница становится существенной.
Добавление через list:  0.0026205
Добавление через deque:  0.0022240000000000003
Добавление слева через list:  3.5336189
Добавление слева через deque:  0.0023341000000001166
Удаление через list:  0.002456100000000294
Удаление через deque:  0.002163799999999938
Удаление слева через list:  1.7133153
Удаление слева через deque:  0.002170500000000075
"""
