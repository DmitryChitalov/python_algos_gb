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

1)##################################################################################

def deque_append():
    my_deque = deque()
    for i in range(1000):
        my_deque.append(i)


def lst_append():
    my_list = []
    for i in range(1000):
        my_list.append(i)


print("deque_append: ", timeit("deque_append()",
                                    "from __main__ import deque_append",
                                    number=100))
print("lst_append: ", timeit("lst_append()",
                                   "from __main__ import lst_append",
                                   number=100))

"""
Время выполнения примерно равно на больших ималых значениях number! 
deque_append:  0.0621415
lst_append:  0.06600430000000002
"""

2)##################################################################################

def deque_appendleft():
    my_deque = deque()
    for i in range(1000):
        my_deque.appendleft(i)

def lst_insert():
    my_list = []
    for i in range(1000):
        my_list.insert(0, i)



print("deque_appendleft: ", timeit("deque_appendleft()",
                                        "from __main__ import deque_appendleft",
                                        number=100))
print("lst_insert: ", timeit("lst_insert()",
                                   "from __main__ import lst_insert",
                                   number=100))

"""
deque здесь значительно быстре!
deque_appendleft:  0.005974899999999998
lst_insert:  0.0279077
"""

3)##################################################################################

def deque_insert():
    my_deque = deque()
    for i in range(1000):
        my_deque.insert(0, i)


def lst_insert_2():
    my_list = []
    for i in range(1000):
        my_list.insert(0, i)


print("deque_insert: ", timeit("deque_insert()",
                                    "from __main__ import deque_insert",
                                    number=1000))
print("list_insert_2: ", timeit("lst_insert_2()",
                                     "from __main__ import lst_insert_2",
                                     number=1000))

"""
deque здесь тут быстре!
deque_insert:  0.10482419999999999
list_insert_2:  0.298469
"""
4)##################################################################################

def deque_popleft():
    my_deque = deque(range(1000))
    for i in range(len(my_deque)):
        my_deque.popleft()


def list_pop():
    my_list = list(range(1000))
    for i in range(len(my_list)):
        my_list.pop(0)


print("deque_popleft: ", timeit("deque_popleft()",
                                     "from __main__ import deque_popleft",
                                     number=1000))
print("list_pop: ", timeit("list_pop()",
                                    "from __main__ import list_pop",
                                    number=1000))

"""
deque здесь значительно быстре!
deque_popleft:  0.07363760000000003
list_pop:  0.6410035
"""

# Вывод: В большинстве тестов deque справляется с задачами быстрее list.


