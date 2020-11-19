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
import random
from collections import deque
from timeit import timeit

deq_new = deque(random.sample(range(100), 10))
print(deq_new)

#Создаем очередь в deque
def completion_dq():
    deq = deque(random.sample(range(100), 5))
    return deq

# добавляем элемент в начало очереди deque
def app_dq():
    deq_new.appendleft('999')
    return deq_new

# перемещаем  элементы с конца очереди в начало deque
def rotat_dq():
    deq_new.rotate(2)
    return deq_new

# пoдсчитываем количесвто эллементов = 5
def count_dq():
    deq_new.count(5)
    return deq_new

# разворачиваем очередь
def reverse_dq():
    deq_new.reverse()
    return deq_new

###################################################

list_new = random.sample(range(100), 5)
print((list_new))

# создаем список
def completion_lst():
    lst = random.sample(range(100), 5)
    return lst

# добавляем элемент в начало списка
def app_lst():
    list_new.insert(6, 999)
    return deq_new

# перемещаем  элементы c начала в конец списка
def rotat_lst():
    new_1 = list_new[:2]
    del list_new[:2]
    list_new.append(new_1)
    return list_new

# пoдсчитываем количесвто эллементов = 5
def count_lst():
    list_new.count(5)
    return list_new

# разворачиваем список
def reverse_lst():
    list_new.reverse()
    return list_new

#################################################
print('сравнительная скорость работы по заполениею очереди и списка')
print(timeit('completion_dq()', setup='from __main__ import completion_dq', number=10000))
print(timeit('completion_lst()', setup='from __main__ import completion_lst', number=10000))

print('сравнительная скорость работы по добавлению элементов очереди и списка')
print(timeit('app_dq()', setup='from __main__ import app_dq', number=1000))
print(timeit('app_lst()', setup='from __main__ import app_lst', number=1000))

print('сравнительная скорость работы по перемещению элементов очереди и списка')
print(timeit('rotat_dq()', setup='from __main__ import rotat_dq', number=1000))
print(timeit('rotat_lst()', setup='from __main__ import rotat_lst', number=1000))

print('сравнительная скорость работы по подсчету определенных элементов очереди и списка')
print(timeit('count_dq()', setup='from __main__ import count_dq'))
print(timeit('count_lst()', setup='from __main__ import count_lst'))

print('сравнительная скорость работы по развороту элементов очереди и списка')
print(timeit('reverse_dq()', setup='from __main__ import reverse_dq', number=1000))
print(timeit('reverse_lst()', setup='from __main__ import reverse_lst', number=1000))