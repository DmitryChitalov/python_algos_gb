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
import random
from timeit import timeit

stand_lst = [random.randrange(0, 1000, 1) for i in range(1000)]
deq = deque(stand_lst)

def time_(lst_):
    #lst_=[]
    lst_.append(lst_)
    cp_lst_ = lst_.copy()
    lst_.count(lst_[0])
    cp_lst_.extend('12')
    lst_.index(lst_[0])
    lst_.insert(0,1)
    lst_.pop()
    lst_.remove(lst_[0])
    lst_.reverse()

print(timeit("time_(stand_lst)", setup="from __main__ import time_, stand_lst"))
print(timeit("time_(deq)", setup="from __main__ import time_, deq"))

# в среднем, отличия лежат в пределах [4:6] секунд,
# что достаточно значимо для миллиона замеров для функции с 10 операциями
# И это всё не в пользу deque