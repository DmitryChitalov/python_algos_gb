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
import timeit

my_list = [el for el in range(5)]
my_deque = deque([el for el in range(5)])

# deque заточена на извлечение и добавление элементов с обоих концов списка, но заметная разница появляется при
# добавлении или удалении элемента в начале списка - appendleft вместо insert и popleft вместо remove.

print('my_list.append: ', timeit.timeit("my_list.append(1)", "from __main__ import my_list", number=10000))
print('my_list.index: ', timeit.timeit("my_list.index(1)", "from __main__ import my_list", number=10000))
print('my_list.pop: ', timeit.timeit("my_list.pop()", "from __main__ import my_list", number=10000))
print('my_list.insert: ', timeit.timeit("my_list.insert(0, 1)", "from __main__ import my_list", number=10000))
print('my_list.remove: ', timeit.timeit("my_list.remove(1)", "from __main__ import my_list", number=10000), '\n')


print('my_deque.append: ', timeit.timeit("my_deque.append(1)", "from __main__ import my_deque", number=10000))
print('my_deque.index: ', timeit.timeit("my_deque.index(1)", "from __main__ import my_deque", number=10000))
print('my_deque.pop: ', timeit.timeit("my_deque.pop()", "from __main__ import my_deque", number=10000))
print('my_deque.appendleft: ', timeit.timeit("my_deque.appendleft(1)", "from __main__ import my_deque", number=10000))
print('my_deque.popleft: ', timeit.timeit("my_deque.popleft()", "from __main__ import my_deque", number=10000))

