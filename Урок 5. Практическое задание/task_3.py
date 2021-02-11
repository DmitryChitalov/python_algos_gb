"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует действительности.

Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям

И добавить аналитику, так ли это или нет.!
"""

from collections import deque
from timeit import timeit
from random import randint

my_list = [randint(0, 99) for i in range(10)]
my_deque = deque(my_list)

N = 10000

print(
    "Добавление случайных значений в конец списка - ",
    timeit(
        'my_list.append(randint(0, 99))',
        setup='from random import randint; from __main__ import my_list',
        number=N))

print(
    "Добавление случайных значений в конец дека - ",
    timeit(
        'my_deque.append(randint(0, 99))',
        setup='from random import randint; from __main__ import my_deque',
        number=N))

print(
    "Добавление случайных значений в начало списка - ",
    timeit(
        'my_list.insert(0,randint(0, 99))',
        setup='from random import randint; from __main__ import my_list',
        number=N))

print(
    "Добавление случайных значений в начало дека - ",
    timeit(
        'my_deque.appendleft(randint(0, 99))',
        setup='from random import randint; from __main__ import my_deque',
        number=N))

print(
    "Выборка случайных индексов списка - ",
    timeit(
        'x = my_list[randint(0, 2*N)]',
        setup='from random import randint; from __main__ import my_list, N',
        number=N))

print(
    "Выборка случайных индексов дека - ",
    timeit(
        'my_deque[randint(0, 2*N)]',
        setup='from random import randint; from __main__ import my_deque, N',
        number=N))

print(
    "Удаление записей из начала списка - ",
    timeit(
        'my_list.pop(0)',
        setup='from random import randint; from __main__ import my_list',
        number=N))

print(
    "Удаление записей из начала дека - ",
    timeit(
        'my_deque.popleft()',
        setup='from random import randint; from __main__ import my_deque',
        number=N))

print(
    "Удаление записей c конца списка - ",
    timeit(
        'my_list.pop()',
        setup='from random import randint; from __main__ import my_list',
        number=N))

print(
    "Удаление записей с конца дека - ",
    timeit(
        'my_deque.pop()',
        setup='from random import randint; from __main__ import my_deque',
        number=N))

print(my_list)
print(my_deque)

print(
    """Выводы:
1) Добавление записей в список с конца быстрее аналогичных операций с деком.
1а) Удаление записей с конца занимает почти одинаковое время, но дек чуть быстрее
2) Добавление и удаление записей из начала дека отрабатывает быстрее, чем в списке
3) Доступ к случайным данным в списке происходит быстрее

Документация не врет :)
    """
)
