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

# создаем список
def list_creator(n):
    lst = []
    start = time.time()
    for i in range(n):
        lst.append(i)
    end = time.time()
    print(f'время заполнения списка: {end - start}')
    return lst

# создаем словарь
def dict_creator(n):
    dct = {}
    start = time.time()
    for i in range(n):
        dct[i] = f'{i}'
    end = time.time()
    print(f'время заполнения словаря: {end - start}')
    return dct

def get_from_list_val (lst, n):
    result = None
    start = time.time()
    for i in lst:
        if lst[i] == n:
            result = n
    end = time.time()
    print(f'значение элемента:{n} , извлечен из списка за:  {end - start}')
    return result

def get_from_dict_val (dct, n):
    result = None
    start = time.time()
    for i in dct.values():
        if i == str(n):
            result = str(n)
    end = time.time()
    print(f'значение элемента:{n} , извлечен из словаря за:  {end - start}')

def get_from_list_ind (lst, n):
    result = None
    start = time.time()
    for i in range(len(lst)):
        if i == n:
            result = lst[i]
    end = time.time()
    print(f'значение индекса:{n} , извлечен из списка за:  {end - start}')
    return result

def get_from_dict_ind (dct, n):
    result = None
    start = time.time()
    for i in dct.keys():
        if i == n:
            result = dct.get(n)
    end = time.time()
    print(f'значение индекса:{n} , извлечен из словаря за:  {end - start}')
    return result

list_example = list_creator(1000000)
dict_example = dict_creator(1000000)

get_from_list_val(list_example, 5000000)
get_from_dict_val(dict_example, 5000000)

get_from_list_ind(list_example, 567899)
get_from_dict_ind(dict_example, 567899)

"""
заполнение листа происходит быстрее, извлечение элемента по значению происходит
быстрее из списка чем из словаря, но по индексу быстрее отработает словарь
"""
