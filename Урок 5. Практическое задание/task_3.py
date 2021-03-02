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
from random import randint
from timeit import timeit

easy_list=[]
easy_deq=deque()
example_list=[randint(el,el*el) for el in range(100)]

def chck_append_list():
    for i in range(len(example_list)):
        easy_list.append(example_list[i])
    return

def chck_append_deque():
    for i in range(len(example_list)):
        easy_deq.append(example_list[i])
    return

def chck_append_left_list():
    for i in range(len(example_list)):
        easy_list.insert(0,example_list[i])
    return

def chck_append_left_deq():
    for i in range(len(example_list)):
        easy_deq.appendleft(example_list[i])
    return

def chck_reverse_list():
    easy_list.reverse()
    return

def chck_reverse_deq():
    easy_deq.reverse()
    return

def chck_popleft_list():
    v_tmp=easy_list.pop(0)
    return

def chck_popleft_deq():
    v_tmp=easy_deq.popleft()
    return

def chck_sort_list():
    easy_list.sort()
    return

def chck_sort_deq():
    easy_list.sort()
    return

n_timeit=1000 # количество тестов для timeit
print("-------------- замеры --------------------------")

print("append")
print("chck_append_list", timeit('chck_append_list()', setup='from __main__ import chck_append_list', number=n_timeit))
print("chck_append_deque", timeit('chck_append_deque()', setup='from __main__ import chck_append_deque', number=n_timeit))

print("appendleft")
print("chck_append_left_list", timeit('chck_append_left_list()', setup='from __main__ import chck_append_left_list', number=n_timeit))
print("chck_append_left_deq", timeit('chck_append_left_deq()', setup='from __main__ import chck_append_left_deq', number=n_timeit))

print("reverse")
print("chck_reverse_list", timeit('chck_reverse_list()', setup='from __main__ import chck_reverse_list', number=n_timeit))
print("chck_reverse_deq", timeit('chck_reverse_deq()', setup='from __main__ import chck_reverse_deq', number=n_timeit))

print("popleft")
print("chck_popleft_list", timeit('chck_popleft_list()', setup='from __main__ import chck_popleft_list', number=n_timeit))
print("chck_popleft_deq", timeit('chck_popleft_deq()', setup='from __main__ import chck_popleft_deq', number=n_timeit))

print("sorted")
print("chck_sort_list", timeit('chck_sort_list()', setup='from __main__ import chck_sort_list', number=n_timeit))
print("chck_sort_deq", timeit('chck_sort_deq()', setup='from __main__ import chck_sort_deq', number=n_timeit))

"""
-------------- замеры --------------------------
append в конец очереди практически одинаковый для обоих типов
chck_append_list 0.014217299999999995
chck_append_deque 0.010905799999999993
appendleft добавление в начало очереди эффективнее для deque 
chck_append_left_list 12.2964183
chck_append_left_deq 0.014255199999999135
reverse  тоже получается быстрее для deque, т.к. используется добавление в начало
chck_reverse_list 0.12167230000000018
chck_reverse_deq 0.20938809999999997
popleft  тоже получается быстрее для deque
chck_popleft_list 0.09524950000000132
chck_popleft_deq 0.00014280000000077564
sorted практически одинаковые для обоих типов?
chck_sort_list 1.3808235999999994
chck_sort_deq 1.0944538000000001