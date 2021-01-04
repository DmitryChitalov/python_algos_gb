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


user_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'a', 'b', 'c']
user_dq = deque(user_list)


def deq_appendleft():
    user_dq.appendleft('abc')
    return


def list_insert():
    user_list.insert(0, 'abc')
    return


def deq_popleft():
    user_dq.popleft()
    return


def list_pop():
    user_list.pop(0)
    return


def deq_append():
    user_dq.append('abc')
    return


def list_append():
    user_list.append('abc')
    return


print(timeit('deq_appendleft()', 'from __main__ import deq_appendleft', number=10000))  # 0.001188599999999998
print(timeit('list_insert()', 'from __main__ import list_insert', number=10000))        # 0.021667900000000004
print(timeit('deq_popleft()', 'from __main__ import deq_popleft', number=10000))        # 0.002824900000000005
print(timeit('list_pop()', 'from __main__ import list_pop', number=10000))              # 0.029200699999999996
print(timeit('deq_append()', 'from __main__ import deq_append', number=10000))          # 0.0012357000000000062
print(timeit('list_append()', 'from __main__ import list_append', number=10000))        # 0.001465999999999995

'''
При сравнении deque.appendleft() vs list.insert() и 
              deque.popleft() vs list.pop()
deque быстрее в 10 раз, так как сложность О(n) уступает О(1)

При сравнении аналогичных операций *.append() - разницы практически не наблюдается,
но deque показал себя быстрее, чем list на десятитысячную долю секунды на 10000 операций. 
'''