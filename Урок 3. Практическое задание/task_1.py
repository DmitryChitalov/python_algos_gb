"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

"""Импортируем модуль time"""

from time import time

"""Заполняем список программно и замеряем время его заполнения"""


# time_start=time.localtime(start)
# print(time_start.tm_min, time_start.tm_sec)

def my_gen_list(down, up):
    my_list = [y ** 2 for y in range(down, up)]
    # print(my_list)
    return my_list


time_start_list = time()
new_list = my_gen_list(0, 10000000)
time_stop_list = time()
# print(lists)
print(f'Время заполнения списка: {time_stop_list - time_start_list}')

"""Заполняем словарь программно и замеряем время его заполнения"""


def my_gen_dict(left, right):
    my_dict = {x: x ** 2 for x in range(left, right)}
    # print(my_dict)
    return my_dict


time_start = time()
new_dict = my_gen_dict(0, 10000000)
time_stop = time()

print(f'Время заполнения словаря: {time_stop - time_start}')

print('Операции со списком\n')

time_start_list = time()


def operation_list_1(lst):
    for i in range(len(lst)):
        if i == 999:
            print(lst[i])


operation_list_1(new_list)
time_stop_list = time()

print(f'Время на получение значения элемента  списка по индексу: {time_stop_list - time_start_list}')

time_start_list = time()


def operation_list_2(lst):
    for i in lst:
        if i == '999':
            print(i)


operation_list_2(new_list)
time_stop_list = time()
print(f'Время на получение индеса эелемента списка: {time_stop_list - time_start_list}')

print('Операции со словарем\n')

time_start = time()


def operation_dict_1(dct):
    i = dct[999]
    print(i)


operation_dict_1(new_dict)

time_stop = time()
print(f'Время получения значения по ключу словаря: {time_stop - time_start}')

time_start = time()
def operaition_dict_2(dict):
    for i in dict.values():
        if i == 999:
            print(i)
time_stop = time()
print(f'Время получения значения элемента  словаря: {time_stop - time_start}')

"""Выводы:
1)Словарь заполняется медленнее списка, потому что при добавлении элемента вычисляется еще и хеш его ключа.
2)Поиск элемента в словаре по ключу просходит быстрее, чем в списке по индексу
"""