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
import timeit
n = range(44)
test_list = list(n)
test_deque = deque(n)


def insert_lst():
    test_list.insert(0, 1)
    # print(test_list)
    return test_list


def aplft_deque():
    test_deque.appendleft(1)
    # print(test_deque)
    return test_deque


def ext_lst():
    test_list.extend('add')
    return test_list


def ext_deque():
    test_deque.extend('add')
    return test_deque


def rev_lst():
    test_list.reverse()
    return test_list


def rev_deque():
    test_deque.reverse()
    return test_deque


def popleft_lst():
    test_list.pop(0)
    return test_list


def popleft_deque():
    test_deque.popleft()
    return test_deque


print('Insert: list vs deque')
print(timeit.timeit("insert_lst()", setup="from __main__ import insert_lst", number=10000))
print(timeit.timeit("aplft_deque()", setup="from __main__ import aplft_deque", number=10000))

print('Extend: list vs deque')
print(timeit.timeit("ext_lst()", setup="from __main__ import ext_lst", number=10000))
print(timeit.timeit("ext_deque()", setup="from __main__ import ext_deque", number=10000))

print('Reverse: list vs deque')
print(timeit.timeit("rev_lst()", setup="from __main__ import rev_lst", number=10000))
print(timeit.timeit("rev_deque()", setup="from __main__ import rev_deque", number=10000))

print('Popleft: list vs deque')
print(timeit.timeit("popleft_lst()", setup="from __main__ import popleft_lst", number=10000))
print(timeit.timeit("popleft_deque()", setup="from __main__ import popleft_deque", number=10000))
"""
Insert: list vs deque
0.0186058
0.000878799999999999
Extend: list vs deque
0.0014797000000000005
0.001347999999999995
Reverse: list vs deque
0.1027634
0.2130216
Popleft: list vs deque
0.06185689999999999
0.0006583000000000006

Deques are a generalization of stacks and queues 
(the name is pronounced “deck” and is short for “double-ended queue”). 
Deques support thread-safe, memory efficient appends and pops from either 
side of the deque with approximately the same O(1) performance in either direction.
Though list objects support similar operations, they are optimized for fast 
fixed-length operations and incur O(n) memory movement costs for pop(0) and 
insert(0, v) operations which change both the size and position of the underlying
 data representation.
 
Очереди специально оптимизированы под методы append/pop. с англ не очень, но из результатов и плохонького перевода
  следует что методы pop/insert для list меняют размер и положение данных что и сказывается на времени выполнения
"""
