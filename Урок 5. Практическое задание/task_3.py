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

Ответ: 'Вот основное правило...' - это не основное правило, а дополнительное.
Основное правило состоит в том, что функциональность, которую несет возможное ограничение длины deque,
намного лучше подходит для определенного ряда задач, чем функциональность простых списков.

Оценка времени совпадает с тем, что написанно в документации: добавление элемента в начало и извлечение
его оттуда в deque производится значительно быстрее, чем в списоке. Но извлечение по индексу происходит
немного медленнее в deque, чем в списке.
"""

from collections import deque
from random import randint
from timeit import timeit


def append_right(obj):
    obj.append(100)


def append_left(obj):
    if isinstance(obj, list):
        obj.insert(0, 100)
    if isinstance(obj, deque):
        obj.appendleft(100)


def pop_right(obj):
    obj.pop()


def pop_left(obj):
    if isinstance(obj, list):
        return obj.pop(0)
    if isinstance(obj, deque):
        return obj.popleft()


def get_el(obj, num):
    return obj[num]


if __name__ == '__main__':
    a = [randint(1, 100) for _ in range(10000)]
    b = deque(a)
    c = randint(0, len(a))
    print('Добавление элемента в конец:')
    print(timeit('append_right(a)', number=10000, globals=globals()))
    print(timeit('append_right(b)', number=10000, globals=globals()))
    print('\nДобавление элемента в начало:')
    print(timeit('append_left(a)', number=10000, globals=globals()))
    print(timeit('append_left(b)', number=10000, globals=globals()))
    print('\nИзвлечение элемента с конца:')
    print(timeit('pop_right(a)', number=10000, globals=globals()))
    print(timeit('pop_right(b)', number=10000, globals=globals()))
    print('\nИзвлечение элемента с начала:')
    print(timeit('pop_left(a)', number=10000, globals=globals()))
    print(timeit('pop_left(b)', number=10000, globals=globals()))
    print('\nИзвлечение элемента по случаному индексу:')
    print(timeit('get_el(a, c)', number=10000, globals=globals()))
    print(timeit('get_el(b, c)', number=10000, globals=globals()))
