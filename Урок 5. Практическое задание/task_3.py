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


def deq_appleft():
    our_deque.appendleft(None)
    return


def list_insert():
    our_list.insert(0, None)
    return


def deq_popleft():
    our_deque.popleft()
    return


def list_pop():
    our_list.pop(0)
    return


def deq_append():
    our_deque.append(None)
    return


def list_append():
    our_list.append(None)
    return


our_list = list(range(1000))
our_deque = deque(our_list)

test_dal = timeit('deq_appleft()',
                  'from __main__ import deq_appleft',
                  number=100000)
test_lin = timeit('list_insert()',
                  'from __main__ import list_insert',
                  number=100000)

print(test_dal)
print(test_lin)
print(f'Deque быстрее в {test_lin/test_dal:0.2f} раз \n')

test_dpl = timeit('deq_popleft()',
                  'from __main__ import deq_popleft',
                  number=100000)
test_lp = timeit('list_pop()',
                 'from __main__ import list_pop',
                 number=100000)

print(test_dpl)
print(test_lp)
print(f'Deque быстрее в {test_lp/test_dpl:0.2f} раз \n')

test_da = timeit('deq_append()',
                 'from __main__ import deq_append',
                 number=100000)
test_la = timeit('list_append()',
                 'from __main__ import list_append',
                 number=100000)

print(test_da)
print(test_la)
print(f'Deque (не)быстрее в {test_la/test_da:0.2f} раз \n')


"""
deq_appleft 0.016710072
list_insert 2.5260141139999996
Deque быстрее в 151.17 раз 

deq_popleft 0.015686720000000154
list_pop 1.7846854409999997
Deque быстрее в 113.77 раз 

deq_append 0.018181649999999827
list_append 0.017341630999999857
Deque (не)быстрее в 0.95 раз 

По общему итогу замеров видно, что Append для List и Deuqe - отрабатывают почти на равной скорости
Однако Insert и Pop у них проходят с существенной разницей в 100++ раз
Deque выигрывает, очевидно =)
"""