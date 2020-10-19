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

from random import randint
from timeit import timeit
from collections import deque

lst = [randint(0, 100) for i in range(10)]
dq = deque(lst)
print(lst)
print(dq)


def append_lst():
    return lst.append(10)


def pop_lst():
    return lst.pop(5)


def append_dq():
    return dq.append(6)


def appendleft_dq():
    return dq.appendleft(4)


def pop_dq():
    return dq.pop()


def popleft_dq():
    return dq.popleft()


print(f"append для списка: "
      f"{timeit('append_lst()', setup='from __main__ import append_lst', number=100000)}")
print(f"append для дека: "
      f"{timeit('append_dq()', setup='from __main__ import append_dq', number=100000)}")
print(f"appendleft для дека: "
      f"{timeit('appendleft_dq()', setup='from __main__ import appendleft_dq', number=100000)}")
print(f"pop для списка: "
      f"{timeit('pop_lst()', setup='from __main__ import pop_lst', number=100000)}")
print(f"pop для дека: "
      f"{timeit('pop_dq()', setup='from __main__ import pop_dq', number=100000)}")
print(f"popleft для дека: "
      f"{timeit('popleft_dq()', setup='from __main__ import popleft_dq', number=100000)}")

'''
append и appendleft для дека работает быстрее чем append для списка.
pop и popleft для дека по скорости значительно превосходит pop по индексу для списка. 
Следовательно, правило из документации верно. 
Если вам нужно дописать или удалить элемент из начала или конца - то использовать дек будет значительно быстрее. 
Если нужно обращение к определенному элементу списка - то необходимо использовать список.
'''
