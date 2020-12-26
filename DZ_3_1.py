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

# Реализация данной задачи через модуль timeit

import timeit

test_list = """
a = range(1000)
b = []
for i in a:
    b.append(i)
    b.index(i)
"""

test_dict = """
a = range(1000)
dict_obj = dict()
for i in a:
    dict_obj[i] = i
    dict_obj.get(i)
"""

elapsed_time_list = timeit.timeit(test_list, number=100) / 10
print(f"Обработка списка заняло {elapsed_time_list}")
elapsed_time_dict = timeit.timeit(test_dict, number=100) / 10
print(f"Обработка словаря заняло {elapsed_time_dict}")

#  Очевидно, что обработка словаря происходит быстрее, чем обработка списка!
