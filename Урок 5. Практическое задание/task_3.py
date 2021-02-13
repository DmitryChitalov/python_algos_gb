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

list = [element for element in range(1, 100)]
deque_1 = deque()


def list_append():
    list.append(10)


def deque_append():
    deque_1.append(10)


def list_get_index():
    a = list[0]


def deque_get_index():
    a = deque_1[0]


for i in range(1, 10):
    deque_append()


def list_get_last():
    a = list[len(list) - 1]


def deque_get_last():
    a = deque_1.pop()


def list_revers():
    r_list = list.reverse()


def deque_revers():
    r_deque = deque_1.reverse()


# -----------------------------------------------------------------------------------------------------------------------
print("Добавление элементов")
print(
    timeit(
        "list_append()",
        setup='from __main__ import list_append',
        number=10000))

print(
    timeit(
        "deque_append()",
        setup='from __main__ import deque_append',
        number=10000))

print("\nПолучение элементов по индексу")
print(
    timeit(
        "list_get_index()",
        setup='from __main__ import list_get_index',
        number=10000))

print(
    timeit(
        "deque_get_index()",
        setup='from __main__ import deque_get_index',
        number=10000))

print("\nПолучение последнего элемента")
print(
    timeit(
        "list_get_last()",
        setup='from __main__ import list_get_last',
        number=10000))

print(
    timeit(
        "deque_get_last()",
        setup='from __main__ import deque_get_last',
        number=10000))

print("\nРеверс")

print(
    timeit(
        "deque_revers()",
        setup='from __main__ import deque_revers',
        number=10000))

print(
    timeit(
        "list_revers()",
        setup='from __main__ import list_revers',
        number=10000))


"""
В документации:
Добавить элемент быстрее deque 
Добавление элементов
0.0013611849990411429
0.001267338999241474

в получении случайных лементов быстрее list
Получение элементов по индексу
0.0009663680011726683
0.0009892279995256104

в получении последнего элемента быстре deque

Получение последнего элемента
0.008398378000492812
0.0012951660010003252

Реверс
0.0012233830002514878
0.046621917999800644

В документации описано реальное поведение стрктур.
список быстрее в получении случайного элеента, а deque быстрее в добалении элемента и получении последнего


"""