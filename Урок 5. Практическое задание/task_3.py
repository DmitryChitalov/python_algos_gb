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

num_list = []
num_deque = deque()


def add_list_r(el):
    for i in range(el):
        num_list.append(i)


def add_deque_r(el):
    for i in range(el):
        num_deque.append(i)


def add_list_l(el):
    for i in range(el):
        num_list.insert(0, el)


def add_deque_l(el):
    for i in range(el):
        num_deque.appendleft(el)


def pop_list_r(el):
    for i in range(el//2):
        num_list.pop()


def pop_deque_r(el):
    for i in range(el//2):
        num_deque.pop()


def pop_list_l(el):
    for i in range(el//2):
        num_list.pop(0)


def pop_deque_l(el):
    for i in range(el//2):
        num_deque.popleft()


def fast_access_list(el):
    return num_list[el-1]


def fast_access_deque(el):
    return num_deque[el-1]


n = 1000
print('добавление list в конец',
      timeit('add_list_r(n)', 'from __main__ import add_list_r, n', number=1000))
print('добавление deque в конец',
      timeit('add_deque_r(n)', 'from __main__ import add_deque_r, n', number=1000))
print('добавление list в начало',
      timeit('add_list_l(n)', 'from __main__ import add_list_l, n', number=10))
print('добавление deque в начало',
      timeit('add_deque_l(n)', 'from __main__ import add_deque_l, n', number=10))
print('Поиск элемента в list',
      timeit('fast_access_list(n)', 'from __main__ import fast_access_list, n', number=10000000))
print('Поиск элемента в  deque ',
      timeit('fast_access_deque(n)', 'from __main__ import fast_access_deque, n', number=10000000))
print('возврат list последнего элемента',
      timeit('pop_list_r(n)', 'from __main__ import pop_list_r, n', number=1000))
print('возврат deque последнего элемента',
      timeit('pop_deque_r(n)', 'from __main__ import pop_deque_r, n', number=1000))
print('возврат list первого элемента',
      timeit('pop_list_l(n)', 'from __main__ import pop_list_l, n', number=1000))
print('возврат deque первого элемента',
      timeit('pop_deque_l(n)', 'from __main__ import pop_deque_l, n', number=1000))

"""
Вывод: 
добавление list в конец 0.12483949999999999
добавление deque в конец 0.10220700000000002
добавление list в начало 4.881513
добавление deque в начало 0.0009841999999995465
Поиск элемента в list 1.8777051
Поиск элемента в  deque  2.0252953
возврат list последнего элемента 0.06877420000000001
возврат deque последнего элемента 0.05649499999999996
возврат list первого элемента 15.7537776
возврат deque первого элемента 0.04746399999999795

Как мы видим по возврату им удалению deque работает быстрее,
особенно это видно при добавлении в начало и возврата элемента с начала.
При поиске элемента по индексу, немного выигрывает list 
"""