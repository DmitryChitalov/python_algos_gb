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

lst_obj = []
deq_obj = deque()
ARRAY_SIZE = 50


def lst_app_end(lst_o):
    for i in range(ARRAY_SIZE):
        lst_o.append(randint(0, 1000))


def deq_app_end(deq_o):
    for i in range(ARRAY_SIZE):
        deq_o.append(randint(0, 1000))


def lst_app_start(lst_o):
    for i in range(ARRAY_SIZE):
        lst_o.insert(0, randint(0, 1000))


def deq_app_start(deq_o):
    for i in range(ARRAY_SIZE):
        deq_o.appendleft(randint(0, 1000))


def lst_ins(lst_o):
    for i in range(ARRAY_SIZE):
        lst_o.insert(2 * randint(0, 1000), randint(0, 1000))


def deq_ins(deq_o):
    for i in range(ARRAY_SIZE):
        deq_o.insert(2 * randint(0, 1000), randint(0, 1000))


def lst_pop_cnt(lst_o):
    for i in range(ARRAY_SIZE):
        lst_o.pop(randint(0, 3000 - i))


# def deq_pop_cnt(deq_o):
#     for i in range(ARRAY_SIZE):
#         deq_o.pop(randint(0, 3000 - i))


def lst_pop_end(lst_o):
    for i in range(ARRAY_SIZE):
        lst_o.pop()


def deq_pop_end(deq_o):
    for i in range(ARRAY_SIZE):
        deq_o.pop()


def lst_pop_start(lst_o):
    for i in range(ARRAY_SIZE):
        lst_o.pop(0)


def deq_pop_start(deq_o):
    for i in range(ARRAY_SIZE):
        deq_o.popleft()


print("\n1) Проверка добавления элементов в конец массива.\n")
print("list: ", timeit("lst_app_end(lst_obj)", setup="from __main__ import lst_app_end, lst_obj", number=1000))
print("deque: ", timeit("deq_app_end(deq_obj)", setup="from __main__ import deq_app_end, deq_obj", number=1000))

print("\n2) Проверка добавления элементов в начало массива.\n")
print("list: ", timeit("lst_app_start(lst_obj)", setup="from __main__ import lst_app_start, lst_obj", number=1000))
print("deque: ", timeit("deq_app_start(deq_obj)", setup="from __main__ import deq_app_start, deq_obj", number=1000))

print("\n3) Проверка добавления элементов в тело массива.\n")
print("list: ", timeit("lst_ins(lst_obj)", setup="from __main__ import lst_ins, lst_obj", number=1000))
print("deque: ", timeit("deq_ins(deq_obj)", setup="from __main__ import deq_ins, deq_obj", number=1000))

print("\n4) Проверка извлечения элементов из тела массива.\n")
print("list: ", timeit("lst_pop_cnt(lst_obj)", setup="from __main__ import lst_pop_cnt, lst_obj", number=1000))
print("deque: ", "операция не предусмотрена")

print("\n5) Проверка извлечения элементов с конца массива.\n")
print("list: ", timeit("lst_pop_end(lst_obj)", setup="from __main__ import lst_pop_end, lst_obj", number=1000))
print("deque: ", timeit("deq_pop_end(deq_obj)", setup="from __main__ import deq_pop_end, deq_obj", number=1000))

print("\n6) Проверка извлечения элементов с начала массива.\n")
print("list: ", timeit("lst_pop_start(lst_obj)", setup="from __main__ import lst_pop_start, lst_obj", number=1000))
print("deque: ", timeit("deq_pop_start(deq_obj)", setup="from __main__ import deq_pop_start, deq_obj", number=1000))

"""

1) Проверка добавления элементов в конец массива.

list:  0.20830687200032116
deque:  0.19328213100016

2) Проверка добавления элементов в начало массива.

list:  6.3864746110011765
deque:  0.1666976500000601

3) Проверка добавления элементов в тело массива.

list:  13.21898601599969
deque:  0.5230054479998216

4) Проверка извлечения элементов из тела массива.

list:  22.26357416800056
deque:  операция не предусмотрена

5) Проверка извлечения элементов с конца массива.

list:  0.011479024000436766
deque:  0.009904327998810913

6) Проверка извлечения элементов с начала массива.

list:  0.6525775480004086
deque:  0.009976287999961642

Объекты list и deque показывают примерно одинаковую эффективность на операциях добавления/извлечения элементов в конце
массива; даже с небольшим преимуществом deque.
Но в операциях добавления/извлечения элементов в начале массива deque выигрывает более чем на порядок.
И, что интересно, такое же огромное преимущество deque имеет и при добавлении элемента в тело массива.
"""