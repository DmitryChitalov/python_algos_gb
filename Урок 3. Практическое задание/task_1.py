"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

from random import randint


def func_decor(f):
    import time

    def control_tyme(n):
        start_val = time.time()
        my_list = f(n)
        end_val = time.time()
        return my_list, end_val - start_val

    return control_tyme


def fill_list(n):
    nums_list = [randint(0, 20) for i in range(n)]
    return nums_list


def fill_dict(n):
    nums_dic = {i: randint(0, 20) for i in range(n)}
    return nums_dic


f1 = func_decor(fill_list)
f2 = func_decor(fill_dict)
# при генерации 10 значений заполнение словаря происходит быстрее
print(f1(10))
print(f2(10))
# при заполнении большого числа элементов то заполнение списка происходит существенно быстрее
print(f1(1000))
print(f2(1000))
