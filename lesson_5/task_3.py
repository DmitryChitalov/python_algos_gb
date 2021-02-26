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


def my_list_append(n):
    for i in range(n):
        my_list.append(i)
    return my_list


def my_deque_append(n):
    for i in range(n):
        my_deque.append(i)
    return my_list


def my_list_insert(n):
    for i in range(n):
        my_list.insert(0, i)
    return my_list


def my_deque_insert(n):
    for i in range(n):
        my_deque.appendleft(i)
    return my_list


def my_list_popright(n):
    for i in range(n):
        my_list.pop(i)
    return my_list


def my_deque_popright(n):
    for i in range(n):
        my_deque.pop()
    return my_list


def my_list_popleft(n):
    for i in range(n):
        my_list.pop(0)
    return my_list


def my_deque_popleft(n):
    for i in range(n):
        my_deque.popleft()
    return my_list


def my_list_insertmid(n):
    for i in range(n):
        my_list.insert(len(my_list) // 2, i)
    return my_list


def my_deque_insertmid(n):
    for i in range(n):
        my_deque.insert(len(my_deque) // 2, i)
    return my_list


n = 10 * 3

my_list = [i for i in range(1, n)]
my_deque = deque(my_list)

print('добавление в конец списка')
print(timeit('my_list_append(n)', globals=globals(), number=10000))

print('добавление в конец очереди')
print(timeit('my_deque_append(n)', globals=globals(), number=10000))

print('добавление в начало списка')
print(timeit('my_list_insert(n)', globals=globals(), number=100))

print('добавление в начало очереди')
print(timeit('my_deque_insert(n)', globals=globals(), number=100))

print('удаление с конца списка')
print(timeit('my_list_popright(n)', globals=globals(), number=100))

print('удаление с конца очереди')
print(timeit('my_deque_popright(n)', globals=globals(), number=100))

print('удаление с начала списка')
print(timeit('my_list_popleft(n)', globals=globals(), number=100))

print('удаление с начала очереди')
print(timeit('my_deque_popleft(n)', globals=globals(), number=100))

print('вставка в середину списка')
print(timeit('my_list_insertmid(n)', globals=globals(), number=100))

print('вставка в середину очереди')
print(timeit('my_deque_insertmid(n)', globals=globals(), number=100))

"""
добавление в конец списка незначительно быстрее добавления в очередь
добавление в конец списка
0.031116199999999997
добавление в конец очереди
0.018694900000000014

добавление в начало очереди значительно (10**3 раз) быстрее такой же операции со списком 
добавление в начало списка
0.6698241
добавление в начало очереди
0.00018259999999992171


удаление с конца очереди значительно (10**3 раз) быстрее такой же операции со списком 
удаление с конца списка
0.22935210000000006
удаление с конца очереди
0.00017050000000007337


удаление с начала очереди значительно (10**3 раз) быстрее такой же операции со списком 
удаление с начала списка
0.21613140000000008
удаление с начала очереди
0.0001567000000000096


вставка в середину списка быстрее в 2 раза такой же операции с очередью 
вставка в середину списка
0.2831211
вставка в середину очереди
0.4560692000000002


Вывод: Deque приоритетьнее по скорости для использования в задачах, требующих действия по принципу FIFO 
"""
