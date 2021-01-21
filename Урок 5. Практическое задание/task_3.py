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

list_example = [x for x in range(10)]
deque_example = deque()
[deque_example.append(x) for x in range(10)]

print(list_example, deque_example)
help(deque)

print("Вставка справа в list занимает",
      timeit.timeit("list_example.append(1)", 'from __main__ import list_example', number=100))
print("Вставка справа в deque занимает:",
      timeit.timeit("deque_example.append(1)", 'from __main__ import deque_example', number=100))
print("Вставка слева в list занимает:",
      timeit.timeit("list_example.insert(0, 1)", 'from __main__ import list_example', number=100))
print("Вставка справа в deque занимает:",
      timeit.timeit("deque_example.appendleft(1)", 'from __main__ import deque_example', number=100))

print("Извлечение справа из list занимает:",
      timeit.timeit("list_example.pop()", 'from __main__ import list_example', number=100))
print("Извлечение справа из deque занимает:",
      timeit.timeit("deque_example.pop()", 'from __main__ import deque_example', number=100))
print("Извлечение слева из list занимает:",
      timeit.repeat("list_example.pop(0)", 'from __main__ import list_example', timeit.default_timer, 3, number=3))
print("Извлечение слева из deque занимает:",
      timeit.repeat("deque_example.popleft()", 'from __main__ import deque_example', timeit.default_timer, 3, number=3))

print("Доступ к случайному элементу из list:",
      timeit.timeit("list_example[0]", 'from __main__ import list_example', number=100))
print("Доступ к случайному элементу из deque:",
      timeit.timeit("deque_example[0]", 'from __main__ import deque_example', number=100))

"""
Как видно из чисел доступ к случайному элементу быстрее происходит из list, 
вставка быстрее у deque, скорость извлечения зависит от стороны извлечения
"""