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

import time


def string(numbers):
    first_time = time.time()
    elements = []
    for el in numbers:
        elements.append(el)
    second_time = time.time()
    print(f' Заполнение списка завершено за {second_time - first_time}')

def dictionary(numbers):
    first_time = time.time()
    elements = {}
    for el in numbers:
        elements[el] = el
    second_time = time.time()
    print(f'Заполнение словаря завершено за {second_time - first_time}')


numbers = [el for el in range(9999999)]
string(numbers)
dictionary(numbers)

#Не смог найти ошибку в коде, но у меня время каждый раз меняется (то список быстрее, то словарь)