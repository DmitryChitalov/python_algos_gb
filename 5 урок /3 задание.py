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

dec = deque([])
list = []
list_n = [1, 2, 3, 4, 5]
n = 12345
i = 10000 # количество повторений для замеров

def deq_append():
    dec.append(n)
    return
def list_append():
    list.append(n)
    return
def deq_appendleft():
    dec.appendleft(n)
    return
def list_insert():
    list.insert(0, n)
    return
def deq_count():
    dec.count(n)
    return
def list_count():
    list.count(n)
    return

def deq_extend():
    dec.extend(list_n)
    return
def list_extend():
    list.extend(list_n)
    return
def deq_extendleft():
    dec.extendleft(list_n)
    return
def list_insert_left():
    list.insert(0, list_n)
    return
def deq_pop():
    dec.pop()
    return
def list_pop():
    list.pop()
    return

print(f'deq_append - {timeit("deq_append()", setup = "from __main__ import deq_append", number = i)}')
print(f'list_append - {timeit("list_append()", setup = "from __main__ import list_append", number = i)}')
# Время работы одинаковое при любых нагрузках
print(f'deq_appendleft - {timeit("deq_appendleft()", setup = "from __main__ import deq_appendleft", number = i)}')
print(f'list_insert - {timeit("list_insert()", setup = "from __main__ import list_insert", number = i)}')
# Вставка в начало списка значительно проигрывает deque
print(f'deq_count - {timeit("deq_count()", setup = "from __main__ import deq_count", number = i)}')
print(f'list_count - {timeit("list_count()", setup = "from __main__ import list_count", number = i)}')
# На больших нагрузках подсчет в списке быстрее чем в deque
print(f'deq_extend - {timeit("deq_extend()", setup = "from __main__ import deq_extend", number = i)}')
print(f'list_extend - {timeit("list_extend()", setup = "from __main__ import list_extend", number = i)}')
# Затраченое время примерно одинаково
print(f'deq_extendleft - {timeit("deq_extendleft()", setup = "from __main__ import deq_extendleft", number = i)}')
print(f'list_insert_left - {timeit("list_insert_left()", setup = "from __main__ import list_insert_left", number = i)}')
# Вставка в начало списка значительно проигрывает deque
print(f'deq_pop - {timeit("deq_pop()", setup = "from __main__ import deq_pop", number = i)}')
print(f'list_pop - {timeit("list_pop()", setup = "from __main__ import list_pop", number = i)}')
# Затраченое время примерно одинаково