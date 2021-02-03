"""
Задание 1.

Реализуйте заполнение списка и словаря, сделайте замеры и сделайте выводы, обоснуйте результат.
Сделайте несколько операций с каждым из объектов, сделайте замеры и сделайте выводы, обоснуйте результат.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
import time

def elapse_list(func):
    def measure(i_a, i_b, i_c):
        l_start = time.time()
        func(i_a, i_b, i_c)
        l_end = time.time()
        l_elapsed = (l_end - l_start)*1000000
        print(f'Elapsed time(ns) for <{func.__name__}>: {l_elapsed}.')
    return measure

def elapse_dict(func):
    def measure(i_a, i_b, i_c, i_d):
        l_start = time.time()
        func(i_a, i_b, i_c, i_d)
        l_end = time.time()
        l_elapsed = (l_end - l_start)*1000000
        print(f'Elapsed time(ns) for <{func.__name__}>: {l_elapsed}.')
    return measure

@elapse_list
def add_list(i_lst, i_item, i_cnt=0):
    # time.sleep(0.3)
    if i_cnt == 0:
        i_cnt = 1

    for i in range(i_cnt):
        i_lst.append(i_item)

@elapse_dict
def add_dict(i_dct, i_start, i_value, i_cnt=0):
    # time.sleep(0.3)
    if i_cnt == 0:
        i_cnt = 1

    for i in range(i_cnt):
        i_dct[i_start+i] = i_value


g_lst = []
g_dct = {}

add_list(g_lst, 'item_1', 50500)
add_dict(g_dct, 0, 'item_1', 50500)

print(len(g_lst))
print(len(g_dct))
######################################################################
# Время, потраченное на заполнении списка или словаря объектами в
# количестве до 5-10 тысяч, равно нулю, хотя уж наносекунды должно длиться.
# Вывод 1: функция time.time() имеет, видимо, како-то лаг и
# для замеров быстрых операций не подходит.
# Вывод 2: заполнение словаря занимает по времени несколько раз больше,
# чем списка.
######################################################################
