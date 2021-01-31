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
test_list = [randint(1, 100) for num in range(1000)]
deq = deque(test_list)
print('Вставка в начало списка:')
print(timeit('test_list.insert(0,"abc")', globals=globals(), number=10000))
print(timeit('deq.appendleft("abc")', globals=globals(), number=10000))
print("Удаление первого элемента списка:")
print(timeit('test_list.pop(0)', globals=globals(), number=10000))
print(timeit('deq.popleft()', globals=globals(), number=10000))
print("Вставка последнего элемента списка:")
print(timeit('test_list.append(1)', globals=globals(), number=10000))
print(timeit('deq.append(1)', globals=globals(), number=10000))
print("доступ к случайному элементу:")
print(timeit('test_list[randint(0, 999)]', globals=globals(), number=10000))
print(timeit('deq[randint(0, 999)]', globals=globals(), number=10000))

"""
Использование дека дает преимущества при работе с первыми элементами.
При работе с последними элементами время выполнения примерно равно, как и при доступе к случайному элементу.
"""
