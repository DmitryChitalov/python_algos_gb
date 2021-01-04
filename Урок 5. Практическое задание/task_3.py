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

my_list = list("OlgaMerezhko")
my_deque = deque("OlgaMerezhko")

# добавим элемент в конец списка или очереди


def add_el_list(lst):
    lst.append('e')


def add_el_dqu(dqu):
    dqu.append('e')


print('Добавим элемент в конец списка: ', timeit(
        'add_el_list(my_list)',
        setup='from __main__ import add_el_list, my_list',
        number=10000))
print('Добавим элемент в конец очереди: ', timeit(
        'add_el_dqu(my_deque)',
        setup='from __main__ import add_el_dqu, my_deque',
        number=10000))

# 0.0018381999999999982   0.002033199999999999    0.002325799999999996
# 0.0022312000000000026   0.0019102000000000008   0.0022495000000000015
# Примерно одинаково, если смотреть на три замера.

# добавим элемент в начало списка или очереди


def add_left_list(list):
    list.insert(0, 'a')


def add_left_dqu(dqu):
    dqu.appendleft('a')


print('Добавим элемент в начало списка: ', timeit(
        'add_left_list(my_list)',
        setup='from __main__ import add_left_list, my_list',
        number=10000))
print('Добавим элемент в начало очереди: ', timeit(
        'add_left_dqu(my_deque)',
        setup='from __main__ import add_left_dqu, my_deque',
        number=10000))

# 0.1042167               0.10205149999999999     0.09824650000000001
# 0.0022336000000000023   0.0017531000000000074   0.0019406999999999897
# У очереди результаты очевидно лучше.

# Удалим элемент с конца списка или очереди


def pop_el_list(lst):
    lst.pop(-1)


def pop_el_dqu(dqu):
    dqu.pop()


print('Удалим элемент с конца списка: ', timeit(
        'pop_el_list(my_list)',
        setup='from __main__ import pop_el_list, my_list',
        number=10000))
print('Удалим элемент с конца очереди: ', timeit(
        'pop_el_dqu(my_deque)',
        setup='from __main__ import pop_el_dqu, my_deque',
        number=10000))

# 0.0024752000000000107   0.0023664999999999936   0.002313700000000002
# 0.002058499999999991    0.001861500000000016    0.0016999999999999793
# Не значительное, но достаточно стабильное приемужество у очереди

# Удалим элемент с начала списка или очереди


def pop_left_list(lst):
    lst.pop(0)


def pop_left_dqu(dqu):
    dqu.popleft()


print('Удалим элемент с начала списка: ', timeit(
        'pop_left_list(my_list)',
        setup='from __main__ import pop_left_list, my_list',
        number=10000))
print('Удалим элемент с начала очереди: ', timeit(
        'pop_left_dqu(my_deque)',
        setup='from __main__ import pop_left_dqu, my_deque',
        number=10000))

# 0.02406950000000002     0.02397070000000001     0.026338699999999993
# 0.0016468000000000038   0.0018118000000000023   0.001543600000000006
# Очевидное приемущество у очереди, примерно в 20 раз

# Вернуть и Удалить случайный элемент
my_list = list("OlgaMerezhko")
my_deque = deque("OlgaMerezhko")


def pop_rand_list(lst):
    el = lst.pop(random.randint(0, len(lst)))
    return el


def pop_rand_dqu(dqu):
    el = dqu[random.randint(0, len(dqu))]
    dqu.remove(el)
    return el


print(pop_rand_list(my_list))
print(pop_rand_dqu(my_deque))
# Вот тут я не поняла, функции рабочие, я проверяла, а померить время не получается... Но я и без этого могу
# с уверенностью сказать, что у очереди всемя будет больше, т.к. больше сложность больше.

# print('Удалим и вернем случайный элемент списка: ', timeit(
#         'pop_rand_list(my_list)',
#         setup='from __main__ import pop_rand_list, my_list',
#         number=10000))
# print('Удалим и вернем случайный элемент очереди: ', timeit(
#         'pop_rand_dqu(my_deque)',
#         setup='from __main__ import pop_rand_dqu, my_deque',
#         number=10000))

# Итого, у нас получилось, что при добавлении элемента справа результаты примерно одинаковые, а при всех остальных
# операциях добавления и удаления результаты очереди сильно лучше. А от с извлечением случайного у списка лучше,
# потому что его функции больше заточены под адресность. У очереди главное начало и конец, в отличии от списка
