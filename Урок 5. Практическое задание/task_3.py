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

mass = [1, 2, 3, 4, 5, 6, 7, 8, 9]
deq_mass = deque(mass)

def mass_append(n):
    mass.append(n)

def deq_mass_append(n):
    deq_mass.append(n)

def mass_ins(n):
    mass.insert(0, n)

def deq_mass_appl(n):
    deq_mass.appendleft(n)

def mass_pop():
    mass.pop()

def deq_mass_pop():
    deq_mass.pop()

n = 345
print('append:1-list, 2-deque')
print(timeit.timeit("mass_append(n)", setup="from __main__ import mass_append, n"))  # 0.2300965000004
print(timeit.timeit("deq_mass_append(n)", setup="from __main__ import deq_mass_append, n"))  # 0.1716681
print('app_left\insert:1-list, 2-deque')
#print(timeit.timeit("mass_ins(n)", setup="from __main__ import mass_ins, n"))  # 0.23460007
print(timeit.timeit("deq_mass_appl(n)", setup="from __main__ import deq_mass_appl, n")) # 0.1984684
print('pop:1-list, 2-deque')
print(timeit.timeit("mass_pop()", setup="from __main__ import mass_pop"))  # 0.20381159999998
print(timeit.timeit("deq_mass_pop()", setup="from __main__ import deq_mass_pop"))  # 0.1568919999992

#операции с деком наглядно в два раза быстрее, чем соответствующие со списком