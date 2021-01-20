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
from timeit import timeit


def deq_append(deq=deque()):
    for i in range(1000):
        deq.append(i)


def deq_appendleft(deq=deque()):
    for i in range(1000):
        deq.appendleft(i)


def deq_pop(deq=deque()):
    for i in range(1000):
        deq.pop()


def deq_popleft(deq=deque()):
    for i in range(1000):
        deq.popleft()


def list_append(lst=list()):
    for i in range(1000):
        lst.append(i)


def list_appendleft(lst=list()):
    for i in range(1000):
        lst.insert(0, i)


def list_pop(lst=list()):
    for i in range(1000):
        lst.pop()


def list_popleft(lst=list()):
    for i in range(1000):
        lst.pop(0)


gl_deq = deque()
for i in range(1000):
    gl_deq.append(i)

gl_lst = list()
for i in range(1000):
    gl_lst.append(i)

print(f'deq_append:'
      f' {timeit("deq_append(gl_deq)", setup="from __main__ import deq_append, gl_deq", number=100)}')
print(f'list_append:'
      f' {timeit("list_append(gl_lst)", setup="from __main__ import list_append, gl_lst", number=100)}')


print(f'deq_appendleft:'
      f' {timeit("deq_appendleft(gl_deq)", setup="from __main__ import deq_appendleft, gl_deq", number=100)}')
print(f'list_appendleft:'
      f' {timeit("list_appendleft(gl_lst)", setup="from __main__ import list_appendleft, gl_lst", number=100)}')


print(f'deq_pop:'
      f' {timeit("deq_pop(gl_deq)", setup="from __main__ import deq_pop, gl_deq", number=100)}')
print(f'list_pop:'
      f' {timeit("list_pop(gl_lst)", setup="from __main__ import list_pop, gl_lst", number=100)}')


print(f'deq_popleft:'
      f' {timeit("deq_popleft(gl_deq)", setup="from __main__ import deq_popleft, gl_deq", number=100)}')
print(f'list_popleft:'
      f' {timeit("list_popleft(gl_lst)", setup="from __main__ import list_popleft, gl_lst", number=100)}')

"""
deq_append: 0.004794399999999997
list_append: 0.005011699999999994
deq_appendleft: 0.004531300000000002
list_appendleft: 5.8142244
deq_pop: 0.00549239999999962
list_pop: 0.005230700000000255
deq_popleft: 0.004728699999999364
list_popleft: 0.9150865000000001

Deque отрабатывает очень быстро на добавление в начало и конец значений, а так же их чтение
У List доступ к произвольному элементу требует все-таки значительное время по сравнению с чтением 
первого или последнего элемента у Deque. Добавление/удаление послежнего элемента в списке сравнимо с deque.
Работа по обращению к первому элементу - дольше"""
