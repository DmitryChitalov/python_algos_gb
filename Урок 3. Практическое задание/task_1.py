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

lists = []

def decor(func):
    def result(*args, **kwargs):
        start=time()
        res = func(*args, **kwargs)
        end=time()
        return res, str(end - start)
    return result

@decor
def create_spisok(lists):
    for i in range(100,100000):
        lists.append(i)
    return lists
@decor
def create_slovar(lists):
    create_spisok(lists)
    b=0
    ind = []
    while len(lists) >= b:
        ind.append(b)
        b+=1
    slovar = dict(zip(ind, lists))
    return slovar

lists_l, lists_time = create_spisok(lists)
slovar_l, slovar_time = create_slovar(lists)

print("Создание списка 100-100000 заняло : "+ lists_time)
print("Создание словаря 100-100000 заняло: " + slovar_time)


@decor
def get_values_spisok(lists_l):
    res_lists_l= []
    v_rd = [randint(0, 100000 - 1) for i in range(10000)]
    for v in v_rd:
        res_lists_l.append(lists_l[v])
    return res_lists_l

@decor
def get_values_slovar(slovar_l):
    res = []
    v_rd = [randint(0, 100000 - 1) for i in range(10000)]
    for v in v_rd:
        res.append(slovar_l.get(v))
    return res

lists_v, lists_v_time = get_values_spisok(lists_l)
slovar_v, slovar_time = get_values_slovar(slovar_l)

print("Найти рандомных 10000 чисел из списка по индексу заняло: " + lists_v_time)
print("Найти рандомных 10000 чисел из словаря по индексу заняло: " + slovar_time)

#Заполнение листа происходит быстрее т.к. он не хэширует.
#Работа с данными происходит быстрее в словаре т.к. перебор и обращение к данным словаря быстрее.
