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

Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям

И добавить аналитику, так ли это или нет.!
"""
from timeit import Timer
from collections import deque
from random import randint








# # Create
# def lst():
#     lst1 = []
#     return lst1
#
#
# def deq():
#     dc = deque()
#     return dc

# Append left
# def lst(lsa):
#     lsa.append(1)
#     return lsa
#
#
# def deq(deqa):
#     deqa.appendleft(1)
#     return deqa

# pop
# lsa = [randint(0, 100) for i in range(100)]
# def lst(lsa):
#     lsa.pop()
#     return lsa
#
# deqa = deque([randint(0, 100) for i in range(100)])
# def deq(deqa):
#     deqa.popleft()
#     return deqa

# extend left
# lsa = [randint(0, 100) for i in range(100)]
# def lst(lsa):
#     lsa.extend([1,2])
#     return lsa
#
# deqa = deque([randint(0, 100) for i in range(100)])
#
# def deq(deqa):
#     deqa.extendleft([1,2])
#     return deqa

# extend
# lsa = [randint(0, 100) for i in range(100)]
#
# def lst(lsa):
#     lsa.extend([1,2])
#     return lsa
#
# deqa = deque([randint(0, 100) for i in range(100)])
#
# def deq(deqa):
#     deqa.extend([1,2])
#     return deqa

# чтение
lsa = [randint(0, 100) for i in range(100)]

def lst(lsa):
    a = lsa[65]
    return a

deqa = deque([randint(0, 100) for i in range(100)])

def deq(deqa):
    a = deqa[65]
    return a



t1 = Timer('lst(lsa)', globals=globals())
t2 = Timer('deq(deqa)', globals=globals())
print('lst', t1.timeit(number=100000))
print('deq', t2.timeit(number=100000))

"""
******На пустых массивах************
----test 1 --- number = 100000----good test
------Create-------
lst 0.0055406
deq 0.0101194

----test 2 --- number = 1000000----bad test
------append-------
lst 0.0823624
deq 0.1151026

----test 3 --- number = 1000000----bad test
------appendleft-------
lst 0.0889375
deq 0.1303476

*******На заполненых массивах*******
------append------- good test
lst 0.0858071
deq 0.0780246

------appendleft------- good test
lst 0.0853124
deq 0.08037190000000001

---------pop--- number =1 -------- good test
lst 9.999999999975306e-07
deq 4.999999999970306e-07

---------popleft-- number=1 --------- good test
lst 1.000000000001e-06
deq 5.999999999999062e-07

---------extendleft-- number=100000 --------- ??? Непонятно почему расширение списка медленнее в деке.
lst 0.012126299999999996
deq 0.022714400000000003

---------extend-- number=100000 ---------??? Непонятно почему расширение списка медленнее в деке с обеих сторон.
lst 0.0112096
deq 0.0138081

---------взятие по индексу (т.е чтение)-- number=100000 -----
lst 0.0062094
deq 0.007014700000000002

Выводы:
1. Дека создается медленнее листа. (create)
2. На пустом массиве тестить бесполезно.
3. На заполненном масиве дека работает быстрее на вставке и удалении (слева справа) как и было заявлено.\
\ appendleft  append
4. Дека медленнее для расширение списка (extend) 
5. Дека на чтение работает медленнее, как и заявлено. (lst[x])





"""

