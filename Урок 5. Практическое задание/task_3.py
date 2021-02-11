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
my_list = [el for el in range(n)]
my_deque = deque(my_list)


# добавим элемент в конец очереди
def list_add():
    my_list.append('e')


def deque_add():
    my_deque.append('e')


# добавим элемент в начало очереди. а почему не insert?
def deque_add_left():
    my_deque.appendleft('a')


def list_add_left():
    global my_list
    my_list = ['a'] + my_list


# pop также работает с обоих концов
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
Добавление через list:  0.006255299999999998
Добавление через deque:  0.006570899999999998
Добавление слева через list:  5.0222851
Добавление слева через deque:  0.006487199999999582
Удаление через list:  0.005893499999999996
Удаление через deque:  0.005919399999999797
Удаление слева через list:  2.6830217999999997
Удаление слева через deque:  0.005774800000000191

Добавление и удаление из дека и списка не очень отличаются в замерах, 
пока дело не коснется добавления или удаления слева.
Вот тут дека быстрее в разы

"""
