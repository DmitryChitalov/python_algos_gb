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

"""
Заполнение словаря происходит медленнее чем заполнение списка, за счет работы хэш-функции
для каждого создаваемого ключа. Операции поиска и изменения данных в словаре происходят быстрее чем в списке, 
за счет прямого указания хеша ключа на его значения.
"""

import time


def dictionary_fill(count=100000, ky=1):
    dct = {}
    while count:
        dct[ky] = 'asd'
        count -= 1
        ky +=1
    return dct
start_time = time.time()
dictionary_fill()
print(f'заполнение словаря - {time.time() - start_time}')



def lst_fill(count=100000):
    lst = []
    while count:
        lst.append('asd')
        count -= 1
    return lst
start_time = time.time()
lst_fill()
print(f'заполнение списка - {time.time() - start_time}')


def dictionary_operations():
    dct = dictionary_fill()
    start_time = time.time()
    del dct[99989]
    print(f'удаление из словаря - {time.time() - start_time}')
    start_time = time.time()
    i = dct[99999]
    print(f'поиск в словаре - {time.time() - start_time}')

dictionary_operations()


def lst_operations():
    lst = lst_fill()
    start_time = time.time()
    del lst[99989]
    print(f'удаление из списка - {time.time() - start_time}')
    start_time = time.time()
    i = lst[99989]
    print(f'поиск в списке - {time.time() - start_time}')

lst_operations()