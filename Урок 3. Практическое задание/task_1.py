"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
# Заполнение списка вышло медленее

import time


def list_fill(num):
    new_list = []
    start_time = time.time()
    for i in range(num):
        new_list.append(i)
    finish_time = time.time()
    print(f"Начало {start_time}, конец {finish_time}, разница {finish_time - start_time}")


def dict_fill(num):
    new_dict = {}
    start_time = time.time()
    for i in range(num):
        new_dict[i] = i
    finish_time = time.time()
    print(f"Начало {start_time}, конец {finish_time}, разница {finish_time - start_time}")


list_fill(1000000)
dict_fill(1000000)

