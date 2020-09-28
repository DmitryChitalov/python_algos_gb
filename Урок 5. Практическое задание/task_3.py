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
from timeit import repeat, timeit
from random import randint
import cProfile

my_list = [randint(-50, 200) for _ in range(30)]
deque_list = deque([randint(-50, 200) for _ in range(30)])
print(my_list)
print(deque_list)


def c_list():
    my_l = my_list.copy()
    return my_l


def deque_l():
    deque_l = deque_list.copy()
    return deque_l


def app_list():
    my_list = [randint(-50, 200) for _ in range(30)]
    num = randint(-100, 300)
    my_list.append(num)
    my_list.insert(0, num)
    return my_list


def app_deque():
    deque_list = deque([randint(-50, 200) for _ in range(30)])
    num = randint(-100, 300)
    deque_list.append(num)
    deque_list.appendleft(num)
    return deque_list


def reverse_l():
    my_list = [randint(-50, 200) for _ in range(30)]
    return my_list.reverse()


def reverse_d():
    deque_list = deque([randint(-50, 200) for _ in range(30)])
    return deque_list.reverse()


def count_l():
    my_list = [randint(-50, 200) for _ in range(30)]
    return my_list.count(15)


def count_d():
    deque_list = deque([randint(-50, 200) for _ in range(30)])
    return deque_list.count(15)


def main():
    c_list()
    deque_l()
    app_list()
    app_deque()
    reverse_l()
    reverse_d()
    count_l()
    count_d()


cProfile.run('main()')
print('Copy list', repeat('c_list', setup='from __main__ import c_list', repeat=5))
print('Copy deque', repeat('deque_l', setup='from __main__ import deque_l', repeat=5))
print('Добавление эл.', repeat('app_list', setup='from __main__ import app_list', repeat=5))
print('Добавление эл.', repeat('app_deque', setup='from __main__ import app_deque', repeat=5))
print('Реверс list', repeat('reverse_l', setup='from __main__ import reverse_l', repeat=5))
print('Реверс deque', repeat('reverse_d', setup='from __main__ import reverse_d', repeat=5))
print('Count list', repeat('count_l', setup='from __main__ import count_l', repeat=5))
print('Count deque', repeat('count_d', setup='from __main__ import count_d', repeat=5))


def main_func(func):
    print(repeat('main_func', setup='from __main__ import main_func', repeat=5))


@main_func
def c_list():
    my_l = my_list.copy()
    return my_l


@main_func
def deque_l():
    deque_l = deque_list.copy()
    return deque_l


@main_func
def app_list():
    my_list = [randint(-50, 200) for _ in range(30)]
    num = randint(-100, 300)
    my_list.append(num)
    my_list.insert(0, num)
    return my_list


@main_func
def app_deque():
    deque_list = deque([randint(-50, 200) for _ in range(30)])
    num = randint(-100, 300)
    deque_list.append(num)
    deque_list.appendleft(num)
    return deque_list


@main_func
def reverse_l():
    my_list = [randint(-50, 200) for _ in range(30)]
    return my_list.reverse()


@main_func
def reverse_d():
    deque_list = deque([randint(-50, 200) for _ in range(30)])
    return deque_list.reverse()


@main_func
def count_l():
    my_list = [randint(-50, 200) for _ in range(30)]
    return my_list.count(15)


@main_func
def count_d():
    deque_list = deque([randint(-50, 200) for _ in range(30)])
    return deque_list.count(15)
# cProfile не выявил уязвимых мест. В случае с timeit - только функции "copy" и "Count" в очереди deque отрабатывали быстрее.
#При применении мемоизации - все функции очереди-deque,  отработали намного быстрее чем обычный список.
# Copy list [0.02767260000000002, 0.026514200000000016, 0.0262637, 0.026527400000000007, 0.0268051]
# Copy deque [0.026249599999999984, 0.026345000000000007, 0.030384000000000022, 0.030696, 0.0306844]
# Добавление эл. [0.027468800000000015, 0.028085899999999997, 0.02701300000000001, 0.026777100000000054, 0.02640600000000004]
# Добавление эл. [0.026211500000000054, 0.025898100000000035, 0.029600599999999977, 0.025839999999999974, 0.026298500000000002]
# Реверс list [0.02585320000000002, 0.027702400000000016, 0.02723719999999996, 0.025902400000000103, 0.027166100000000082]
# Реверс deque [0.02716839999999998, 0.029285400000000017, 0.031014199999999992, 0.028352399999999944, 0.028287399999999963]
# Count list [0.0372648000000001, 0.0283720999999999, 0.02685549999999992, 0.028587499999999988, 0.027711800000000064]
# Count deque [0.027519700000000036, 0.02761289999999983, 0.029640800000000134, 0.028404899999999955, 0.028245999999999993]
# [0.037777300000000125, 0.03526370000000001, 0.036680899999999905, 0.03552409999999995, 0.03811720000000007]
# [0.029682200000000103, 0.03135930000000009, 0.02747860000000002, 0.02951450000000011, 0.0312945]
# [0.0355802999999999, 0.0340024000000001, 0.03408930000000021, 0.03532880000000005, 0.03580850000000013]
# [0.027009300000000014, 0.028688599999999953, 0.02872269999999988, 0.03084639999999994, 0.033716700000000044]
# [0.03621819999999998, 0.03683539999999996, 0.03865629999999998, 0.03665540000000034, 0.03788539999999996]
# [0.02836570000000016, 0.029684000000000044, 0.03168430000000022, 0.029878800000000094, 0.029428600000000138]
# [0.03426380000000018, 0.03437879999999982, 0.03539609999999982, 0.03598020000000002, 0.033711600000000175]
# [0.028301700000000096, 0.02861950000000002, 0.028136200000000056, 0.02791879999999969, 0.030133500000000257]
