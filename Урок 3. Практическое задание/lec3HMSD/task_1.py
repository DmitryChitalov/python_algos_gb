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

lista = []
dicta = {}


def timer_decor(func_name):
    def wrapper(arg):
        print("Функция ", func_name, ". Затраченное время = ", end='')
        start_time = time.time()
        func_name(arg)
        end_time = time.time()
        timer = end_time - start_time
        print(timer)

    return wrapper


@timer_decor
def list_add_element(n):
    for i in range(n):
        lista.append(i)


@timer_decor
def dict_add_elements(n):
    for i in range(n):
        dicta[i] = i


@timer_decor
def list_watch(n):
    lendata = len(lista)
    for i in range(n):
        # k = lista.index(i)*lista.index(lendata-i-1)
        k = lista[i] * lista[lendata - i - 1]


@timer_decor
def dict_watch(n):
    lendata = len(dicta)
    for i in range(n):
        # k = dicta.get(i)*dicta.get(lendata-i-1)
        k = dicta[i] * dicta[lendata - i - 1]


time_long = 1000000

list_add_element(time_long)
dict_add_elements(time_long)
list_watch(int(time_long))
dict_watch(int(time_long))

# Функция  <function list_add_element at 0x01B67190> . Затраченное время = 0.22687029838562012
# Функция  <function dict_add_elements at 0x01B67100> . Затраченное время = 0.20997118949890137
# Функция  <function list_watch at 0x01B67070> . Затраченное время = 27.307092428207397
# Функция  <function dict_watch at 0x01B67220> . Затраченное время = 0.0009999275207519531

# Выводы
# Заполнение словаря происходит быстрее чем заполнение словаря
# Извлечение данных из списка происходит быстрее
# p.s. А если использовать index и get, то index списка работае в 10000 раз медленнее чем get словаря.
