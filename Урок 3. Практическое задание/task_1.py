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
from random import choices
from string import ascii_letters


def with_timing(func):
    def timing_wrapper(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        return t2 - t1
    return timing_wrapper


@with_timing
def add_to_dict(dictionary, key, el):
    dictionary[key] = el


@with_timing
def add_to_list(target_list, el):
    target_list.append(el)


dic_time = 0
lst_time = 0
dic = dict()
lst = list()
for i in range(5000000):
    rand_el = ''.join(choices(ascii_letters, k=5))
    dic_time += add_to_dict(dic, rand_el, rand_el)
    lst_time += add_to_list(lst, rand_el)

print(dic_time)
print(lst_time)

"""
2.6437435150146484 for dict if key = rand_el
1.2684946060180664 for list

1.2981338500976562 for dict if key = i
1.2764840126037598

Добавление в список более чем в два раза быстрее, чем добавление в словарь по  
Обоснование - необходимость расчета хэша для ключа словаря
Однако, если в качестве ключа используются уникальные числа, подобно индексам массива,
то добавление в словарь совсем немного медленнее, чем добавление в список, наверное hash(int) = int?
Вывод: если присутствуют частые операции добавления, то словарь, возможно, не лучший выбор
"""