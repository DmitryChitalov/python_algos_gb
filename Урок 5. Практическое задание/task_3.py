"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует действительности.
"""

import time
from collections import deque


def benchmark(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return res

    return wrapper


@benchmark
def init_list():
    lst = []
    for i in range(1000):
        lst.append(i)
    return lst


@benchmark
def init_deque():
    deq = deque()
    for i in range(1000):
        deq.append(i)
    return deq


@benchmark
def append_to_list(lst):
    for i in range(len(lst), len(lst) + 1000):
        lst.append(i)


@benchmark
def append_to_deque(deq):
    for i in range(1000, 2000):
        deq.append(i)


@benchmark
def append_left_to_list(lst):
    lst.insert(0, 5)


@benchmark
def append_left_to_deque(deq):
    deq.appendleft(5)


@benchmark
def insert_to_list(lst):
    lst.insert(0, 30)


@benchmark
def insert_to_deque(deq):
    deq.insert(0, 30)


@benchmark
def pop_from_list(lst):
    return lst.pop()


@benchmark
def pop_from_deque(deq):
    return deq.pop()


@benchmark
def popleft_from_list(lst):
    return lst.pop(0)


@benchmark
def popleft_from_deque(deq):
    return deq.popleft()


@benchmark
def get_from_list_by_index(lst):
    return lst[10]


@benchmark
def get_from_deque_by_index(deq):
    return deq[10]


@benchmark
def extend_left_list(extend_lst):
    lst = []
    for el in extend_lst:
        lst.insert(0, el)


@benchmark
def extend_left_deque(extend_lst):
    deq = deque()
    return deq.extendleft(extend_lst)


@benchmark
def reverse_list(lst):
    lst.reverse()


@benchmark
def reverse_deque(deq):
    deq.reverse()


list = init_list()
deq = init_deque()
append_to_list(list)
append_to_deque(deq)
append_left_to_list(list)
append_left_to_deque(deq)
insert_to_list(list)
insert_to_deque(deq)
extend_left_list(list)
extend_left_deque(list)
reverse_list(list)
reverse_deque(deq)
list_el = pop_from_list(list)
dict_el = pop_from_deque(deq)
list_el1 = popleft_from_list(list)
dict_el1 = popleft_from_deque(deq)
list_el_indexed = get_from_list_by_index(list)
dict_el_indexed = get_from_deque_by_index(deq)

"""
init_list 8.0108642578125e-05
init_deque 8.20159912109375e-05

append_to_list 0.0001010894775390625
append_to_deque 9.298324584960938e-05

append_left_to_list 1.6689300537109375e-06
append_left_to_deque 3.814697265625e-06

insert_to_list 9.5367431640625e-07
insert_to_deque 2.1457672119140625e-06

extend_left_list 0.000965118408203125
extend_left_deque 2.5987625122070312e-05

reverse_list 2.1457672119140625e-06
reverse_deque 2.86102294921875e-06

pop_from_list 1.1920928955078125e-06
pop_from_deque 1.1920928955078125e-06

popleft_from_list 1.1920928955078125e-06
popleft_from_deque 1.1920928955078125e-06

get_from_list_by_index 1.1920928955078125e-06
get_from_deque_by_index 1.1920928955078125e-06

Как мы видим на примере, все операции с deque быстрее, чем операции с list, 
кроме операций append - они примерно одинаковы по времени.
Сильно выигрывают по времени операции по вставке/выборке элементов слева (appendleft/extendleft/popleft)
"""
