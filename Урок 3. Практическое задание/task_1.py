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

def time_of_function(function):
    def wrapped(*args):
        start_time = time.time()
        res = function(*args)
        print(f'{(time.time() - start_time):.5f}')
        return res
    return wrapped

@time_of_function
def create_list(iteration):
    fun_list = []
    for i in range(iteration):
        fun_list.append(random.randint(-iteration, iteration))
    return True

@time_of_function
def create_dict(iteretion):
    fun_dict = {}
    for i in range(iteretion):
        fun_dict[i] = random.randint(-iteretion, iteretion)
    return True


if __name__ == '__main__':
    # я использовал одиноковые функции для заполнения, что бы это не влияло на время
    # часто словарь заполняется быстрее, чем список, независимо количества итераций, возможно изза
    # функции аппенд, которая добавляет значение в конец списка
        for i in range(10,11010, 2000):
            print(f'for {i} iterations')
            create_list(i)
            create_dict(i)
