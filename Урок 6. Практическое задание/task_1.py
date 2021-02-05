
"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

import memory_profiler
from timeit import default_timer
from memory_profiler import profile
from random import randint
from math import factorial


def decor(func):
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        m1 = memory_profiler.memory_usage()
        my_generator = func(args[0])
        res_time = default_timer() - start_time
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return my_generator, mem_diff, res_time

    return wrapper

# 3 Заполнение списка

@decor
def get_list(numbers):
    new_lst = []
    for i in numbers:
        if i % 2 == 0:
            new_lst.append(i)
    return new_lst


@decor
def get_list_2(numbers):
    new_lst_2 = [i for i in numbers if i % 2 == 0]
    return new_lst_2


@decor
def get_list_3(numbers):
    for i in numbers:
        if i % 2 == 0:
            yield i



if __name__ == '__main__':

    print('###### Тест с append ######')
    my_generator, mem_diff, res_time = get_list(list(range(300000)))
    print(f"Выполнение заняло {mem_diff} Mib")
    print(f"Выполнение заняло {res_time} sec")
    print('###### Тест со списковым включением ######')
    my_generator, mem_diff1, res_time1 = get_list_2(list(range(300000)))
    print(f"Выполнение заняло {mem_diff1} Mib")
    print(f"Выполнение заняло {res_time1} sec")
    print('###### Тест c yield ######')
    my_generator, mem_diff2, res_time2 = get_list_3(list(range(300000)))
    print(f"Выполнение заняло {mem_diff2} Mib")
    print(f"Выполнение заняло {res_time2} sec")

"""
###### Test 1 ######
Выполнение заняло 2.06640625 Mib
Выполнение заняло 0.12603599999999998 sec
###### Test 2 ######
Выполнение заняло 1.14453125 Mib
Выполнение заняло 0.11773270000000002 sec
###### Test 3 ######
Выполнение заняло 0.0 Mib
Выполнение заняло 0.10011389999999998 sec

Скрипты взял из ДЗ 4 урока.
В декоратор добавил res_time для подсчета времени выполнения.
Оптимизация кода за счет использование генератора позволяет значительно сократить использоваине памяти.
Использование спискового включения  занимает больше памяти, но в два раза меньше чем стандартный способ
с использованием append. 
"""

# 2 Поиск n-го по счету натурально числа

@profile
def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


@profile
def sieve(n):
    i = 2
    last_elem = n * 10
    all_num = [z for z in range(last_elem)]
    all_num[1] = 0
    while i < last_elem:
        if all_num[i] != 0:
            check = i * 2
            while check < last_elem:
                all_num[check] = 0
                check = check + i
        i = i + 1
    return [x for x in all_num if x != 0][n - 1]

simple(100)
sieve(100)


"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   106     35.1 MiB     35.1 MiB           1   @profile
   107                                         def simple(i):
   108                                             """Без использования Решета Эратосфена"""
   109     35.1 MiB      0.0 MiB           1       count = 1
   110     35.1 MiB      0.0 MiB           1       n = 2
   111     35.1 MiB      0.0 MiB         540       while count <= i:
   112     35.1 MiB      0.0 MiB         540           t = 1
   113     35.1 MiB      0.0 MiB         540           is_simple = True
   114     35.1 MiB      0.0 MiB       25724           while t <= n:
   115     35.1 MiB      0.0 MiB       25624               if n % t == 0 and t != 1 and t != n:
   116     35.1 MiB      0.0 MiB         440                   is_simple = False
   117     35.1 MiB      0.0 MiB         440                   break
   118     35.1 MiB      0.0 MiB       25184               t += 1
   119     35.1 MiB      0.0 MiB         540           if is_simple:
   120     35.1 MiB      0.0 MiB         100               if count == i:
   121     35.1 MiB      0.0 MiB           1                   break
   122     35.1 MiB      0.0 MiB          99               count += 1
   123     35.1 MiB      0.0 MiB         539           n += 1
   124     35.1 MiB      0.0 MiB           1       return n


