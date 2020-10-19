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
from collections import deque
import random

my_len = random.randint(1000, 10000)
print(f'Len = {my_len}')
start_time = timeit()
add_len = random.randint(10000, 100000)
print(f'Add len = {add_len}')
my_str = ''
for i in range(my_len):
    my_str += f'{i}'

def list_creator(_len):
    return [i**2 for i in range(_len)]

def list_creator_v2(data: str):
    return list(data)

def deq_creator(_len):
    return deque([i**2 for i in range(_len)])

def deq_creator_v2(data: list):
    return deque(data)

def list_add(ed_list: list, data):
        ed_list.append(data)

def deq_add(ed_deque: deque, data):
        ed_deque.append(data)

def rand_reader(data, num):
    max_idx = len(data) - 1
    while num > 0:
        data[random.randint(0, max_idx)]
        num -= 1

def rand_taker_l(data: list, num):
    while num > 0:
        data.pop()
        num -= 1

def rand_taker_d(data: deque, num):
    while num > 0:
        data.popleft()
        num -= 1

my_list = list_creator(my_len)
my_deq = deq_creator(my_len)

print('Время создания List')
print(timeit('list_creator(my_len)', setup="from __main__ import list_creator, my_len ", number=10000))
print('Время создания List V2')
print(timeit('list_creator_v2(my_str)', setup="from __main__ import list_creator_v2, my_str ", number=10000))
print('Время создания Deque')
print(timeit('deq_creator(my_len)', setup="from __main__ import deq_creator, my_len ", number=10000))
print('Время создания Deque v2')
print(timeit('deq_creator_v2(my_list)', setup="from __main__ import deq_creator_v2, my_list ", number=10000))

add_list = list_creator(add_len)
add_deq = deq_creator(add_len)
print('Время добавления в List')
print(timeit('list_add(my_list, add_list)', setup="from __main__ import list_add, my_list, add_list ", number=10000))
print('Время добавления в Deque')
print(timeit('deq_add(my_deq, add_deq)', setup="from __main__ import deq_add, my_deq, add_deq ", number=10000))
list_add(my_list, add_list)
deq_add(my_deq, add_deq)

print('Время чтения из List 1000 раз')
print(timeit('rand_reader(my_list, 1000)', setup="from __main__ import rand_reader, my_list ", number=10000))
print('Время чтения из Deque 1000 раз')
print(timeit('rand_reader(my_deq, 1000)', setup="from __main__ import rand_reader, my_deq ", number=10000))
rand_reader(my_list, 1000)
rand_reader(my_deq, 1000)

print('Время возврата из List 100 раз')
print(timeit('rand_taker_l(my_list, 100)', setup="from __main__ import rand_taker_l, my_list ", number=20))
print('Время возврата из Deque 100 раз')
print(timeit('rand_taker_d(my_deq, 100)', setup="from __main__ import rand_taker_d, my_deq ", number=20))
rand_taker_l(my_list, 100)
rand_taker_d(my_deq, 100)

"""
Len = 4174
Add len = 11108
Время создания List
7.428107594001631
Время создания List V2
0.8520447200025956
Время создания Deque
7.6023827229983
Время создания Deque v2
0.2007590329994855
Время добавления в List
0.0007986199998413213
Время добавления в Deque
0.0007656079978914931
Время чтения из List 1000 раз
5.7660079229972325
Время чтения из Deque 1000 раз
6.722321732999262
Время возврата из List 100 раз
0.00013132699677953497
Время возврата из Deque 100 раз
0.00012003500160062686

Для использования преимуществ каждого из типов хранения данных необходимо верно использовать их
сильные стороны
Создание методом генераторных выражений даёт примерно равный результат
Однако, преобразование типов для Deque происходит быстрее
Случайное чтение быстрее для списка, а возврат - для Deque

Судя по полученным данным, заявленные утверждения из документации подтверждаются 
"""