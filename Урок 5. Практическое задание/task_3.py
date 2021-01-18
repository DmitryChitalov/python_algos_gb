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

n = range(50)
my_list = list(n)
my_deque = deque(n)


def create_lst():
    my_list = list(n)
    return my_list


def create_deq():
    my_deque = deque(n)
    return my_deque


def insert_lst():
    my_list.insert(0, 'num')
    return my_list


def ap_lft_deq():
    my_deque.appendleft('num')
    return my_deque


def ext_lst():
    my_list.extend('add')
    return my_list


def ext_deq():
    my_deque.extend('add')
    return my_deque


def rev_lst():
    my_list.reverse()
    return my_list


def rev_deq():
    my_deque.reverse()
    return my_deque


def poplf_lst():
    my_list.pop(0)
    return my_list


def poplf_deq():
    my_deque.popleft()
    return my_deque


## Создание списка и очереди
print(
    timeit.timeit(
        "create_lst()", setup="from __main__ import create_lst",
        number=10000))  ## 0.01072552299592644
print(
    timeit.timeit(
        "create_deq()", setup="from __main__ import create_deq",
        number=10000))  ## 0.011986394005361944

print('#################################')
##Добавление элемента в начало списка и очереди

print(
    timeit.timeit(
        "insert_lst()", setup="from __main__ import insert_lst",
        number=10000))  ## 0.028336001007119194
print(
    timeit.timeit(
        "ap_lft_deq()", setup="from __main__ import ap_lft_deq",
        number=10000))  ## 0.003973811995820142

print('#################################')
##Добавление элементов в конец списка и очереди

print(
    timeit.timeit(
        "ext_lst()", setup="from __main__ import ext_lst",
        number=10000))  ## 0.007913456996902823
print(
    timeit.timeit(
        "ext_deq()", setup="from __main__ import ext_deq",
        number=10000))  ## 0.007576081989100203

print('#################################')
##Реверс списка и очереди

print(
    timeit.timeit(
        "rev_lst()", setup="from __main__ import rev_lst",
        number=10000))  ## 0.8635506369901123
print(
    timeit.timeit(
        "rev_deq()", setup="from __main__ import rev_deq",
        number=10000))  ## 1.0032881619990803

print('#################################')
##Удаление элементов сначала списка и очереди

print(
    timeit.timeit(
        "poplf_lst()", setup="from __main__ import poplf_lst",
        number=10000))  ##0.1499738230049843
print(
    timeit.timeit(
        "poplf_deq()", setup="from __main__ import poplf_deq",
        number=10000))  ## 0.0037691659963456914
"""
Из результатов видно, что методы удаления, вставки сначала очереди работают быстрее списка. 
Остальные идентичные методы работают примерно одинаково.
Однако реверс списка получается быстрее по времени чем реверс очереди.
В целом, применять очередь полезно, зная подходящие методы как ускорить выполнение программы. 
"""
