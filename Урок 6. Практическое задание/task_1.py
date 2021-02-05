"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО
"""
from memory_profiler import profile
import random

list_nums = [i for i in range(100000)]
array = [random.randint(1, 9) for i in range(100000)]
list_number = [random.randint(256, 10000) for i in range(1000)]


@profile
def func_1(nums):
    # создание списка четных чисел
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@profile
def func_2(nums):
    # создание списка четных чисел
    return [i for i in nums if i % 2 == 0]


func_1(list_nums)
func_2(list_nums)

"""

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    19     19.1 MiB     19.1 MiB           1   @profile
    20                                         def func_1(nums):
    21     19.1 MiB      0.0 MiB           1       new_arr = []
    22     21.2 MiB      1.3 MiB      100001       for i in range(len(nums)):
    23     21.2 MiB      0.0 MiB      100000           if nums[i] % 2 == 0:
    24     21.2 MiB      0.7 MiB       50000               new_arr.append(i)
    25     21.2 MiB      0.0 MiB           1       return new_arr

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    27     21.2 MiB     21.2 MiB           1   @profile
    28                                         def func_2(nums):
    29     21.6 MiB      0.4 MiB      100003       return [i for i in nums if i % 2 == 0]
    
Второй вариант решения занимает меньше памяти, за счет того что не сохраняется каждый обьект из списка
при проходе циклом в функции func_1 
"""


@profile
def func_3():
    # определяется число, которое встречается в массиве чаще всего.
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


@profile
def func_4():
    # определяется число, которое встречается в массиве чаще всего.
    return f'Чаще всего встречается число {max(array, key=array.count)}, ' \
           f'оно  появилось в массиве {array.count(max(array))} раз(а)'


func_3()
func_4()
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    61     22.4 MiB     22.4 MiB           1   @profile
    62                                         def func_3():
    63                                             # определяется число, которое встречается в массиве чаще всего.
    64     22.4 MiB      0.0 MiB           1       new_array = []
    65     24.9 MiB      0.0 MiB      100001       for el in array:
    66     24.9 MiB      0.0 MiB      100000           count2 = array.count(el)
    67     24.9 MiB      2.5 MiB      100000           new_array.append(count2)
    68                                         
    69     24.9 MiB      0.0 MiB           1       max_2 = max(new_array)
    70     24.9 MiB      0.0 MiB           1       elem = array[new_array.index(max_2)]
    71     24.9 MiB      0.0 MiB           2       return f'Чаще всего встречается число {elem}, '
    72     24.9 MiB      0.0 MiB           1              f'оно появилось в массиве {max_2} раз(а)'


Filename: /Users/Home/PyProject/Algorithms/python_algos_gb/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    74     24.4 MiB     24.4 MiB           1   @profile
    75                                         def func_4():
    76                                             # определяется число, которое встречается в массиве чаще всего.
    77     18.6 MiB     -5.9 MiB           2       return f'Чаще всего встречается число {max(array, key=array.count)},
    78     18.6 MiB      0.0 MiB           1              f'оно  появилось в массиве {array.count(max(array))} раз(а)'

Функция func_4 является более приемлемой, так идет освобождение памяти 
"""


@profile
def search_min_number(list_search):
    """
    Поиск минимального значения в списке при помощи сравнения
    каждого числа списка со всеми другими.

    :param list_search:
    :return:
    """

    set_search = set(list_search)
    min_number = list_search[0]
    for i in set_search:
        for j in set_search:
            if i <= min_number and i <= j:
                min_number = i
    return min_number


@profile
def search_min_number2(list_search):
    """
    Поиск минимального значения для списка
    :param list_search:
    :return:
    """
    return min(list_search)


search_min_number(list_number)
search_min_number2(list_number)

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
     8     13.8 MiB     13.8 MiB           1   @profile
     9                                         def search_min_number(list_search):
    10                                             
    11                                             Поиск минимального значения в списке при помощи сравнения
    12                                             каждого числа списка со всеми другими.
    13                                         
    14                                             :param list_search:
    15                                             :return:
    16                                             
    17                                             
    18     13.8 MiB      0.0 MiB           1       set_search = set(list_search)
    19     13.8 MiB      0.0 MiB           1       min_number = list_search[0]
    20     13.8 MiB  -1122.4 MiB         956       for i in set_search:
    21     13.8 MiB -1072093.8 MiB      912980           for j in set_search:
    22     13.8 MiB -1070972.3 MiB      912025               if i <= min_number and i <= j:
    23     13.8 MiB      0.0 MiB        1733                   min_number = i
    24     11.7 MiB     -2.1 MiB           1       return min_number


Filename: /Users/Home/PyProject/Algorithms/python_algos_gb/Урок 6. Практическое задание/1111.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    27     11.8 MiB     11.8 MiB           1   @profile
    28                                         def search_min_number2(list_search):
    29                                             
    30                                             Поиск минимального значения для списка
    31                                             :param list_search:
    32                                             :return:
    33                                             
    34     11.8 MiB      0.0 MiB           1       return min(list_search)
    
В данном случае получил очень странные результаты, даже боюсь это комментировать 
"""

"""
Python 3.9
macOS Big Sur x64
"""