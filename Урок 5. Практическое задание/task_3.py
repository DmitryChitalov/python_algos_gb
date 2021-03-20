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
from timeit import timeit


def append_left_list(num):
    my_list = []
    for i in range(num):
        my_list.insert(0, i)


def append_left_deque(num):
    my_deque = deque()
    for i in range(num):
        my_deque.appendleft(i)


def append_right_list(num):
    my_list = []
    for i in range(num):
        my_list.append(i)


def append_right_deque(num):
    my_deque = deque()
    for i in range(num):
        my_deque.append(i)


def pop_left_list(my_list):
    for i in range(len(my_list)):
        my_list.pop(0)


def pop_left_deque(my_deque):
    for i in range(len(my_deque)):
        my_deque.popleft()


def pop_right_list(my_list):
    for i in range(len(my_list)):
        my_list.pop()


def pop_right_deque(my_deque):
    for i in range(len(my_deque)):
        my_deque.pop()


num = 1000

def_list = [el for el in range(num)]
def_deque = deque(def_list)

print(f"append_left_list({num}): ",
      timeit(f"append_left_list({num})", globals=globals(), number=1000))
print(f"append_left_deque({num}): ",
      timeit(f"append_left_deque({num})", globals=globals(), number=1000))
print()
print(f"append_right_list({num}): ",
      timeit(f"append_right_list({num})", globals=globals(), number=1000))
print(f"append_right_deque({num}): ",
      timeit(f"append_right_deque({num})", globals=globals(), number=1000))
print()
my_list2 = def_list.copy()
my_deque2 = def_deque.copy()
print("pop_left_list(my_list2): ",
      timeit("pop_left_list(my_list2)", globals=globals(), number=1000))
print("pop_left_deque(my_deque2): ",
      timeit("pop_left_deque(my_deque2)", globals=globals(), number=1000))
print()
my_list3 = def_list.copy()
my_deque3 = def_deque.copy()
print("pop_right_list(my_list3): ",
      timeit("pop_right_list(my_list3)", globals=globals(), number=1000))
print("pop_right_deque(my_deque3): ",
      timeit("pop_right_deque(my_deque3)", globals=globals(), number=1000))
print()
print("def_list.reverse(): ",
      timeit("def_list.reverse()", globals=globals(), number=1000))
print("def_deque.reverse(): ",
      timeit("def_deque.reverse()", globals=globals(), number=1000))
