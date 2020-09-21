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


def speed_info(func):
    def wrapper(*args, **kwargs):
        start_val = time.time()
        print(start_val)
        func(*args, **kwargs)
        end_val = time.time()
        print(end_val)
        print(f' Время выполнения: {(end_val - start_val)} секунд.')

    return wrapper


class MyList:
    def __init__(self, n):
        self.mylist = []
        self.n = n

    @speed_info
    def list_filling(self):
        for i in range(self.n):
            self.mylist.append(random.randint(0, self.n))
        # print(self.mylist)
        return self.mylist

    @speed_info
    def item_search(self, itm):
        if itm in self.mylist:
            # print(self.mylist.index(itm))
            return self.mylist.index(itm)
        else:
            return None

    @speed_info
    def item_add(self, itm):
        self.mylist.append(itm)
        # print(self.mylist)
        return self.mylist

    @speed_info
    def item_remove(self):

        return self.mylist.pop()


class MyDict:
    def __init__(self, n):
        self.mydict = {}
        self.n = n

    @speed_info
    def list_filling(self):
        for i in range(self.n):
            self.mydict[i] = chr(random.randint(0, self.n)) * 3
        # print(self.mydict)
        return self.mydict

    @speed_info
    def item_search(self, itm):
        print(self.mydict.get(itm))
        return self.mydict.get(itm)

    @speed_info
    def item_add(self, itm, vol):
        self.mydict[itm] = vol
        # print(self.mydict)
        return self.mydict

    @speed_info
    def item_remove(self):
        print(self.mydict.popitem())
        return self.mydict.popitem()


n = 100000
lst = MyList(n)

lst.list_filling()
lst.item_add(15)
lst.item_remove()
lst.item_search(22)

dkt = MyDict(n)
dkt.list_filling()
dkt.item_add(15, 25689)
dkt.item_remove()
dkt.item_search(22)
""" Словарь  заполняется медленнее списка """
