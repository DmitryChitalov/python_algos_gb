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

from timeit import timeit, repeat, default_timer



setup = '''
from collections import deque
elements = range(1000)
my_dec = deque()
my_list = []
'''
statments = [
    '''
for el in elements:
    my_list.append(el)
''',
    '''
for el in elements:
    my_dec.append(el)
''',
    '''
for el in elements:
    my_list.insert(0, el)
''',
    '''
for el in elements:
    my_dec.appendleft(el)
'''
]
for st in statments:
    print(repeat(st, setup, default_timer, 3, 100))

setup1 = '''
from collections import deque
elements1 = range(100000)
my_dec1 = deque()
for el in elements1:
    my_dec1.append(el)
my_list1 = []
for el in elements1:
    my_list1.append(el)
'''


statments1 = [
    '''
my_list1.pop()
''',
    '''
my_dec1.pop()
''',
    '''
my_list1.pop(0)
''',
    '''
my_dec1.popleft()
'''

]
for st in statments1:
    print(repeat(st, setup1, default_timer, 3, 10000))

'''
Исходя из замеров можно сделать вывод что основные операции со списками такие как append и pop делаются 
практически одинаково. Но удалить с головы или добавить в голову в deque делается существенно быстрее.
Поэтому если нужно чо то втавить или удалить из начала списка нужно воспользоваться deque
'''