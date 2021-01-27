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

Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям

И добавить аналитику, так ли это или нет.!
"""
from timeit import timeit
from collections import deque


def deque_append():
    d = deque()
    for i in range(100):
        d.append(i)


def list_append():
    l = list()
    for i in range(100):
        l.append(i)


def deque_append_left():
    d = deque()
    for i in range(100):
        d.appendleft(i)


def list_append_left():
    l = list()
    for i in range(100):
        l.insert(0, i)


def deque_pop():
    for _ in range(len(d)):
        d.pop()


def list_pop():
    for _ in range(len(l)):
        l.pop()


def deque_pop_left():
    for _ in range(len(d)):
        d.popleft()


def list_pop_left():  # На самом деле не pop, возвращает значение
    for _ in range(len(l)):
        r = l[0]
        del l[0]


def deque_get_el():
    for _ in range(len(d)):
        pass


def list_get_el():
    for _ in range(len(l)):
        pass


def deque_extend():
    d = deque()
    d.extend(l)


def list_extend():
    ll = list()
    ll.extend(l)


n = 1000000
d = deque()
for i in range(100):
    d.appendleft(i)
l = [i for i in range(100)]

print('deque_append()', timeit('deque_append()', globals=globals(), number=n))
print('list_append()', timeit('list_append()', globals=globals(), number=n))
print('deque_append_left()', timeit('deque_append_left()', globals=globals(), number=n))
print('list_append_left()', timeit('list_append_left()', globals=globals(), number=n))
for i in range(100):
    d.appendleft(i)
print('deque_pop()', timeit('deque_pop()', globals=globals(), number=n))
print('list_pop()', timeit('list_pop()', globals=globals(), number=n))
for i in range(100):
    d.appendleft(i)
print('deque_pop_left()', timeit('deque_pop_left()', globals=globals(), number=n))
l = [i for i in range(100)]
print('list_pop_left()', timeit('list_pop_left()', globals=globals(), number=n))
for i in range(100):
    d.appendleft(i)
print('deque_get_el()', timeit('deque_get_el()', globals=globals(), number=n))
l = [i for i in range(100)]
print('list_get_el()', timeit('list_get_el()', globals=globals(), number=n))
l = [i for i in range(100)]
print('deque_extend()', timeit('deque_extend()', globals=globals(), number=n))
l = [i for i in range(100)]
print('list_extend()', timeit('list_extend()', globals=globals(), number=n))


"""
Результаты:

deque_append() 3.5933700969908386
list_append() 3.9399394299834967
deque чуть медленнее list'a

deque_append_left() 3.588441881001927
list_append_left() 7.144101576996036
вставка слева у deque быстрее вдвое

deque_pop() 0.139009628968779
list_pop() 0.13830838998546824
забираем последний элемент за одинаковое время

deque_pop_left() 0.13672614604001865
list_pop_left() 0.13885816896799952
слева забираем элемент тоже одинаково быстро

deque_get_el() 2.9137129909940995
list_get_el() 2.6210955909918994
по индексу чуть дольше обращается deque

deque_extend() 0.47299577097874135
list_extend() 0.23948923201533034
расширять из итерируемого объекта вдвое быстрее list

deque нужно использовать если есть частое добавление слева, а остальных случаях ом такой же как лист или медленнее

"""
