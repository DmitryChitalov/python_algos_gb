"""
Задание 1.

Выполните профилирование памяти в скриптах  --- 1
Проанализировать результат --- 2 и определить программы с
наиболее эффективным использованием памяти.  ---- 3

Примечание: Для анализа возьмите любые 1-5 ваших разных скриптов!. (2 обязательно)
Сделать их разные реализации.  ---- 4

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду. !!
Также укажите в комментариях версию Python и разрядность вашей ОС. !!

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!  ---- 5
"""

from memory_profiler import profile, memory_usage
from time import perf_counter

"""
Версия Python:
C:\Windows\system32>python --version
Python 3.9.0
ОС:
Процессор	AMD Ryzen 7 2700 Eight-Core Processor             3.20 GHz
Тип системы	64-разрядная операционная система, процессор x64
"""

"""
======================================
=            Скрипт №1               =
======================================
"""


# профилируем через декоратор библиотеки memory_profiler --- 1
@profile()
def func_1():  # O(n)
    nums = list(range(500000))
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


func_1()


"""
Результат работы программы:

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    43     19.7 MiB     19.7 MiB           1   @profile()
    44                                         def func_1():  # O(n)
    45     38.9 MiB     19.3 MiB           1       nums = list(range(500000))
    46     38.9 MiB      0.0 MiB           1       new_arr = []
    47     49.5 MiB      0.0 MiB      500001       for i in range(len(nums)):
    48     49.5 MiB      7.8 MiB      500000           if nums[i] % 2 == 0:
    49     49.5 MiB      2.7 MiB      250000               new_arr.append(i)
    50     49.5 MiB      0.0 MiB           1       return new_arr
    
Делаем анализ. --- 2.
Для запуска программы выделено 19.7 MiB - строка 43
Для создания списка nums выделено еще 19.2 MiB - строка 45
(Increment показывает 19.3, однако в Mem usage результат 38.9,
ореинтируемся на Mem usage 38.9 - 19.7 = 19.2)
Для операций с элементами списка nums и создания нового списка new_arr выделено 10.6 MiB - строка 47
(аналогичная ситуация 49.5 - 38.9 = 10.6)
Всего задействован объем памти размером 49.5 MiB.
После создания списка четных чисел new.arr исходный список nums нам больше не нужен,
предлагаю его удалить.
"""

"""
======================================
=   Скрипт №1 - другая реализация    =  --- 4
======================================
"""


@profile()
def func_opt_1():  # O(n)
    nums = list(range(500000))
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    del nums
    return new_arr


func_opt_1()

"""
Результат:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    89     20.3 MiB     20.3 MiB           1   @profile()
    90                                         def func_opt_1():  # O(n)
    91     38.9 MiB     18.6 MiB           1       nums = list(range(500000))
    92     38.9 MiB      0.0 MiB           1       new_arr = []
    93     48.6 MiB -20267.6 MiB      500001       for i in range(len(nums)):
    94     48.6 MiB -20259.9 MiB      500000           if nums[i] % 2 == 0:
    95     48.6 MiB -10131.3 MiB      250000               new_arr.append(i)
    96     30.1 MiB    -18.6 MiB           1       del nums
    97     30.1 MiB      0.0 MiB           1       return new_arr
    
Как видим такой подход позволил освободить нам 18.5 MiB
"""


"""
======================================
=            Скрипт №2               =
======================================
"""


@profile()
def my_func_2():
    user_list = [el for el in range(500000)]
    index = 0
    for i in range(len(user_list) // 2):
        user_list[index], user_list[index+1] = user_list[index+1], user_list[index]
        index += 2
    return user_list


my_func_2()

"""
Результат:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   128     20.5 MiB     20.5 MiB           1   @profile()
   129                                         def my_func_2():
   130     39.2 MiB -26888.4 MiB      500003       user_list = [el for el in range(500000)]
   131     39.2 MiB      0.0 MiB           1       index = 0
   132     39.2 MiB      0.0 MiB      250001       for i in range(len(user_list) // 2):
   133     39.2 MiB      0.0 MiB      250000           user_list[index], user_list[index+1] = user_list[index+1], user_list[index]
   134     39.2 MiB      0.0 MiB      250000           index += 2
   135     39.2 MiB      0.0 MiB           1       return user_list
   
Анализируем:
Для запуска программы - 20.5 MiB
Для создания списка - 18.7 MiB
Предлагаю вместо ключевого слова return использовать yield
"""

"""
======================================
=  Скрипт №2 - вариант с yield       =
======================================
"""


def my_func_2_opt():
    user_list = [el for el in range(500000)]
    index = 0
    for i in range(len(user_list) // 2):
        user_list[index], user_list[index+1] = user_list[index+1], user_list[index]
        index += 2
    yield user_list

"""
Профилировать встроенным декоратором не получится. Сделаем свой. --- 5
"""


def mem_time_check(func):
    def wrapper():
        start = perf_counter()
        mem = memory_usage()
        func()
        print(f'Время выполнения функции заняло {perf_counter() - start} сек.')
        print(f'Для этого потребовалось {memory_usage()[0] - mem[0]} MiB')
    return wrapper()


# замеряем и сравниваем
print('Функция с return')


@mem_time_check
def my_func_2():
    user_list = [el for el in range(500000)]
    index = 0
    for i in range(len(user_list) // 2):
        user_list[index], user_list[index+1] = user_list[index+1], user_list[index]
        index += 2
    return user_list


print('Функция с yield')


@mem_time_check
def my_func_2_opt():
    user_list = [el for el in range(500000)]
    index = 0
    for i in range(len(user_list) // 2):
        user_list[index], user_list[index+1] = user_list[index+1], user_list[index]
        index += 2
    yield user_list


"""
Результат:
Функция с return
Время выполнения функции заняло 0.18207539999999997 сек.
Для этого потребовалось 1.69140625 MiB
Функция с yield
Время выполнения функции заняло 0.11417709999999998 сек.
Для этого потребовалось 0.015625 MiB

Вывод: использование генератора менее затратно по времени и объему занимаемой памяти
"""