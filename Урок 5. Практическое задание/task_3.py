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

some_list = [i for i in range(1000)]
some_deque = deque(some_list)

n = 'some_value'


def deque_append():
    some_deque.append(n)
    return

def list_append():
    some_list.append(n)
    return

def deque_appendleft():
    some_deque.appendleft(n)
    return

def list_insert():
    some_list.insert(0, n)
    return

def deque_count():
    some_deque.count(n)
    return

def list_count():
    some_list.count(n)
    return

def deque_extend():
    some_deque.extend(some_list)
    return

def list_extend():
    some_list.extend(some_list)
    return

def deque_extendleft():
    some_deque.extendleft(some_list)
    return

def list_insert_left():
    some_list.insert(0, some_list)
    return

def deque_pop():
    some_deque.pop()
    return

def list_pop():
    some_list.pop()
    return


# print(f'deque_append {timeit("deque_append()", globals=globals(), number=10000)}')
# print(f'list_append {timeit("list_append()", globals=globals(), number=10000)}')
# print(f'deque_appendleft {timeit("deque_appendleft()", globals=globals(), number=10000)}')
# print(f'list_insert {timeit("list_insert()", globals=globals(), number=10000)}')
# print(f'deque_count {timeit("deque_count()", globals=globals(), number=10000)}')
# print(f'list_count {timeit("list_count()", globals=globals(), number=10000)}')
# print(f'deque_extend {timeit("deque_extend()", globals=globals(), number=10000)}')
# print(f'list_extend {timeit("list_extend()", globals=globals(), number=10000)}')
# print(f'deque_extendleft {timeit("deque_extendleft()", globals=globals(), number=10000)}')
# print(f'list_insert_left {timeit("list_insert_left()", globals=globals(), number=10000)}')
# print(f'deque_pop {timeit("deque_pop()", globals=globals(), number=10000)}')
# print(f'list_pop {timeit("list_pop()", globals=globals(), number=10000)}')

"""
#операции append одинаковы по скорости
deque_append 0.1818087
list_append 0.1742751 
#insert в начало  deque значительно быстрее
deque_appendleft 0.0017440000000000025
list_insert 0.0673282
# count одинаково
deque_count 0.2682112
list_count 0.26362430000000003
# extend одинаково
deque_extend 1.3002903000000001
list_extend 1.2122333000000001
#вставка в начало списка почти одинаково
deque_extendleft 1.2730537000000002
list_insert_left 0.10146809999999995
#pop одинаково
deque_pop 0.0015994999999993098
list_pop 0.001759500000000358
"""
