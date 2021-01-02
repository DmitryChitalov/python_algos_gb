
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

test_dic = {}
test_list = []

def excute_time(func):
    def wrapped(*args):
        start_time = time.time()
        result = func(*args)
        end_time = time.time()
        print(end_time - start_time)
    return wrapped


@excute_time
def insert_dic(dic):
    for a in range(1000):
        k=str(a+1)+' '+'val'
        test_dic[k] = a
    print(test_dic)

@excute_time
def insert_list(list):
    for i in range(1000):
        test_list.append(i)
    print(test_list)


insert_dic(test_dic)
insert_list(test_list)
