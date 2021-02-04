"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""

import time as t
import sys
sys.setrecursionlimit(5000)

# Part a)

def list_full(n, ll=[]):
    if n >= 9000:
        return ll
    else:
        ll.append(n)
        return list_full(n+3)



def dict_full(n, dict={}):
    if n >= 9000:
        return dict
    else:
        dict[n] = n+2
        return dict_full(n+3)

def measure():
    start = t.time()
    list_full(1)
    end = t.time()
    print(f'Total time for list: {end - start}')

    start = t.time()
    dict_full(1)
    end = t.time()
    print(f'Total time for dict: {end - start}')


measure()

# По заполнению результаты показывают что словарь заполняется немного быстрее чем список,
# потому что в словаре используется оптимизированный алгоритм с хещированием
#Part b)

def elem_to_string():
    start = t.time()
    a = list_full(1)
    for i in a:
        i = str(i)+'abs'
    end = t.time()
    print(f'Time for converting list elements to string: {end - start}')

    start = t.time()
    a = dict_full(1)
    for i, z in a.items():
        a[i] = str(z)+'abs'
    end = t.time()
    print(f'Time for converting dict values to string: {end - start}')

elem_to_string()


#Оценивая показатели после перебора и изменения элементов списка и словаря,
# словарь выглядит более быстрым вариантом так же как и в первом варианте



