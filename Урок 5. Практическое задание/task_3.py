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
import cProfile
from collections import deque
import random
my_list = list()
deq_obj = deque("")


def append_deq():
    for i in range(1000000):
        deq_obj.append(random.randint(0, 1000))


def append_left_deq():
    for i in range(1000000):
        deq_obj.appendleft(random.randint(0, 1000))


def get_deq():
    for el in deq_obj:
        el = 0


def get_deq_el():
    for i in range(2000000):
        deq_obj[random.randint(0, 1000000)]


def append_list():
    for i in range(2000000):
        my_list.append(random.randint(0, 1000))


def get_list():
    for el in my_list:
        el = 0


def get_list_el():
    for i in range(2000000):
        my_list[random.randint(0, 1000000)]


print(f"Добавление в конец deque")
cProfile.run('append_deq()')        # 2.038 seconds

print(f"Добавление в начало deque")
cProfile.run('append_left_deq()')   # 2.025 seconds

print(f"Перебор deque")
cProfile.run('get_deq()')           # 0.028 seconds

print(f"Извлечение случайных элементов из deque")
cProfile.run('get_deq_el()')           # 123.3 seconds

print("Добавление в конец списка")
cProfile.run('append_list()')       # 4.093 seconds

print(f"Перебор списка")
cProfile.run('get_list()')          # 0.023 seconds

print(f"Извлечение случайных элементов из списка")
cProfile.run('get_list_el()')          # 3.88 seconds

"""
Добавление в deque в начало и в конец занимает примерно одинаковое время. Так же как и добавление в конец списка (если
сложить время на добавление слева и в конец deque, чтобы в сумме было одинаковое кол-во элементов). Взятие элемента
методом перебора быстрее идет в обычном списке, но не значительно. Если извлекать случайные значения по индексу элемента
то в обычном списке в разы быстрее, чем в deque
"""