"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
import time
import random

#start_time = time.time()


def gen_list(n):
    mass = []
    start = time.time()
    for i in range(n):
        mass.append(i)
    end = time.time()
    return f'время затрачено {end-start}'


def gen_dict(n):
    company_data = {}
    start = time.time()
    for i in range(n):
        company_name = f'Компания{i}'
        company_cost = random.randint(1000, 10000)
        company_data.update({company_name: company_cost})
    end = time.time()
    return f'время затрачено {end-start}'

'''
Время занимаемое для генерации списка меньше времени генерации словаря потому,
что под капотом python данные ключей словаря хешируется, нежели в списках где 
идет подсчет индекса элемента.
'''
print(gen_list(100000))
print(gen_dict(100000))