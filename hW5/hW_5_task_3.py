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
n_l = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90,91, 92, 93, 94, 95, 96, 97, 98, 99, 100
new_el = 101, 102, 103, 104, 105, 106, 107, 108, 109, 110
s_n_l = list(n_l)
deq_list = deque(n_l)


def create_list():
    s_n_l = list(n_l)


def cr_deq_list():
    deq_list = deque(n_l)


def ins_list():
    s_n_l.insert(0, new_el)


def ins_deq_list():
    deq_list.appendleft(new_el)


def ext_list():
    s_n_l.extend(new_el)


def ext_deq_list():
    deq_list.extend(new_el)


def cou_list():
    s_n_l.count(70)


def cou_deq_list():
    deq_list.count(70)


def pop_list():
    s_n_l.pop()


def pop_deq_list():
    deq_list.pop()


print(timeit.timeit("create_list()", setup="from __main__ import create_list"))
print(timeit.timeit("cr_deq_list()", setup="from __main__ import cr_deq_list"))

# формирование списка:
"""
0.314501
0.5688705000000001 - очередь медленней
"""
print(timeit.timeit("ins_list()", setup="from __main__ import ins_list"))
print(timeit.timeit("ins_deq_list()", setup="from __main__ import ins_deq_list"))
# добавление в нчало списка:
"""
206.31579649999998
0.09022809999999026 очередь быстрее в огромное количество раз!!!
"""
print(timeit.timeit("ext_list()", setup="from __main__ import ext_list"))
print(timeit.timeit("ext_deq_list()", setup="from __main__ import ext_deq_list"))

# добавление в конец списка:
"""
0.3168093
0.18381809999999998 снова очередь быстрее
"""
print(timeit.timeit("cou_list()", setup="from __main__ import cou_list"))
print(timeit.timeit("cou_deq_list()", setup="from __main__ import cou_deq_list"))

# подсчет элементов в списке:
"""
0.3168093
0.18381809999999998 снова очередь быстрее
"""
print(timeit.timeit("pop_list()", setup="from __main__ import pop_list", number=99))
print(timeit.timeit("pop_deq_list()", setup="from __main__ import pop_deq_list", number=99))

# удаление последних элементов в списке:
"""
1.1699999999999905e-05
1.1799999999999311e-05 по правилу сравнения числе в отрицательной степени очередь снова быстрее
"""
