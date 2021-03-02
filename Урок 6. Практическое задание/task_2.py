"""
Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность

Например, один из вариантов, использование генераторов
"""

Задание 2.
Предложите фундаментальные варианты оптимизации памяти
 и доказать (наглядно, кодом, если получится) их эффективность
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика)

import collections
from pympler import asizeof

array = [1, 3, 1, 3, 4, 5, 1]


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

for i in range(1, 1000): # увеличим размер массива
    array.append(7)

###########################################################################################3
def max_coll():
    counter = collections.Counter(array)
    key_max = counter.most_common()
    return key_max[0][0], key_max[0][1]

print("func_1:", asizeof.asizeof((func_1())))
print("func_2:", asizeof.asizeof((func_2())))
print("max_coll", asizeof.asizeof((max_coll())))
"""
Например, один из вариантов, использование генераторов

использование Collections не только быстрее - что было выяснено в Lesson 4 / task_4: 
    func_1 14.0197108
    func_2 17.010997
    max_coll 0.5865653000000002
но еще и занимает меньше памяти
func_1: 208
func_2: 208
max_coll 120
""" 

"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from random import randint
from memory_profiler import profile


@profile
def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

num_1000 = randint(10000000, 100000000)

recursive_reverse(num_1000)

"""
декоратор профилировщика вызывается каждый раз при новой итерации рекурсии
в результате, непонятно - скоолько на самом деле будет затрачено памяти на работу скрипта.
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     25.5 MiB     25.5 MiB           1   @profile
    13                                         def recursive_reverse(number):
    14     25.5 MiB      0.0 MiB           1       if number == 0:
    15     25.5 MiB      0.0 MiB           1           return str(number % 10)
    16                                             return f'{str(number % 10)}{recursive_reverse(number // 10)}'
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     25.5 MiB     25.5 MiB           2   @profile
    13                                         def recursive_reverse(number):
    14     25.5 MiB      0.0 MiB           2       if number == 0:
    15     25.5 MiB      0.0 MiB           1           return str(number % 10)
    16     25.5 MiB      0.0 MiB           1       return f'{str(number % 10)}{recursive_reverse(number // 10)}'
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     25.5 MiB     25.5 MiB           3   @profile
    13                                         def recursive_reverse(number):
    14     25.5 MiB      0.0 MiB           3       if number == 0:
    15     25.5 MiB      0.0 MiB           1           return str(number % 10)
    16     25.5 MiB      0.0 MiB           2       return f'{str(number % 10)}{recursive_reverse(number // 10)}'
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     25.5 MiB     25.5 MiB           4   @profile
    13                                         def recursive_reverse(number):
    14     25.5 MiB      0.0 MiB           4       if number == 0:
    15     25.5 MiB      0.0 MiB           1           return str(number % 10)
    16     25.5 MiB      0.0 MiB           3       return f'{str(number % 10)}{recursive_reverse(number // 10)}'
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     25.5 MiB     25.5 MiB           5   @profile
    13                                         def recursive_reverse(number):
    14     25.5 MiB      0.0 MiB           5       if number == 0:
    15     25.5 MiB      0.0 MiB           1           return str(number % 10)
    16     25.5 MiB      0.0 MiB           4       return f'{str(number % 10)}{recursive_reverse(number // 10)}'
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     25.5 MiB     25.5 MiB           6   @profile
    13                                         def recursive_reverse(number):
    14     25.5 MiB      0.0 MiB           6       if number == 0:
    15     25.5 MiB      0.0 MiB           1           return str(number % 10)
    16     25.5 MiB      0.0 MiB           5       return f'{str(number % 10)}{recursive_reverse(number // 10)}'
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     25.5 MiB     25.5 MiB           7   @profile
    13                                         def recursive_reverse(number):
    14     25.5 MiB      0.0 MiB           7       if number == 0:
    15     25.5 MiB      0.0 MiB           1           return str(number % 10)
    16     25.5 MiB      0.0 MiB           6       return f'{str(number % 10)}{recursive_reverse(number // 10)}'
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     25.5 MiB     25.5 MiB           8   @profile
    13                                         def recursive_reverse(number):
    14     25.5 MiB      0.0 MiB           8       if number == 0:
    15     25.5 MiB      0.0 MiB           1           return str(number % 10)
    16     25.5 MiB      0.0 MiB           7       return f'{str(number % 10)}{recursive_reverse(number // 10)}'
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    12     25.5 MiB     25.5 MiB           9   @profile
    13                                         def recursive_reverse(number):
    14     25.5 MiB      0.0 MiB           9       if number == 0:
    15     25.5 MiB      0.0 MiB           1           return str(number % 10)
    16     25.5 MiB      0.0 MiB           8       return f'{str(number % 10)}{recursive_reverse(number // 10)}'
""" 