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
import timeit
from collections import deque
from random import randint

new_lst = []
lst_deque = deque()

for i in range(1000):
    new_lst.append(i)
    lst_deque.append(i)

print(timeit.timeit('new_lst',
                    setup='from __main__ import new_lst',
                    number=1000000))   # 0.02103674099998898

print(timeit.timeit('lst_deque',
                    setup='from __main__ import lst_deque',
                    number=1000000))   # 0.016052523998951074

print(timeit.timeit('new_lst[randint(0, 999)]',
                    setup='from __main__ import new_lst, randint',
                    number=1000000))   # 0.8183468889983487

print(timeit.timeit('lst_deque[randint(0, 999)]',
                    setup='from __main__ import lst_deque, randint',
                    number=1000000))   # 0.827682030001597

'''
По итогам замера доказано, что:
создание списка происходит быстрее у collections.deque,
а обращение по случайному элементу у list
'''
