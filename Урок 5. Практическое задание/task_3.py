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


MY_LIST = [numb for numb in range(1000)]
MY_DEQUE = deque(MY_LIST)


def fill_list():
    my_list = []
    for numb in range(1000):
        my_list.append(numb)


def remove_list(new_list):
    for el in new_list[:]:
        new_list.remove(el)


def get_list(new_list):
    for idx in range(len(new_list)):
        new_list[idx]


def fill_deque():
    my_deque = deque()
    for numb in range(1000):
        my_deque.append(numb)


def remove_deque(new_deque):
    for el in new_deque.copy():
        new_deque.remove(el)


def get_deque(new_deque):
    for idx in range(len(new_deque)):
        new_deque[idx]


result_fill_list = timeit("fill_list()", "from __main__ import fill_list", number=10000)
result_fill_deque = timeit("fill_deque()", "from __main__ import fill_deque", number=10000)

result_remove_list = timeit("remove_list(MY_LIST)", "from __main__ import remove_list, MY_LIST", number=1000000)
result_remove_deque = timeit("remove_deque(MY_DEQUE)", "from __main__ import remove_deque, MY_DEQUE", number=1000000)

result_get_list = timeit("get_list(MY_LIST)", "from __main__ import get_list, MY_LIST", number=1000000)
result_get_deque = timeit("get_deque(MY_DEQUE)", "from __main__ import get_deque, MY_DEQUE", number=1000000)


print(f'Результат выполнения fill_list(): \t{result_fill_list}')
print(f'Результат выполнения fill_deque(): \t{result_fill_deque}')
print()
print(f'Результат выполнения remove_list(): \t{result_remove_list}')
print(f'Результат выполнения remove_deque(): \t{result_remove_deque}')
print()
print(f'Результат выполнения get_list(): \t{result_get_list}')
print(f'Результат выполнения get_deque(): \t{result_get_deque}')

"""
Результат выполнения fill_list():       0.6998541580000001
Результат выполнения fill_deque():      0.597490795         -> Заполнение Deque происходит на 15% быстрее, чем списка.

Результат выполнения remove_list():     0.14822453400000013
Результат выполнения remove_deque():    0.19666190300000008 -> Удаление элементов из Deque происходит на 32% медленнее, чем из списка.

Результат выполнения get_list():        0.24839028399999985
Результат выполнения get_deque():       0.23297481600000003 -> Получение элементов из Deque происходит на 7% быстрее, чем из списка.
                                                               Можно считать время получения элементов практически одинаковым.
"""
