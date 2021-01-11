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


print('Время выполнения операций с deque: ',timeit('''
from collections import deque
lst = [x*2 for x in range(100)]
deq = deque(lst)

deq.append(1)
deq.appendleft(20)
deq.pop()
deq.popleft()
deq.reverse()
sum(deq)
deq.clear()'''))


print('Время выполнения операций с списком: ', timeit('''
lst = [x*2 for x in range(100)]
lst.append(1)
lst.insert(0, 20)
lst.pop()
lst.pop(0)
lst.reverse()
sum(lst)
lst.clear()'''))

'''Как мы видим из тестов, работа со списком немного быстрее, чем с deque'''