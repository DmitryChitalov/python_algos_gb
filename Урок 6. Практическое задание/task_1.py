"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-5 ваших разных скриптов!.
Сделать их разные реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from memory_profiler import profile, memory_usage
import time
import random

def my_decorator(function):
    def wrapper(*args, **kwargs):
        t_1 = time.process_time()
        m_1 = memory_usage()
        function(*args, **kwargs)
        t_2 = time.process_time()
        m_2 = memory_usage()
        process_time = t_2 - t_1
        process_memory = m_2[0] - m_1[0]
        return f'Время выполнения: {process_time}, память: {process_memory}'

    return wrapper


my_num = 10**5


# @profile
@my_decorator
def my_list():
    '''
    Реализуйте заполнение списка.
    '''

    foo = [element *2 for element in list(range(my_num))]
    return foo


# @profile
@my_decorator
def my_dist():
    '''
    Реализуйте заполнение словаря.
    '''
    foo = {k: k*2 for k in list(range(my_num))}
    return foo


# @profile
@my_decorator
def func_1():
    foo = list(range(my_num))
    new_arr = []
    for i in range(len(foo)):
        if foo[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# @profile
@my_decorator
def func_2():
    foo = [i for i in list(range(my_num)) if i % 2 == 0]
    return foo

print(my_list())
print(my_dist())
print(func_1())
print(func_2())
# print(my_num)
# my_list()
# my_dist()
# func_1()
# func_2()
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    44     23.7 MiB     23.7 MiB           1   @profile
    45                                         # @my_decorator
    46                                         def my_list():
    47                                             '''
    48                                             Реализуйте заполнение списка.
    49                                             '''
    50                                         
    51     28.4 MiB      0.7 MiB      100003       foo = [element *2 for element in list(range(my_num))]
    52     26.4 MiB     -2.0 MiB           1       return foo
@my_decorator -  Время выполнения: 0.03125, память: 0.1328125 

Как мы видим из результатов работы @profile использование памяти - 28.4 MiB MiB-23.7 MiB = 4,7 MiB(Хотя Increment пишет 
0.7 MiB ) в конце было высвобождено 2 MiB памяти 


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    55     24.1 MiB     24.1 MiB           1   @profile
    56                                         # @my_decorator
    57                                         def my_dist():
    58                                             '''
    59                                             Реализуйте заполнение словаря.
    60                                             '''
    61     30.7 MiB      5.7 MiB      100003       foo = {k: k*2 for k in list(range(my_num))}
    62     30.3 MiB     -0.4 MiB           1       return foo
@my_decorator -  Время выполнения: 0.0625, память: 0.03515625
    
Как мы видим из результатов работы @profile использование памяти - 30.7 MiB MiB-24.1 MiB MiB = 6,6 MiB(Хотя Increment 
пишет 5.7 MiB ) в конце было высвобождено 0,4 MiB памяти 

Из полученных данных можно сделать вывод что заполнения списка требует меньшего времени на выполнения и количества памяти

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================    
    65     24.4 MiB     24.4 MiB           1   @profile
    66                                         # @my_decorator
    67                                         def func_1():
    68     25.8 MiB      1.4 MiB           1       foo = list(range(my_num))
    69     25.8 MiB      0.0 MiB           1       new_arr = []
    70     26.8 MiB      0.0 MiB      100001       for i in range(len(foo)):
    71     26.8 MiB      0.8 MiB      100000           if foo[i] % 2 == 0:
    72     26.8 MiB      0.2 MiB       50000               new_arr.append(i)
    73     26.8 MiB      0.0 MiB           1       return new_arr
@my_decorator -  Время выполнения: 0.0625, память: 0.0

Как мы видим из результатов работы @profile использование памяти - 26.8 MiB MiB-24.4 MiB = 2,4 MiB(Increment 
в данном случае это подтверждает)
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    76     24.8 MiB     24.8 MiB           1   @profile
    77                                         # @my_decorator
    78                                         def func_2():
    79     26.0 MiB      0.4 MiB      100003       foo = [i for i in list(range(my_num)) if i % 2 == 0]
    80     25.6 MiB     -0.4 MiB           1       return foo
@my_decorator -  Время выполнения: 0.03125, память: 0.0625

Как мы видим из результатов работы @profile использование памяти - 26.0 MiB MiB-24.8 MiB = 1,8 MiB(Хотя Increment 
пишет 0.4 MiB ) в конце было высвобождено 0,4 MiB памяти 

в итоге мы получили противоречивые результаты  @my_decorator говорит нам что для выполнение второго скрипта памяти 
понадобилось больше чем на первый. @profile наоборот. Так как данные малы ими можно принебречь
Из полученных данных можно сделать вывод что использование генераторных выражений более выгодно ведь скорость выполнения
их в данном случае больше в 2 раза 
"""