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
import numpy as np


class ListClass:

    def __init__(self):
        self.elems = []

    def fill(self, elems):
        start_time = time.time()
        for el in elems:
            self.elems.append(el)
        return "--- %s seconds ---" % (time.time() - start_time)

    def delete(self, el):
        start_time = time.time()
        self.elems.remove(el)
        return "--- %s seconds ---" % (time.time() - start_time)


l = ListClass()
l.fill(np.random.randint(-10, 100, 100000000))
l.delete(78)


class DictClass:

    def __init__(self):
        self.elems = {}

    def fill(self, elems):
        start_time = time.time()
        for x in range(1, (len(elems) + 1)):
            self.elems[x] = elems[x - 1]
        return "--- %s seconds ---" % (time.time() - start_time)

    def delete(self, el):
        start_time = time.time()
        self.elems.pop(el)
        return "--- %s seconds ---" % (time.time() - start_time)

d = DictClass()
d.fill(np.random.randint(-10, 100, 100000000))
d.delete(45)

# List быстрее создается,чем dict, так как в dict идет расход времени и памяти на создание хэшей.
# Зато операции в dict, связанные с поиском элемента, выполняются быстрее, за константное время, в отличие от list
# Время выполнения в list — линейное.

