"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""

from collections import deque
from timeit import timeit

list_obj = list("bcd")
deque_obj = deque(list_obj)

print('list_obj:', list_obj)
print('deque_obj:', deque_obj, '\n')

str_alphabet = 'абвгдеёжзиклмнопрстуфхцчшщэюя1234567890abcdefghijklmnopqrstuvwxyz1234567890'


def list_or_deque_append(list_or_deque_data, list_with_obg):
    for obj in list_with_obg:
        list_or_deque_data.append(obj)
    return list_or_deque_data


# # добавление эл-ов в конец
# list_alphabet = list((str_alphabet + str_alphabet.upper()) * 10)
# print('Длинна добавляемого списка: ', len(list_alphabet), 'элементов, 10 тысяч повторений')
# t1 = timeit("list_or_deque_append(list_obj, list_alphabet)", globals=globals(), number=10000)
# t2 = timeit("list_or_deque_append(deque_obj, list_alphabet)", globals=globals(), number=10000)
# print('%.2f Список, добавление в конец' % t1)  # 1.21
# print('%.2f Дека, добавление в конец\n' % t2)  # 0.87 при добавлении эл-ов в конец, скорость деки выше в 1,39 раза


def list_insert(list_data, list_with_obg):
    for obj in list_with_obg:
        list_data.insert(0, obj)


def deque_append_left(deque_data, list_with_obg):
    for obj in list_with_obg:
        deque_data.appendleft(obj)


# # добавление эл-ов в начало
# list_alphabet = list((str_alphabet + str_alphabet.upper()) * 10)
# print('Длинна добавляемого списка: ', len(list_alphabet), 'элементов, 100 повторений')
# t1 = timeit("list_insert(list_obj, list_alphabet)", globals=globals(), number=100)
# t2 = timeit("deque_append_left(deque_obj, list_alphabet)", globals=globals(), number=100)
# print('%.2f Список, добавление в начало' % t1)  # 3.41
# print('%.3f Дека, добавление  в начало\n' % t2)  # 0.008 при добавлении эл-ов в начало, скорость деки выше в 426


def list_del_left(list_data):
    for _ in range(len(list_data)):
        del list_data[0]


def list_pop_left(list_data):
    for _ in range(len(list_data)):
        list_data.pop(0)


def deque_pop_left(deque_data):
    for _ in range(len(deque_data)):
        deque_data.popleft()


# # удалеине эл-ов
# list_alphabet = list((str_alphabet + str_alphabet.upper()) * 1200)
# num_of_rep = 200
#
# big_list_obj_1 = list_or_deque_append(list_obj, list_alphabet)
# print('Длинна очищаемого списка: ', len(big_list_obj_1), f'элементов, {num_of_rep} повторений')
# t1 = timeit("list_del_left(big_list_obj_1)", globals=globals(), number=num_of_rep)
# print('%.2f Список, удаление слева методом del' % t1)  # 1.41
#
# big_list_obj_2 = list_or_deque_append(list_obj, list_alphabet)
# t2 = timeit("list_pop_left(big_list_obj_2)", globals=globals(), number=num_of_rep)
# print('%.2f Список, удаление слева методом pop' % t2)  # 1.46
# # удалеине эл-ов из списка методами del и pop почти одинкоавые по времени
#
# big_deque_obj = list_or_deque_append(deque_obj, list_alphabet)
# t3 = timeit("deque_pop_left(big_deque_obj)", globals=globals(), number=num_of_rep)
# print('%.3f Дека, удаление слева методом popleft\n' % t3)  # 0.012
# # удаление эл-ов из деки в 122 раза быстрее чем из списка


def list_or_deque_reverse(list_or_deque_data):
    list_or_deque_data.reverse()


# # проверка на реверс
# list_alphabet = list((str_alphabet + str_alphabet.upper()) * 90000)
# num_of_rep = 200
#
# big_list_obj = list_or_deque_append(list_obj, list_alphabet)
# print('Длинна реверсируемого списка: ', len(big_list_obj), f'элементов, {num_of_rep} повторений')
# t1 = timeit("list_or_deque_reverse(big_list_obj)", globals=globals(), number=num_of_rep)
# print('%.2f Список, reverse' % t1)  # 2.01
#
# big_deque_obj = list_or_deque_append(deque_obj, list_alphabet)
# print('\nДлинна реверсируемого дека: ', len(big_deque_obj), f'элементов, {num_of_rep} повторений')
# t2 = timeit("list_or_deque_reverse(big_deque_obj)", globals=globals(), number=num_of_rep)
# print('%.2f Дека, reverse' % t2)  # 2.72 а вот реверс данных спискаем даётся в 1,35 раз быстрее.

# # получение эл-ов
# list_alphabet = list((str_alphabet + str_alphabet.upper()) * 90000)
# num_of_rep = 200
#
# big_list_obj = list_or_deque_append(list_obj, list_alphabet)
# big_deque_obj = list_or_deque_append(deque_obj, list_alphabet)
# print('Длинна списка: ', len(big_list_obj), f'элементов, {num_of_rep} повторений')
# central_num = int(len(list_alphabet) / 2)
#
# print('Время на получение среднего эл-та:')
# t1 = timeit("big_list_obj[central_num]", globals=globals(), number=num_of_rep)
# print('%.6f Список' % t1)  # 0.000019
#
# t2 = timeit("big_deque_obj[central_num]", globals=globals(), number=num_of_rep)
# print('%.2f Дека' % t2)  # 1.21 получение центрального эл-та из деки может быть в 16 тысяч раз дольше, чем из списка
#
# num_of_rep = 2000000
# print('\nВремя на получение первого элемента с конца')
# t1 = timeit("big_list_obj[-1]", globals=globals(), number=num_of_rep)
# print('%.2f Список' % t1)  # 0.10 Список
#
# t2 = timeit("big_deque_obj[-1]", globals=globals(), number=num_of_rep)
# print('%.2f Дека' % t2)  # 0.09 Дека
#
# lust_index = len(big_deque_obj) - 1
#
# print('\nВремя на получение последнеего элемента')
# t1 = timeit("big_list_obj[lust_index]", globals=globals(), number=num_of_rep)
# print('%.2f Список' % t1)  # 0.13 Список
#
# t2 = timeit("big_list_obj[lust_index]", globals=globals(), number=num_of_rep)
# print('%.2f Дека\n' % t2)  # 0.13 Дека если брать последний эл-т по индексу, то время выполнения вырастет в 1,3 раза

'''
Итоги:
Плюсы Деки по отношению к списку:
+ при добавлении эл-ов в конец, скорость деки выше в 1,39 раза
+ при добавлении эл-ов в начало, скорость деки выше в 426 раз
+ удаление эл-ов из деки в 122 раза быстрее чем из списка

Плюсы Списков по отношению к деки:
+ получение элементов из списка может быть в 16 тысяч быстрее, чем из Деки

Доп. наблюдения:
а если брать последний эл-т по индексу указывая -1 элемент, вместо его порядкового номера,
то время выполнения может сократится до 1,3 раза
'''
