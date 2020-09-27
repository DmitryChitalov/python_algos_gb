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
from timeit import repeat

my_list = [i for i in range(1000)]
print(my_list)
my_deque = deque([i for i in range(1000)])
print(my_deque)


def append_list():
    copy_list = my_list.copy()
    for i in range(len(my_list)):
        copy_list.append(my_list[i])
    return copy_list


def append_deque():
    copy_deque = my_deque.copy()
    for i in range(len(my_deque)):
        copy_deque.append(my_deque[i])
    return copy_deque


def insert_list():
    copy_list = my_list.copy()
    for i in range(len(my_list)):
        copy_list.insert(0, my_list[i])
    return copy_list


def insert_deque():
    copy_deque = my_deque.copy()
    for i in range(len(my_deque)):
        copy_deque.appendleft(my_deque[i])
    return copy_deque


def del_list():
    copy_list = my_list.copy()
    if len(copy_list) != 0:
        copy_list.pop()


def del_deque():
    copy_deque = my_deque.copy()
    if len(copy_deque) != 0:
        copy_deque.pop()


print(repeat("append_list()", setup='from __main__ import append_list', number=10000, repeat=5))
"""[1.1602687999999999, 1.2441646, 1.2706089999999999, 1.1463693, 1.0557894999999995]"""
print(repeat("append_deque()", setup='from __main__ import append_deque', number=10000, repeat=5))
"""[1.08059, 1.1469237999999997, 1.0907188000000012, 1.0599656999999993, 1.1667489]"""
print(repeat("insert_list()", setup='from __main__ import insert_list', number=10000, repeat=5))
"""[5.871688699999998, 5.926226800000002, 5.8156354000000015, 5.596667099999998, 5.643771600000001]"""
print(repeat("insert_deque()", setup='from __main__ import insert_deque', number=10000, repeat=5))
"""[1.0985062999999968, 1.075772299999997, 1.1028783000000004, 1.1655309000000003, 1.1206530999999984]"""
print(repeat("del_list()", setup='from __main__ import del_list', number=10000, repeat=5))
"""[0.02022840000000059, 0.02013290000000012, 0.02223250000000121, 0.021683699999996975, 0.02049209999999846]"""
print(repeat("del_deque()", setup='from __main__ import del_deque', number=10000, repeat=5))
"""[0.06324469999999849, 0.06775189999999753, 0.06347689999999773, 0.06755669999999725, 0.06544849999999514]"""

"""
1) Добавление в конец list и deque примерно одинаково время показывает.
При разных запусках меняется преимуество, то в одну, то в другую сторону.
2) Добавление в начало list и deque, постоянное преимущество deque.
3) Удаление из конца list и deque, постоянное преимущество list.
"""