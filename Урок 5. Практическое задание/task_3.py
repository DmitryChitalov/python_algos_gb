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

import collections
import timeit


def l():
    ll = list()

    for i in range(1000):
        ll.append(chr(i))
    return ll


a = l()


def dq():
    dq = collections.deque()

    for i in range(1000):
        dq.append(chr(i))
    return dq


b = dq()


def access_elem(z, n):
    return z[n]


print('List time spent for insertion: ')
print(timeit.timeit("l()", globals=globals(), number=10000))
print('Deque timespent for insertion: ')
print(timeit.timeit("dq()", globals=globals(), number=10000))
print('List time spent for access: ')
print(timeit.timeit("access_elem(a,458)", globals=globals(), number=100000))
print('Deque time spent for access: ')
print(timeit.timeit("access_elem(b,458)", globals=globals(), number=100000))

"""
List time spent for insertion: 
0.9036715999999999
Deque timespent for insertion: 
0.8824223999999999
List time spent for access: 
0.00638200000000011
Deque time spent for access: 
0.013105200000000039

deque быстрее списка в случае наполнения, а 
список быстрее deque в случае доступа к элементам.
"""