"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""
from random import randint
import time

# Простое добавление в список и словарь
rand = randint(10000000, 500000000)


def auto_lst(int):
    start_time = time.time()
    lst = [i for i in range(int)]
    end_time = time.time()
    return end_time - start_time


def auto_dict(int):
    start_time = time.time()
    dct = {i: i for i in range(int)}
    end_time = time.time()
    return end_time - start_time


print(auto_lst(rand))
print(auto_dict(rand))

"""
test 1: randint(10000000, 500000000)
lst: 11.27658748626709
dct: 20.7668514251709

test 2: randint(1000000, 50000000)
lst: 1.2711563110351562
dct: 2.798200845718384

test 3: randint(100000, 5000000)
lst: 0.11510443687438965
dct: 0.2252047061920166

test 4: randint(10000, 500000)
lst: 0.004003763198852539
dct: 0.009008407592773438

test 5: randint(1000, 50000)
lst: 0.0010008811950683594
dct: 0.0030028820037841797

Вывод: Простое добавление в словарь длится в 2 раза дольше, чем в список.
Почему? Скорей всего потому что в словаре надо вычислять хэш-функцию для каждого ключа + добавлять 2 элемента
ключ-значение,  в то время как в списке добавляется всего 1 элемент.
"""

rnd = 9999999


# Удаляем [х] элемент
def pop_lst(int):
    lst = [i for i in range(int)]
    start_time = time.time()
    lst.pop(9000)
    end_time = time.time()
    return end_time - start_time


def pop_dict(int):
    dct = {i: i for i in range(int)}
    start_time = time.time()
    dct.pop(9000)
    end_time = time.time()

    return end_time - start_time


print(pop_lst(rnd))
print(pop_dict(rnd))

"""
test 1: 9999999
pop(1)
lst: 0.004004001617431641
dct: 0.0

test 2: 9999999
pop(77)
lst: 0.0030028820037841797
dct: 0.0

test 3: 9999999
pop(9000)
lst: 0.004003763198852539
dct: 0.0
Вывод: в словаре ключ берется из хэш-таблицы, поэтому мгновенно.
Возможно другое объяснение: при удалении элемента из списка - формируется новый список, уменьшаясь на 1 индекс 
(т.к все элементы списка должны хранится в соседних ячейках памяти)
"""

# Copy lst,dct
rnd1 = 99999


def copy_lst(int):
    lst = [i for i in range(int)]
    start_time = time.time()
    lst.copy()
    end_time = time.time()
    return end_time - start_time


def copy_dict(int):
    dct = {i: i for i in range(int)}
    start_time = time.time()
    dct.copy()
    end_time = time.time()

    return end_time - start_time


print(copy_lst(rnd1))
print(copy_dict(rnd1))

"""
test 1: 9999999
lst: 0.06605958938598633
dct: 0.12211108207702637

test 2: 99999999
lst: 0.5955417156219482
dct: 1.7415757179260254

test 3: 999999999  - тестить не стал, тк заняло больше 25гб оперативы

test 3: 99999
lst: 0.0
dct: 0.001001119613647461

Вывод: копирование словаря занимает в 2-3 раза больше времени, чем списка.
Почему? Незнаю. Возможно потому что у него элементов в 2 раза больше, чем в списке + хэш таблица память занимает.
"""
