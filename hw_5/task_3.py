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

Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям

И добавить аналитику, так ли это или нет.!
"""
from collections import deque
from timeit import timeit

list_obj = list('example')
deq_obj = deque('example')


def list_ins_begin(letter):
    list_obj.insert(0, letter)


def deq_ins_begin(letter):
    deq_obj.appendleft(letter)


def list_ins_end(letter):
    list_obj.append(letter)


def deq_ins_end(letter):
    deq_obj.append(letter)


def list_pop_begin():
    list_obj.pop(0)


def deq_pop_begin():
    deq_obj.popleft()


def list_pop_end():
    list_obj.pop()


def deq_pop_end():
    deq_obj.pop()


print(timeit("list_ins_begin('t')", globals=globals(), number=1000))
print(timeit("deq_ins_begin('t')", globals=globals(), number=1000))
print(timeit("list_ins_end('t')", globals=globals(), number=1000))
print(timeit("deq_ins_end('t')", globals=globals(), number=1000))
print(timeit("list_pop_begin()", globals=globals(), number=1000))
print(timeit("deq_pop_begin()", globals=globals(), number=1000))
print(timeit("list_pop_end()", globals=globals(), number=1000))
print(timeit("deq_pop_end()", globals=globals(), number=1000))
'''
После профилирования получились следующие данные:
Вставка в начало:
list -  0.0002940000000000026 
deque - 0.00013780000000000042
Вставка в конец:
list -  0.0001344999999999992 
deque - 0.00013629999999999892
Удаление с начала:
list -  0.00022589999999999763 
deque - 0.00012539999999999774
Удаление с конца:
list -  0.00012839999999999727 
deque - 0.00013260000000000008
Отсюда вывод, что очередь оптимизирована на вставку и удаление, особенно с начала, поэтому
если надо много вставлять, удалять с начала или с конца, то очередь подходит лучше, если же
для рандомного доступа к данным, то список
'''