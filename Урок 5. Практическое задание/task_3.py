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
from timeit import timeit

lst = [randint(1, 100) for i in range(50)]
dq = deque([randint(1, 100) for i in range(50)])

print('Замеры вставки элементов: ')
print(f'Список append:\t{timeit("lst.append(999)", setup="from __main__ import lst", number=10000)}')
print(f'Список insert в начало:\t{timeit("lst.insert(0, 999)", setup="from __main__ import lst", number=10000)}')
print(f'Очередь append:\t{timeit("dq.append(999)", setup="from __main__ import dq", number=10000)}')
print(f'Очередь appendleft:\t{timeit("dq.appendleft(999)", setup="from __main__ import dq", number=10000)}')
print(f'Список insert произвольно:\t{timeit("lst.insert(25, 999)", setup="from __main__ import lst", number=10000)}')

"""
Замеры вставки элементов: 
Список append:	0.004920399002003251
Список insert в начало:	0.21060303700141958
Очередь append:	0.0013309360001585446
Очередь appendleft:	0.0009664659992267843
Список insert произвольно:	0.2473680980001518
"""

print('Замеры удаления элементов: ')
print(f'Список pop:\t{timeit("lst.pop()", setup="from __main__ import lst", number=10000)}')
print(f'Список pop c началa:\t{timeit("lst.pop(0)", setup="from __main__ import lst", number=10000)}')
print(f'Очередь pop:\t{timeit("dq.pop()", setup="from __main__ import dq", number=10000)}')
print(f'Очередь popleft:\t{timeit("dq.popleft()", setup="from __main__ import dq", number=10000)}')
print(f'Список pop произвольно:\t{timeit("lst.pop(25)", setup="from __main__ import lst", number=10000)}')

"""
Замеры удаления элементов: 
Список pop:	0.001508262001152616
Список pop c началa:	0.11321323800075334
Очередь pop:	0.0007029309999779798
Очередь popleft:	0.0008152209993568249
Список pop произвольно:	0.032500467998033855
"""

print('Замеры функции reverse: ')
print(f'Список: {timeit("lst.reverse()", setup="from __main__ import lst", number=10000)}')
print(f'Очередь: {timeit("dq.reverse()", setup="from __main__ import dq", number=10000)}')

"""
Замеры функции reverse: 
Список: 0.0010985810004058294
Очередь: 0.0012469360008253716
"""
# Как показали замеры, очередь действительно выйгрывает по времени, на оперциях вставки/удаления, как в конец,
# так и в начало, при этом разница во времени довольно существенна.
# Фунция reverse в случае с очередью выполнилась медленнее.
# Вывод:
# если вам нужно что-то быстро дописать или вытащить, используйте deque
# - правило верно