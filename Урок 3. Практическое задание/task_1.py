"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
from time import time
from random import randint


def timer(func):
    def f():
        start = time()
        func()
        finish = time()
        print(finish-start)
        print('*' * 100)
    f()


@timer
def operations_with_list():
    my_list = []
    for i in range(100):
        my_list.append(i)
    for i in range(100):
        my_list[i]
    for i in range(100):
        number1 = randint(0, 99)
        number2 = randint(0, 99)
        my_list[number1] = number2
    print(my_list)


@timer
def operations_with_dictionary():
    my_dictionary = {}
    for i in range(100):
        my_dictionary[i] = i
    for i in range(100):
        my_dictionary[i]
    for i in range(100):
        my_dictionary[randint(0, 99)] = randint(0, 99)
    print(my_dictionary)

operations_with_list
operations_with_dictionary