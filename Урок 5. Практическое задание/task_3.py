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

lst = [i for i in range(100)]
d = deque([i for i in range(100)])

print(timeit.timeit('d.append(1)', setup= 'from __main__ import d'))
print(timeit.timeit('d.append(2)', setup= 'from __main__ import d'))
print(timeit.timeit('d.append(3)', setup= 'from __main__ import d'))
print(timeit.timeit('d.append(4)', setup= 'from __main__ import d'))
print(timeit.timeit('d.append(5)', setup= 'from __main__ import d'))
#print(timeit.timeit(d.append(6)))  #ошибка
print(timeit.timeit('d.insert(100, 2)', setup= 'from __main__ import d'))
print(timeit.timeit('d.popleft()', setup= 'from __main__ import d'))
print(timeit.timeit('d.appendleft(566)', setup= 'from __main__ import d'))
print(timeit.timeit('d.extend(lst)', setup= 'from __main__ import d, lst')) #добавление списка
print(timeit.timeit('d.popleft()', setup= 'from __main__ import d')) # удаление с левой стороны
print(timeit.timeit('lst.append(5)', setup= 'from __main__ import lst'))
print(timeit.timeit('lst.pop(5)', setup= 'from __main__ import lst'))
print(timeit.timeit('lst.remove()', setup= 'from __main__ import lst'))
print(timeit.timeit('lst.extend(lst)', setup= 'from __main__ import lst'))

# Время затрачивается примерно одинаковое

