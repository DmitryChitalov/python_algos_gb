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
import random


def test_list(ob_test=[]):
    for i in range(1000):
        ob_test.append(i)
        # ob_test.insert(0, i)
    return


def test_deque(ob_test=deque([])):
    for i in range(1000):
        ob_test.append(i)
        # ob_test.appendleft(i)
    return


def test_list_R(list_test, list_ramd):
    for i in list_ramd:
        k = list_test[i]
        return k


def test_deque_R(deque_test, list_rand):
    for i in list_rand:
        k = deque_test[i]
        return k


# test_deque_R(deque_test, list_random)
# test_list_R(list_test, list_random)

# print(list_test)
# print(deque_test)

# print(test_deque())
# print(timeit.timeit("test_list()", setup="from __main__ import test_list", number=1000))
# print(timeit.timeit("test_deque()", setup="from __main__ import test_deque", number=1000))

# ------------------------------------------------------------------------------------------
# Замеры доступа к случайному элементу
list_test = list(range(100000))
deque_test = deque(list_test)
list_random = [random.randint(0, 99999) for i in range(100000)]     # Формированние списка случайных индексов

print(timeit.timeit("test_list_R(list_test, list_random)", setup="from __main__ import test_list_R, list_test,"
                                                                 " list_random", number=3000000))
print(timeit.timeit("test_deque_R(deque_test, list_random)", setup="from __main__ import test_deque_R,"
                                                                   " deque_test, list_random", number=3000000))

# ------------------------------------------------------------------------------------------
"""
По данным замеров:
метод .append() список 1000 элементов 10 000 раз 
list    -> 1.1072522
deque   -> 0.8640307999

методы .insert() и .appendleft() список 1000 элементов 1000 раз 
list    -> 189.182783
deque   -> 0.08318979999998533

Вывод:  Вставлять элементы в 'deque' быстрее
*******************************************

Cлучайный доступ: 10 000 элементов 3 000 000 раз
list    -> 0.5925965
deque   -> 0.7975883

Cлучайный доступ: 100 000 элементов 3 000 000 раз
list    -> 0.5824444
deque   -> 3.4590721

Вывод:  Случайный доступ к элементам 'list' работает быстрее 
"""