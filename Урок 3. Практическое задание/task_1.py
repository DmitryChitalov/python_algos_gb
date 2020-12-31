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


def filling_list(n):
    start_val = time.time()
    lst = []
    for i in range(n):
        lst.append(i)
    end_val = time.time()
    return end_val - start_val, type(lst), len(lst)


def filling_dict(n):
    start_val = time.time()
    dct = {}
    for i in range(n):
        dct[i] = i
    end_val = time.time()
    return end_val - start_val, type(dct), len(dct)


print(filling_list(1000))
print(filling_dict(1000))
'''
filling_list   # 0.0001239776611328125   список
filling_dict   # 0.00014328956604003906  словарь
Вывод: создание списка происходит быстрее, чем в словаре,
'''
