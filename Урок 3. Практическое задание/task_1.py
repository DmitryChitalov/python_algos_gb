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

list_l = [[1,2], ['a', 'b'], [24.0, 0.0]]
dict_d = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def fill_list(count):
    start = time()
    lst = []
    for i in range(count):
        lst.append(i)
    finish = time()
    result = finish - start
    return result

def fill_dict(count):
    start = time()
    dict_d = {}
    for i in range(count):
        dict_d[i] = i
    finish = time()
    result = finish - start
    return result

def list_list_2(obj):
    start = time()
    for k in obj:
        print(k)
    finish = time()
    result = finish - start
    return result

def dict_dict(obj):
    start = time()
    dec = obj.items()
    finish = time()
    result = finish - start
    return result, dec

# вывод всех значений 
print(list_list_2(list_l)) #0.00017905235290527344
print(dict_dict(dict_d)) #9.5367431640625e-07

# добавление значений 
print(fill_list(20)) # 5.9604644775390625e-06
print(fill_dict(20)) # 4.0531158447265625e-06


# При добавлении значений в словарь и список, когда значений 50, время вывода у словаря дольше. Когда значений 20, время вывода дольше у списка. 
