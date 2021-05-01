"""
Задание 1.
Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
from random import sample

list = sample(range(-10, 11), 20)

print(list)

import timeit

code_to_test = """
a = range(100000)
b = []
for i in a:
    b.append(i*2)
"""

elapsed_time = timeit.timeit(code_to_test, number=100) / 100
print(elapsed_time)

for a in range(20):
    k = str(a + 1) + ' ' + 'may'
    d = {k: a}
    print(d)
print('Весь словарь имеет вид: ', d)

import timeit

code_to_test = """
a = range(100000)
b = []
for i in a:
    b.append(i*2)
"""

elapsed_time = timeit.timeit(code_to_test, number=100) / 100
print(elapsed_time)
