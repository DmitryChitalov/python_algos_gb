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


# Ответ - список строится быстрее, потому что в словаре идёт (кроме размещения элементов) вычисление хеша.
# Словари в Python устроены как хеш-таблицы.

#решение моё предельно конкретное, а не общее; также я использовала модуль timeit за простоту

import timeit

def a_list(l):          #заполняет элементами список
    return list(l)

def a_dict(l):           #заполняет элементами словарь
    return dict.fromkeys(l)

k = ('itcouldbebetterbutno')

print(k)
print(a_list(k))
print(a_dict(k))
print(timeit.timeit("a_list(k)", setup="from __main__ import a_list, k", number=10000))
print(timeit.timeit("a_dict(k)", setup="from __main__ import a_dict, k", number=10000))

#Видно, что словарь заполняется дольше

