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
from random import randint


def remove_left_deque(deq, count=0):
    deq_fun = deq.copy()
    for i in range(count):
        deq_fun.popleft()
    return deq_fun


def remove_left_list(lst, count=0):
    lst_fun = lst.copy()
    for i in range(count):
        lst_fun.pop(0)
    return lst_fun


def revers_deque(deq):
    return deq.reverse()


def revers_list(lst):
    return lst.reverse()


def append_deque(deq):
    return deq.append(123)


def append_list(lst):
    return lst.append(123)


if __name__ == '__main__':
    lst_obj = [randint(0, 100) for i in range(100)]
    deq_obj = deque(lst_obj)

    print('Функция remove_left_deque: ', end='')
    print(
        timeit(
            'remove_left_deque(deq_obj, 50)', setup='from __main__ import remove_left_deque, deq_obj', number=1000000
        ))

    print('Функция remove_left_list:  ', end='')
    print(
        timeit(
            'remove_left_list(lst_obj, 50)', setup='from __main__ import remove_left_list, lst_obj', number=1000000
               ))

    print('Функция revers_deque:', end='')
    print(timeit(
        'revers_deque(deq_obj)', setup='from __main__ import revers_deque, deq_obj', number=1000000
    ))

    print('Функция revers_list:', end='')
    print(timeit(
        'revers_list(lst_obj)', setup='from __main__ import revers_list, lst_obj', number=1000000
    ))

    print('Функция append_deque:', end='')
    print(timeit(
        'append_deque(deq_obj)', setup='from __main__ import append_deque, deq_obj', number=1000000
    ))

    print('Функция append_list:', end='')
    print(timeit(
        'append_list(lst_obj)', setup='from __main__ import append_list, lst_obj', number=1000000
    ))


'''
Функция remove_left_deque: 5.0121035
Функция remove_left_list:  8.528395

Судя по времени deque удаляет быстрей.

Функция revers_deque:0.25771489999999986
Функция revers_list:0.20805949999999918

Реверс list делает быстрее чем  deque.

Функция append_deque:0.17047030000000163
Функция append_list:0.19156629999999986

Добавление deque делает быстрей чем list 
'''