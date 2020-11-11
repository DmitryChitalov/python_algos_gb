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

def list_append(el):
    my_list = []
    for i in range(el):
        my_list.append(i)
    return my_list

def list_insert(el):
    my_list = []
    for i in range(el):
        my_list.insert(0, i)
    return my_list

def list_reverse(cur_list):
    new_list = reversed(cur_list)
    return list(new_list)

def list_remove(cur_list, el):
    new_list = cur_list.remove(el)
    return new_list

def deque_append(el):
    my_deque = deque()
    for i in range(el):
        my_deque.append(i)
    return my_deque

def deque_appendleft(el):
    my_deque = deque()
    for i in range(el):
        my_deque.appendleft(i)
    return my_deque

def deque_reverse(cur_deque):
    new_deque = reversed(cur_deque)
    return list(new_deque)

def deque_remove(cur_deque, el):
    new_deque = cur_deque.remove(el)
    return new_deque

print('Функция list_append(100)')
list_ap_100 = list_append(100)
print(
    timeit(
        "list_append(100)",
        setup='from __main__ import list_append, list_ap_100',
        number=10000))

print('Функция list_append(1000)')
list_ap_1000 = list_append(1000)
print(
    timeit(
        "list_append(1000)",
        setup='from __main__ import list_append, list_ap_1000',
        number=10000))

print('Функция list_append(10000)')
list_ap_10000 = list_append(10000)
print(
    timeit(
        "list_append(10000)",
        setup='from __main__ import list_append, list_ap_10000',
        number=10000))

print('Функция deque_append(100)')
deque_ap_100 = deque_append(100)
print(
    timeit(
        "deque_append(100)",
        setup='from __main__ import deque_append, deque_ap_100',
        number=10000))

print('Функция deque_append(1000)')
deque_ap_1000 = deque_append(1000)
print(
    timeit(
        "deque_append(1000)",
        setup='from __main__ import deque_append, deque_ap_1000',
        number=10000))

print('Функция deque_append(10000)')
deque_ap_10000 = deque_append(10000)
print(
    timeit(
        "deque_append(10000)",
        setup='from __main__ import deque_append, deque_ap_10000',
        number=10000))

print('Функция list_insert(100)')
list_in_100 = list_insert(100)
print(
    timeit(
        "list_insert(100)",
        setup='from __main__ import list_insert, list_in_100',
        number=10000))

print('Функция list_insert(1000)')
list_in_1000 = list_insert(1000)
print(
    timeit(
        "list_insert(1000)",
        setup='from __main__ import list_insert, list_in_1000',
        number=10000))

print('Функция deque_appendleft(100)')
deque_in_100 = deque_appendleft(100)
print(
    timeit(
        "deque_appendleft(100)",
        setup='from __main__ import deque_appendleft, deque_in_100',
        number=10000))

print('Функция deque_appendleft(1000)')
deque_in_1000 = deque_appendleft(1000)
print(
    timeit(
        "deque_appendleft(1000)",
        setup='from __main__ import deque_appendleft, deque_in_1000',
        number=10000))

print(type(list_ap_100))
print(list_ap_100)
print(type(deque_ap_100))
print(list_ap_100)
print(deque_ap_100)


# print('Функция list_reverse(list_100)')
# reverse_list_100 = list_reverse(list_ap_100)
# print(
#     timeit(
#         "list_reverse(list_ap_100)",
#         setup='from __main__ import list_reverse, reverse_list_100',
#         number=10000))


#
# print('Функция deque_reverse(deque_100)')
# reverse_dq_100 = deque_reverse(deque_ap_100)
# print(
#     timeit(
#         "deque_reverse(deque_ap_100)",
#         setup='from __main__ import deque_reverse, reverse_dq_100',
#         number=10000))

# print('Функция list_remove(list_1000, 500)')
# remove_1000 = list_remove(list_ap_1000, 500)
# print(
#     timeit(
#         "list_remove(list_ap_1000, 500)",
#         setup='from __main__ import list_remove, remove_1000',
#         number=10000))
#
# print('Функция deque_remove(deque_1000, 500)')
# remove_1000 = deque_remove(deque_ap_1000, 500)
# print(
#     timeit(
#         "deque_remove(deque_ap_1000, 500)",
#         setup='from __main__ import deque_remove, remove_1000',
#         number=10000))

'''
Функция list_append(100) - 0.5233599580000001
Функция list_append(1000) - 3.6622010449999998
Функция list_append(10000) - 21.614685574
Функция deque_append(100) - 0.1320028769999979
Функция deque_append(1000) - 0.976176487
Функция deque_append(10000) - 12.033188386000003
Функция list_insert(100) - 0.3066541210000011
Функция list_insert(1000) - 9.186634779999999
Функция deque_appendleft(100) - 0.13550953700000434
Функция deque_appendleft(1000) - 1.3027727949999957

Очевидно, что одинакового фукнционала действия производятся быстрее с объектом класса deque

Единственное, возникла проблема с выполнением reverse, remove
'''