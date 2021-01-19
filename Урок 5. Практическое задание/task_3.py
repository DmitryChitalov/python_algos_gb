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
import random
import timeit


list = [i for i in range(100)]
deque_1 = deque([i for i in range(100)])



def edit_list():
    for i in list:
        number = random.randint(1, 100)
        list[i] = i*number
    return list


def edit_deque():
    for i in deque_1:
        number = random.randint(1, 100)
        deque_1[i] = i*number
    return deque_1


def append_list(a):
    while a != 0:
        number = random.randint(1, 100)
        list.append(number)
        a -= 1
    return list


def append_deque(a):
    while a != 0:
        number = random.randint(1, 100)
        deque_1.append(number)
        a -= 1
    return deque_1


def appendleft_deque(a):
    while a != 0:
        number = random.randint(1, 100)
        deque_1.appendleft(number)
        a -= 1
    return deque_1


def remove_list(b):
    while b != 0:
        i = random.randint(1, 100)
        list.remove(i)
        b -= 1
    return list


def remove_deque(b):
    while b != 0:
        i = random.randint(1, 100)
        deque_1.remove(i)
        b -= 1
    return deque_1


a = 1000
b = 10
edit_list_time = timeit.timeit('edit_list', setup='from __main__ import edit_list', number=1000)
edit_deque_time = timeit.timeit('edit_deque', setup='from __main__ import edit_deque', number=1000)
append_list_time = timeit.timeit('append_list(a)', setup='from __main__ import append_list, a', number=1000)
append_deque_time = timeit.timeit('append_deque(a)', setup='from __main__ import append_deque, a', number=1000)
appendleft_deque_time = timeit.timeit('appendleft_deque(a)', setup='from __main__ import appendleft_deque, a', number=1000)
remove_list_time = timeit.timeit('remove_list(b)', setup='from __main__ import remove_list, b', number=1000)
remove_deque_time = timeit.timeit('remove_deque(b)', setup='from __main__ import remove_deque, b', number=1000)

print(f'Изменение элементов в списке - {edit_list_time}')
print(f'Изменение элементов в очереди - {edit_deque_time}')
print(f'Добавление элементов в список - {append_list_time}')
print(f'Добавление элементов в очередь - {append_deque_time}')
print(f'Добавление appendleft элементов в очередь - {appendleft_deque_time}')
print(f'Удаление элементов из списка - {remove_list_time}')
print(f'Удаление элементов из очереди - {remove_deque_time}')

'''
Изменение значений элементов в списке - 2.6384999999996828e-05
Изменение значений элементов в очереди - 2.763299999999913e-05
Добавление элементов в список - 1.368061832
Добавление элементов в очередь - 1.291890653
Добавление appendleft элементов в очередь - 1.289948463
Удаление элементов из списка - 9.68080389
Удаление элементов из очереди - 0.17331275400000123

Удаление элементов из очереди работает в 10 раз быстрее, а вот добавлене в список почему-то почти так же
'''