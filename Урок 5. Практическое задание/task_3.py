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

"""
    Тестируем методы, определенные в коллекции deque.
    1) appendleft VS insert.
"""


def deque_appendleft():
    d = deque()
    for i in range(10000):
        d.appendleft(i)


def list_insert():
    l = list()
    for i in range(10000):
        l.insert(0, i)


print("deque_appendleft_time: ", timeit("deque_appendleft()",
                                        "from __main__ import deque_appendleft",
                                        number=100))
print("list_insert_time: ", timeit("list_insert()",
                                   "from __main__ import list_insert",
                                   number=100))
"""
    Безоговорочная победа за коллекцией deque. Операция вставки происходит значительно быстрее.
    deque_appendleft_time:  0.0613959 VS list_insert_time:  1.5652554
"""
###############################################################################
"""
    2) deque_append VS list_append
"""


def deque_append():
    d = deque()
    for i in range(10000):
        d.append(i)


def list_append():
    l = list()
    for i in range(10000):
        l.append(i)


print("deque_append_time: ", timeit("deque_append()",
                                    "from __main__ import deque_append",
                                    number=1000))
print("list_append_time: ", timeit("list_append()",
                                   "from __main__ import list_append",
                                   number=1000))

"""
    Во втором противостоянии объявляется ничья.
    deque_append_time:  0.5758004 VS list_append_time:  0.5757568
"""
###############################################################################
"""
    3) deque_popleft VS list_popleft
"""


def deque_popleft():
    d = deque(range(1000))
    for i in range(len(d)):
        d.popleft()


def list_popleft():
    l = list(range(1000))
    for i in range(len(l)):
        l.pop(0)


print("deque_popleft_time: ", timeit("deque_popleft()",
                                     "from __main__ import deque_popleft",
                                     number=1000))
print("list_popleft_time: ", timeit("list_popleft()",
                                    "from __main__ import list_popleft",
                                    number=1000))

"""
    В третьем раунде победа снова за коллекцией deque.
    deque_popleft_time:  0.06719859999999978 VS list_popleft_time:  0.16106989999999977
"""
###############################################################################
"""
    4) deque_pop VS list_pop
"""


def deque_pop():
    d = deque(range(1000))
    for i in range(len(d)):
        d.pop()


def list_pop():
    l = list(range(1000))
    for i in range(len(l)):
        l.pop()


print("deque_pop_time: ", timeit("deque_pop()",
                                 "from __main__ import deque_pop",
                                 number=1000))
print("list_pop_time: ", timeit("list_pop()",
                                "from __main__ import list_pop",
                                number=1000))

"""
    Интерес к тестированию начинает пропадать, т.к. deque, очевидно, справляется с задачами быстрее.
    deque_pop_time:  0.0575261 VS list_pop_time:  0.07248030
"""
###############################################################################
"""
    5) deque_insert VS list_insert
"""


def deque_insert():
    d = deque()
    for i in range(1000):
        d.insert(0, i)


def list_insert_2():
    l = list()
    for i in range(1000):
        l.insert(0, i)


print("deque_insert_time: ", timeit("deque_insert()",
                                    "from __main__ import deque_insert",
                                    number=1000))
print("list_insert_2_time: ", timeit("list_insert_2()",
                                     "from __main__ import list_insert_2",
                                     number=1000))

"""
    Последний гвоздь в крышку стандартных методов. Безкомпромисная победа коллекции deque.
    deque_insert_time:  0.0922857 VS list_insert_2_time:  0.2427235
"""
