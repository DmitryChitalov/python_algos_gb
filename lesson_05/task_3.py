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
from timer import timer
from random import randint


NUMBER = 5000


@timer(NUMBER)
def fill_obj(obj, num):
    for _ in range(num):
        obj.append(randint(1, 100))


@timer(NUMBER)
def left_app_deque(deq):
    deq.appendleft(randint(1, 100))


@timer(NUMBER)
def left_insert(lst):
    lst.insert(0, randint(1, 100))


@timer(NUMBER)
def random_insert(obj):
    pos = randint(0, len(obj) - 1)
    obj.insert(pos, randint(1, 100))


@timer(NUMBER)
def element_get(obj):
    idx = randint(0, len(obj) - 1)
    elem = obj[idx]
    return elem


@timer(NUMBER)
def pop_right(obj):
    elem = obj.pop()
    return elem


@timer(NUMBER)
def pop_left_deq(deq):
    elem = deq.popleft()
    return elem


@timer(NUMBER)
def pop_left_list(lst):
    elem = lst.pop(0)
    return elem


@timer(NUMBER)
def random_pop(obj):
    idx = randint(0, len(obj) - 1)
    elem = obj.pop(idx)
    return elem


test_list = list()
test_deque = deque()

print('\nЗаполнение list и deque:')
print('list:', end=' ')
fill_obj(test_list, 100)
print('deque:', end=' ')
fill_obj(test_deque, 100)

# list: 0.2732127999999997
# deque: 0.2661854000000027
# Замеры показывают, что очередь заполняется незначительно быстрее, чем список

print('\nДобавление элемента в начало:')
print('list:', end=' ')
left_insert(test_list)
print('deque:', end=' ')
left_app_deque(test_deque)

# list: 1.3033582000000026
# deque: 0.00318570000000018
# Элементы в начало списка добавляются в гораздо медленнее,
# чем в начало очереди - что соответствует документации.

print('\nДобавление элемента в произвольную позицию:')
print('list:', end=' ')
random_insert(test_list)
print('deque:', end=' ')
random_insert(test_deque)

# list: 0.6128666999999923
# deque: 0.6984531000000018

# Добавление элемента в произвольную позицию в список происходит несколько быстрее,
# чем в очередь, впрочем незначительно.

print('\nПолучение значения элемента по индексу:')
print('list:', end=' ')
element_get(test_list)
print('deque:', end=' ')
element_get(test_deque)

# list: 0.003778700000016233
# deque: 0.09563959999998817

# А вот обращение к элементу по индексу в списке происходит значительно быстрее, чем в очереди, что соответствует
# документации.

print('\nЗабрать элемент справа:')
print('list:', end=' ')
pop_right(test_list)
print('deque:', end=' ')
pop_right(test_deque)

# list: 0.000668099999998617
# deque: 0.0006687999999948069

# Получение элемента справа в списке происходит почти за то же время (чуть быстрее), что и в очереди -
# разница настолько мала, что ею можно пренебречь.

print('\nЗабрать элемент слева:')
print('list:', end=' ')
pop_left_list(test_list)
print('deque:', end=' ')
pop_left_deq(test_deque)

# list: 0.4595461000000016
# deque: 0.00066099999999647

# А вот получение элемента из начала списка происходит невероятно долго по сравнению с той же операцией в очереди.
# Метод pop в очереди не позволяет извлекать элементы из произвольной позиции,
# что только подтверждает назначение класса.

# По результатам замеров видно, что информация в документации соответствует действительности:
# очередь незначительно хуже справляется с добавлением и извлечением элементов с конца,
# и гораздо быстрее выполняет операции извлечения и вставки элементов в начало, а вот при работе с обращением
# по индексу и вставкой или извлечением элементов из произвольной позиции имеет смысл обратиться к списку.