Filename: C:/Users/Shevt/YandexDisk/Python курс GB/Основной курс/Алгоритмы и стуктуры данных на Python/Урок 6/Урок 6. Практическое задание/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   128     35.1 MiB     35.1 MiB           1   @profile
   129                                         def sieve(n):
   130     35.1 MiB      0.0 MiB           1       i = 2
   131     35.1 MiB      0.0 MiB           1       last_elem = n * 10
   132     35.1 MiB      0.0 MiB        1003       all_num = [z for z in range(last_elem)]
   133     35.1 MiB      0.0 MiB           1       all_num[1] = 0
   134     35.1 MiB      0.0 MiB         999       while i < last_elem:
   135     35.1 MiB      0.0 MiB         998           if all_num[i] != 0:
   136     35.1 MiB      0.0 MiB         168               check = i * 2
   137     35.1 MiB      0.0 MiB        2124               while check < last_elem:
   138     35.1 MiB      0.0 MiB        1956                   all_num[check] = 0
   139     35.1 MiB      0.0 MiB        1956                   check = check + i
   140     35.1 MiB      0.0 MiB         998           i = i + 1
   141     35.1 MiB      0.0 MiB        1003       return [x for x in all_num if x != 0][n - 1]


Использование Решета Эратосфена сокращает количество операций и ускоряет код.

"""

# 3. Удаление из первого списка все вхождений во втором списке

my_list_1 = list(range(1000))
my_list_2 = [23, 74, 102, 300, 45, 456]


@profile
def func_1(lst1, lst2):
    j = len(lst1)
    i = 0

    for el1 in lst1:
        i = 0
        if el1 in lst2:
            while i < j:
                if lst1[i] == el1:
                    del lst1[i]
                    j -= 1
                    i -= 1
                i += 1
    return lst1


@profile
def func_2(lst1, lst2):
    return [el for el in lst1 if el not in lst2]


@profile
def func_3(lst1, lst2):
    for el_1 in lst1.copy():
        if el_1 in lst2:
            lst1.remove(elem1)
    return lst1


func_1(my_list_1, my_list_2)
func_2(my_list_1, my_list_2)
func_3(my_list_1, my_list_2)


"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   200     35.0 MiB     35.0 MiB           1   @profile
   201                                         def func_1(lst1, lst2):
   202     35.0 MiB      0.0 MiB           1       j = len(lst1)
   203     35.0 MiB      0.0 MiB           1       i = 0
   204                                         
   205     35.0 MiB      0.0 MiB         995       for elem1 in lst1:
   206     35.0 MiB      0.0 MiB         994           i = 0
   207     35.0 MiB      0.0 MiB         994           if elem1 in lst2:
   208     35.0 MiB      0.0 MiB        5991               while i < j:
   209     35.0 MiB      0.0 MiB        5985                   if lst1[i] == elem1:
   210     35.0 MiB      0.0 MiB           6                       del lst1[i]
   211     35.0 MiB      0.0 MiB           6                       j -= 1
   212     35.0 MiB      0.0 MiB           6                       i -= 1
   213     35.0 MiB      0.0 MiB        5985                   i += 1
   214     35.0 MiB      0.0 MiB           1       return lst1



Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   217     35.0 MiB     35.0 MiB           1   @profile
   218                                         def func_2(lst1, lst2):
   219     35.0 MiB      0.0 MiB         997       return [elem for elem in lst1 if elem not in lst2]



Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   222     35.0 MiB     35.0 MiB           1   @profile
   223                                         def func_3(lst1, lst2):
   224     35.0 MiB      0.0 MiB         995       for elem1 in lst1.copy():
   225     35.0 MiB      0.0 MiB         994           if elem1 in lst2:
   226                                                     lst1.remove(elem1)
   227     35.0 MiB      0.0 MiB           1       return lst1

  
Из статистики видно, что удаление из первого списка все вхождений во втором списке  лучше использовать 
списковые включения func_2 - значительно снижает количество операций


"""
