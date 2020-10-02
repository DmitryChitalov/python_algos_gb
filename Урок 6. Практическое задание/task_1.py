"""
Задание 1 и 3.
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
"""
Python 3.8 Windows 10(X64)
############################################################################
первый вариант с генератором 
my_list_in = (el for el in range(100, 100001) if el % 2 == 0)
и кортежем


Line #    Mem usage    Increment   Line Contents
================================================
    25     13.6 MiB     13.6 MiB   @profile
    26                             def general_list():
    27     13.6 MiB      0.0 MiB       my_list_in = (el for el in range(100, 10000001) if el % 2 == 0)
    28     13.6 MiB      0.0 MiB       return my_list_in

Line #    Mem usage    Increment   Line Contents
================================================
    50     13.7 MiB     13.7 MiB   @profile
    51                             def main():
    52     13.7 MiB      0.0 MiB       my_list = general_list()
    53     13.8 MiB      0.1 MiB       print(functools.reduce(my_func, my_list))
__________________________________________
второй вариант с генераторным выражение
my_list_in = [el for el in range(100, 100001) if el % 2 == 0]
и списком

Line #    Mem usage    Increment   Line Contents
================================================
    42     13.7 MiB     13.7 MiB   @profile
    43                             def general_list():
    44     14.7 MiB      0.1 MiB       my_list_in = [el for el in range(100, 100001) if el % 2 == 0]
    45     14.7 MiB      0.0 MiB       return my_list_in

Line #    Mem usage    Increment   Line Contents
================================================
    58     13.7 MiB     13.7 MiB   @profile
    59                             def main():
    60     14.8 MiB      1.1 MiB       my_list = general_list()
    61     15.0 MiB      0.2 MiB       print(functools.reduce(my_func, my_list))
    
Вывод: в первом случае большая экономия памяти

"""

import functools
from memory_profiler import profile

#######################################################################################


@profile
def general_list():
    my_list_in = (el for el in range(100, 100001) if el % 2 == 0)
    return my_list_in


def my_func(num_1, num_2):
    """
    функция принемает 2 числа и возращяет их произведение
    :param num_1: number
    :param num_2: number
    :return: number
    """
    return num_1 * num_2


@profile
def main():
    my_list = general_list()
    print(functools.reduce(my_func, my_list))


# main()

#############################################################################################
"""
При замере рекурсии замеряеться каждый вызов функции отдельно,
и так как при отдельном вызове памяти требуеться мало то мы не можем помереть общие затраты.
Line #    Mem usage    Increment   Line Contents
================================================
    97     14.7 MiB     13.8 MiB   @profile
    98                             def fact_num(num):
    99     14.7 MiB      0.0 MiB       if num == 0:
   100     14.7 MiB      0.0 MiB           return 1
   101     14.7 MiB      0.0 MiB       return num * fact_num(num - 1)
Попробывал сделать вызов рекурсивной функции не на прямую ,а из функции - увидел расход памяти.
Line #    Mem usage    Increment   Line Contents
================================================
   104     13.8 MiB     13.8 MiB   @profile
   105                             def get_num():
   106     14.7 MiB      0.9 MiB       return fact_num(200)
"""


@profile
def fact_num(num):
    if num == 0:
        return 1
    return num * fact_num(num - 1)


@profile
def get_num():
    return fact_num(200)


get_num()
