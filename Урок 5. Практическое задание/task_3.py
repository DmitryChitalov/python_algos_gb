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
from random import randint
from collections import deque


test_list = [randint(1,100) for _ in range(1000)]
deq = deque(test_list)


print('Вставка в начало списка:')
print(timeit('test_list.insert(0,23)', 'from __main__ import test_list', number=10000))
print(timeit('deq.appendleft(23)', 'from __main__ import deq', number=10000))

print("Удаление первого элемента списка:")
print(timeit('test_list.pop(0)', 'from __main__ import test_list', number=10000))
print(timeit('deq.popleft()', 'from __main__ import deq', number=10000))

print("Вставка последнего элемента списка:")
print(timeit('test_list.append(1)', 'from __main__ import test_list', number=10000))
print(timeit('deq.append(1)', 'from __main__ import deq', number=10000))
"""
Результаты:
В случае, еогда требуется вставить или удалить какой либо элемент в начало списка
дек показывает огромное преимущество по скорости
При вставке в конец время выполнения не отличается
    Вставка в начало списка:
    0.026416949
    0.000673515999999999
    Удаление первого элемента списка:
    0.14283057
    0.00040707500000000674
    Вставка последнего элемента списка:
    0.0003925050000000152
    0.0004057450000000129
 
"""