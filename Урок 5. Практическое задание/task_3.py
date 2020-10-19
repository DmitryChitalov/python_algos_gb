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
import cProfile


lst = list()
dq = deque()


def append(a, el_count=100):
    for _ in range(el_count):
        a.append(randint(0, 100))


def pop(a, el_count=100):
    for _ in range(el_count):
        a.pop()
    

def list_insert_left(a, el_count=100):
    for _ in range(el_count):
        a.insert(0, randint(-100, -1))


def list_pop_left(a, el_count=100):
    for _ in range(el_count):
        a.pop(0)
    

def deque_append_left(a,el_count=100):
    for _ in range(el_count):
        a.appendleft(randint(-100, -1))


def deque_pop_left(a, el_count=100):
    for _ in range(el_count):
        a.popleft()


def test_list(a, el_count=100):
    """Тестирование списков

    """
    # Наполнение списка первыми данными в конец
    append(a, el_count * 2)
    # Наполнение списка данными в начало списка
    list_insert_left(a, el_count * 2)
    # Извлечение части данных с конца списка
    pop(a, el_count)
    # Извлечение части данных с начала списка
    list_pop_left(a, el_count)


def test_deque(a, el_count=100):
    """Тестирование очередей deque

    """
    # Наполнение списка первыми данными в конец
    append(a, el_count * 2)
    # Наполнение списка данными в начало списка
    deque_append_left(a, el_count * 2)
    # Извлечение части данных с конца списка
    pop(a, el_count)
    # Извлечение части данных с начала списка
    deque_pop_left(a, el_count)


def repeat_test_list(a, el_count=100, repeat=3):
    for _ in range(repeat):
        test_list(a, el_count)


def repeat_test_deque(a, el_count=100, repeat=3):
    for _ in range(repeat):
        test_deque(a, el_count)


#########################################
# Тестируем list
cProfile.run('repeat_test_list(lst, 10000, 3)')
""" >>>
813117 function calls in 2.835 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    2.835    2.835 <string>:1(<module>)
   120000    0.279    0.000    0.391    0.000 random.py:200(randrange)
   120000    0.258    0.000    0.649    0.000 random.py:244(randint)
   120000    0.084    0.000    0.112    0.000 random.py:250(_randbelow_with_getrandbits)
        3    0.106    0.035    0.434    0.145 task_3.py:23(append)
        3    0.005    0.002    0.007    0.002 task_3.py:28(pop)
        3    0.178    0.059    2.088    0.696 task_3.py:33(list_insert_left)
        3    0.010    0.003    0.305    0.102 task_3.py:38(list_pop_left)
        3    0.000    0.000    2.834    0.945 task_3.py:53(test_list)
        1    0.000    0.000    2.835    2.835 task_3.py:81(repeat_test_list)
        1    0.000    0.000    2.835    2.835 {built-in method builtins.exec}
    60000    0.005    0.000    0.005    0.000 {method 'append' of 'list' objects}
   120000    0.011    0.000    0.011    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   153098    0.017    0.000    0.017    0.000 {method 'getrandbits' of '_random.Random' objects}
    60000    1.584    0.000    1.584    0.000 {method 'insert' of 'list' objects}
    60000    0.297    0.000    0.297    0.000 {method 'pop' of 'list' objects}
"""

#########################################
# Тестируем deque
cProfile.run('repeat_test_deque(dq, 10000, 3)')
""" >>>
812863 function calls in 0.766 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.766    0.766 <string>:1(<module>)
   120000    0.244    0.000    0.338    0.000 random.py:200(randrange)
   120000    0.224    0.000    0.562    0.000 random.py:244(randint)
   120000    0.072    0.000    0.093    0.000 random.py:250(_randbelow_with_getrandbits)
        3    0.090    0.030    0.379    0.126 task_3.py:23(append)
        3    0.005    0.002    0.007    0.002 task_3.py:28(pop)
        3    0.090    0.030    0.373    0.124 task_3.py:43(deque_append_left)
        3    0.005    0.002    0.006    0.002 task_3.py:48(deque_pop_left)
        3    0.000    0.000    0.766    0.255 task_3.py:67(test_deque)
        1    0.000    0.000    0.766    0.766 task_3.py:86(repeat_test_deque)
        1    0.000    0.000    0.766    0.766 {built-in method builtins.exec}
    60000    0.005    0.000    0.005    0.000 {method 'append' of 'collections.deque' objects}
    60000    0.005    0.000    0.005    0.000 {method 'appendleft' of 'collections.deque' objects}
   120000    0.009    0.000    0.009    0.000 {method 'bit_length' of 'int' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
   152844    0.013    0.000    0.013    0.000 {method 'getrandbits' of '_random.Random' objects}
    30000    0.002    0.000    0.002    0.000 {method 'pop' of 'collections.deque' objects}
    30000    0.002    0.000    0.002    0.000 {method 'popleft' of 'collections.deque' objects}
"""
