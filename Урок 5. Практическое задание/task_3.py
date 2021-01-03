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


def list_add(raw_list):
    result = []
    return [result.append(i) for i in raw_list]


def list_ins(raw_list):
    result = raw_list.copy()
    return [result.insert(0, i) for i in raw_list]


def list_get(raw_list):
    for i in range(len(raw_list)-1):
        raw_list[i]


def list_pop(raw_list):
    while len(raw_list):
        raw_list.pop()


def deque_add(raw_deq):
    result = deque()
    return [result.append(i) for i in raw_deq]


def deque_ins(raw_deq):
    result = raw_deq.copy()
    return [result.appendleft(i) for i in raw_deq]


def deque_get(raw_deq):
    for i in range(len(raw_deq) - 1):
        raw_deq[i]


def deque_pop(raw_deq):
    while len(raw_deq):
        raw_deq.pop()


test_list = [i for i in range(10000)]
test_deq = deque(test_list)
print('Результаты для list: ')
for elem in ['add', 'ins', 'get', 'pop']:
    print(timeit(f'list_{elem}(test_list)', f'from __main__ import list_{elem}, test_list', number=100))
print('Результаты для deque: ')
for elem in ['add', 'ins', 'get', 'pop']:
    print(timeit(f'deque_{elem}(test_deq)', f'from __main__ import deque_{elem}, test_deq', number=100))


"""
Результаты для list: 
0.0599928
6.0691257
0.07163620000000037
0.0013395999999996633
Результаты для deque: 
0.06840340000000023
0.07499559999999938
0.08443690000000004
0.0009726999999992714

Результаты замеров для вышеприведенного кода подтверждают указанное в задании правило - deque во много раз превосходит
по скорости добавления новых элементов, особенно в начало (практически в 100 раз). Так же извлечение элементов в 
deque работает быстрее.
Однако случайный доступ (обращение по индексу) быстрее у стандартного list, если при этом не происходит изменения длины. 
"""