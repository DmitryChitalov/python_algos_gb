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
from random import randint

my_list = [randint(0, 99) for i in range(10)]
my_deque = deque(my_list)

N = 10000

# Добавление значений
print(
    "Добавление случайных значений в список - ",
    timeit(
        'my_list.append(randint(0, 99))',
        setup='from random import randint; from __main__ import my_list',
        number=N))

print(
    "Добавление случайных значений в деку - ",
    timeit(
        'my_deque.append(randint(0, 99))',
        setup='from random import randint; from __main__ import my_deque',
        number=N))

# Случайная выборка
print(
    "Выборка случайных элементов списка - ",
    timeit(
        'x = my_list[randint(0, N)]',
        setup='from random import randint; from __main__ import my_list, N',
        number=N))

print(
    "Выборка случайных элементов деки - ",
    timeit(
        'my_deque[randint(0, N)]',
        setup='from random import randint; from __main__ import my_deque, N',
        number=N))

# Удаление записей
print(
    "Удаление записей из списка - ",
    timeit(
        'my_list.pop(0)',
        setup='from random import randint; from __main__ import my_list',
        number=N))

print(
    "Удаление записей из деки - ",
    timeit(
        'my_deque.popleft()',
        setup='from random import randint; from __main__ import my_deque',
        number=N))

print(my_list)
print(my_deque)


# Вывод:
# Мы на практике убедились в большем быстродействии очереди, нежели листа при добавлении и удалении данных,
# А так же в большем быстродействии списка при случайной выборке

