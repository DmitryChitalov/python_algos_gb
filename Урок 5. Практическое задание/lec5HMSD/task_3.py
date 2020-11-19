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
from random import randint

def list_append ():
    test_list.append(randint(0, 999))

def deque_append ():
    test_deque.append(randint(0, 999))

def list_extend ():
    temp_list = [randint(0, 999) for i in range(100)]
    test_list.extend (temp_list)

def deque_extend ():
    temp_deque = deque([randint(0, 999) for i in range(100)])
    test_deque.extend (temp_deque)

def list_reverse ():
    test_list.reverse()

def deque_reverse():
    test_deque.reverse()


col = 10000
test_list = [i for i in range(int(col / 10))]
test_deque = deque(test_list)

print(
    timeit(
        'list_append()',
        setup='from __main__ import list_append',
        number=col))

print(
    timeit(
        'deque_append()',
        setup='from __main__ import deque_append',
        number=col))

print(
    timeit(
        'list_extend()',
        setup='from __main__ import list_extend',
        number=col))

print(
    timeit(
        'deque_extend()',
        setup='from __main__ import deque_extend',
        number=col))

print(
    timeit(
        'list_reverse()',
        setup='from __main__ import list_reverse',
        number=col))

print(
    timeit(
        'deque_reverse()',
        setup='from __main__ import deque_reverse',
        number=col))


#0.011795199999999999
#0.0132262
#1.4884589
#1.3148309
#3.8714481999999997
#11.3820325

#Вывод. В базовых операциях deque быстрее работает на несколько процентов.
#Неожиданный был результат по Reverse - deque медленнее в несколько раз.