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
from timeit import timeit
from collections import deque


def list_append():
    list_a = []
    for i in range(10000):
        list_a.append(i)

def deque_append():
    list_a = deque()
    for i in range(10000):
        list_a.append(i)

def list_appendleft():
    list_a = []
    for i in range(10000):
        list_a.insert(0, i)

def deque_appendleft():
    list_a = deque()
    for i in range(10000):
        list_a.appendleft(i)

def list_pop(test):
    list_a = test[:]
    for i in range(len(list_a)):
        a = list_a.pop()

def deque_pop(test_deque:deque):
    list_a = test_deque
    for i in range(len(list_a)):
        list_a.pop()

def list_popleft(test):
    list_a = test[:]
    for i in range(len(list_a)):
        list_a.pop(0)

def deque_popleft(test_deque):
    list_a = test_deque
    for i in range(len(list_a)):
        list_a.popleft()

def list_extend(test):
    list_a = []
    list_a.extend(test)

def deque_extend(test_deque):
    list_a = deque()
    list_a.extend(test_deque)

def list_extendleft(test):
    list_a = []
    for i in test:
        list_a.insert(0, i)

def deque_extendleft(test_deque):
    list_a = deque()
    list_a.extend(test_deque)

def list_reverse(test:list):
    list_a = test.reverse()

def deque_reverse(test_deque:deque):
    list_a = test_deque.reverse()


test_list = [el for el in range(10000)]
test_deque = deque()
test_deque.extend(test_list)

print('list_append', timeit("list_append", setup="from __main__ import list_append", number=100000))
print('deque_append', timeit("deque_append", setup="from __main__ import deque_append", number=100000))
print('list_appendleft', timeit("list_appendleft", setup="from __main__ import list_appendleft", number=100000))
print('deque_appendleft', timeit("deque_appendleft", setup="from __main__ import deque_appendleft", number=100000))
print('list_pop', timeit("list_pop(test_list)", setup="from __main__ import list_pop, test_list", number=1000))
print('deque_pop', timeit("deque_pop(test_deque)", setup="from __main__ import deque_pop, test_deque", number=1000))
print('list_popleft', timeit("list_popleft(test_list)", setup="from __main__ import list_popleft, test_list", number=1000))
print('deque_popleft', timeit("deque_popleft(test_deque)", setup="from __main__ import deque_popleft, test_deque", number=1000))
print('list_extend', timeit("list_extend(test_list)", setup="from __main__ import list_extend, test_list", number=10000))
print('deque_extend', timeit("deque_extend(test_deque)", setup="from __main__ import deque_extend, test_deque", number=10000))
print('list_extendleft', timeit("list_extendleft(test_list)", setup="from __main__ import list_extendleft, test_list", number=1000))
print('deque_extendleft', timeit("deque_extendleft(test_deque)", setup="from __main__ import deque_extendleft, test_deque", number=1000))
print('list_reverse', timeit("list_reverse(test_list)", setup="from __main__ import list_reverse, test_list", number=100000))
print('deque_reverse', timeit("deque_reverse(test_deque)", setup="from __main__ import deque_reverse, test_deque", number=100000))

'''
Долго подгонял number, так как работа по подсчету времени занимала много времени.
Deque очень удобный класс для работы для вставки чисел
'''