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
from random import randint

# el_num = randint(0, 100000)
el_num = 100000
my_list = [el for el in range(100000)]
my_deque = deque(my_list)
print(my_deque)


def append_my_list(lst, el):
    return lst.append(el)


def append_my_deque(dq, el):
    return dq.append(el)


def pop_my_list(lst):
    return lst.pop(el_num)


def pop_my_deque(dq):
    return dq.popleft(el_num)


def access_to_item(lst):
    return lst[el_num]


def access_to_item_dq(dq):
    return dq[el_num]


# Добавление элемента
print(f"Добавление элемента в list: "
      f"{timeit('lambda: append_my_list(my_list, 10)', 'from __main__ import append_my_list')}")
print(f"Добавление элемента в deque: "
      f"{timeit('lambda: append_my_list(my_deque, 10)', 'from __main__ import append_my_deque')}")
# Извлечение элемента
print(f"Извлечение элемента из list: "
      f"{timeit('lambda: pop_my_list(my_list)', 'from __main__ import pop_my_list')}")
print(f"Извлечение элемента из deque: "
      f"{timeit('lambda: pop_my_deque(my_deque)', 'from __main__ import pop_my_deque')}")
# Доступ к элементу
print(f"Доступ к элементу в list: "
      f"{timeit('lambda: access_to_item(my_list)', 'from __main__ import access_to_item')}")
print(f"Доступ к элементу в deque: "
      f"{timeit('lambda: access_to_item_dq(my_deque)', 'from __main__ import access_to_item_dq')}")

"""
1) Скорость извлечения элемента в list и deque сопоставима;
2) Скорость добавления элемента в deque быстрее;
3) Скорость доступа к элементу в list и deque сопоставима;
"""
