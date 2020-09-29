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
from random import randint
from collections import deque


def test_deque(arg, flag):
    deque_obj = deque(arg)
    if flag == 'last':
        deque_obj.append(randint(0, 100))
        return deque_obj.pop()
    elif flag == 'first':
        deque_obj.appendleft(randint(0, 100))
        return deque_obj.popleft()
    else: return deque_obj[(randint(0, 100))]


def test_list(arg, flag):
    arg = list(arg)
    if flag is 'last':
        arg.append(randint(0, 100))
        return arg.pop()
    elif flag == 'first':
        arg.insert(0,randint(0, 100))
        return arg.pop(0)
    else: return arg[(randint(0, 100))]
setup = 'from __main__ import test_list, test_deque, mylist'
mylist = list(range(101))

print(timeit('test_deque(mylist, "last")',setup))
'2.4490394569999996'
print(timeit('test_list(mylist, "last")', setup))
'2.201580571'
print(timeit('test_deque(mylist, "first")',setup))
'2.4347791070000007'
print(timeit('test_list(mylist, "first")', setup))
"2.515698265"
print(timeit('test_deque(mylist, "")',setup))
'2.3829177470000005'
print(timeit('test_list(mylist, "")', setup))
'2.02614185'
""" Анализ:
1. добвление последенго элемента и извлечение посленего элемента быстре у списка
2. добвление первого элемента и извлечение первого элемента быстре у deque
2. извлечение произвольного элемента быстре у списка
"""

