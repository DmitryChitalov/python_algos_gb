"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить,
используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""

from collections import deque
from timeit import timeit


def list_append(lst):
    for i in range(1000):
        lst.append(i)


def list_append_idx(lst):
    for i in range(1000):
        lst.insert(0, i)


def list_extend(lst):
    lst.extend([i for i in range(1000)])


def list_extend_idx(lst):
    for i in range(1000):
        lst.insert(0, i)


def list_pop(lst):
    for i in range(1000):
        a = lst.pop()


def list_pop_idx(lst):
    for i in range(1000):
        a = lst.pop(0)


def list_reverse(lst):
    return lst.reverse()


def deque_append(dqe):
    for i in range(1000):
        dqe.append(i)


def deque_appendleft(dqe):
    for i in range(1000):
        dqe.appendleft(i)


def deque_extend(dqe):
    dqe.extend([i for i in range(1000)])


def deque_extendleft(dqe):
    dqe.extendleft([i for i in range(1000)])


def deque_pop(dqe):
    for i in range(1000):
        a = dqe.pop()


def deque_popleft(dqe):
    for i in range(1000):
        a = dqe.popleft()


def deque_reverse(dqe):
    return dqe.reverse()


some_list = [el for el in range(10000)]
some_deque = deque([el for el in range(10000)])

print('list: ', timeit("list_append(some_list)", globals=globals(),
                       number=100))
print('deque: ', timeit("deque_append(some_deque)", globals=globals(),
                        number=100))
print('-' * 100)
print('list: ', timeit("list_append_idx(some_list)", globals=globals(),
                       number=100))
print('deque: ',
      timeit("deque_appendleft(some_deque)", globals=globals(),
             number=100))
print('-' * 100)
print('list: ', timeit("list_extend(some_list)", globals=globals(),
                       number=100))
print('deque: ',
      timeit("deque_extend(some_deque)", globals=globals(),
             number=100))
print('-' * 100)
print('list: ', timeit("list_extend_idx(some_list)", globals=globals(),
                       number=100))
print('deque: ',
      timeit("deque_extendleft(some_deque)", globals=globals(), number=100))
print('-' * 100)
print('list: ', timeit("list_pop(some_list)", globals=globals(), number=100))
print('deque: ', timeit("deque_pop(some_deque)", globals=globals(), number=100))
print('-' * 100)
print('list: ', timeit("list_pop_idx(some_list)", globals=globals(),
                       number=100))
print('deque: ',
      timeit("deque_popleft(some_deque)", globals=globals(), number=100))
print('-' * 100)
print('list: ', timeit("list_reverse(some_list)", globals=globals(),
                       number=100))
print('deque: ',
      timeit("deque_reverse(some_deque)", globals=globals(), number=100))

"""
Добавление элемента в список справа: скорость похожая
list:  0.013968999999999995
deque:  0.016079800000000005
----------------------------------------------------------------------------------------------------
Добавление элемента в список слева: для deque скорость гораздо выше
list:  9.794535699999999
deque:  0.009253700000000364
----------------------------------------------------------------------------------------------------
Расширение списка справа: скорость примерно одинаковая
list:  0.005163800000000052
deque:  0.004913900000000027
----------------------------------------------------------------------------------------------------
Расширение списка слева: для deque скорость гораздо выше
list:  22.746557900000003
deque:  0.005251399999998796
----------------------------------------------------------------------------------------------------
Удаление элемента справа: скорость примерно одинаковая
list:  0.010830500000004406
deque:  0.012880299999999067
----------------------------------------------------------------------------------------------------
Удаление элемента слева: для deque скорость гораздо выше
list:  4.9500414999999975
deque:  0.010427100000001133
----------------------------------------------------------------------------------------------------
Reverce: для list скорость выше
list:  0.008230000000004623
deque:  0.02276170000000377
"""
