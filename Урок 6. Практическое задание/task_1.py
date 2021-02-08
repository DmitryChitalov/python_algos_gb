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
from statistics import mean
from cProfile import run
from numpy import array
from pympler import asizeof
import memory_profiler


@profile
def task_1_1():
    my_list = list(range(10, 100000))
    my_list_even = []
    for el in my_list:
        if el % 2 == 0:
            my_list_even.append(el)
    max_el = max(my_list_even)
    min_el = min(my_list_even)
    avr_el = (max_el + min_el) / 2
    del my_list, my_list_even, max_el, min_el
    return avr_el


task_1_1()
run('task_1_1()')


@profile
def task_1_2():
    my_list = [el for el in range(10, 100000) if el % 2 == 0]
    avr_el = sum(my_list) / len(my_list)
    del my_list
    return avr_el


task_1_2()
run('task_1_2()')


@profile
def task_1_3():
    return mean([el for el in range(10, 100000) if el % 2 == 0])


task_1_3()
run('task_1_3()')

""" task_1_1():
Результат работы @profile:
============================================================
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    18     19.5 MiB     19.5 MiB           1   @profile
    19                                         def task_1_1():
    20     23.3 MiB      3.8 MiB           1       my_list = list(range(10, 100000))
    21     23.3 MiB      0.0 MiB           1       my_list_even = []
    22     24.5 MiB      0.0 MiB       99991       for el in my_list:
    23     24.5 MiB      0.0 MiB       99990           if el % 2 == 0:
    24     24.5 MiB      1.1 MiB       49995               my_list_even.append(el)
    25     24.5 MiB      0.0 MiB           1       max_el = max(my_list_even)
    26     24.5 MiB      0.0 MiB           1       min_el = min(my_list_even)
    27     24.5 MiB      0.0 MiB           1       avr_el = (max_el + min_el) / 2
    28     19.8 MiB     -4.6 MiB           1       del my_list, my_list_even, max_el, min_el
    29     19.8 MiB      0.0 MiB           1       return avr_el
============================================================

Результат работы cProfile:
    51362 function calls in 4.441 seconds
"""

""" task_1_2():
Результат работы @profile:
============================================================
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    24     19.7 MiB     19.7 MiB           1   @profile
    25                                         def task_1_2():
    26     21.4 MiB      1.7 MiB       99993       my_list = [el for el in range(10, 100000) if el % 2 == 0]
    27     21.4 MiB      0.0 MiB           1       avr_el = sum(my_list) / len(my_list)
    28     20.2 MiB     -1.2 MiB           1       del my_list
    29     20.2 MiB      0.0 MiB           1       return avr_el
============================================================
    
Результат работы cProfile:
    865 function calls (864 primitive calls) in 1.641 seconds
"""

""" task_1_3():
Результат работы @profile:
============================================================
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    36     19.7 MiB     19.7 MiB           1   @profile
    37                                         def task_1_3():
    38     21.4 MiB      0.7 MiB       99993       return mean([el for el in range(10, 100000) if el % 2 == 0])
============================================================
    
Результат работы cProfile:
    100664 function calls (100663 primitive calls) in 1.964 seconds
"""

# # # # # # # # # # # # # # # Аналитика # # # # # # # # # # # # # # #
# В приведенных примерах анализировались 3 параметра: объем памяти, #
# необходимый для выполнения функций, время, затраченное на их      #
# выполнение и лаконичность кода. Очевидно, первый пример task_1_1  #
# проигрывает по всем параметрам, особенно, если проигнорировать    #
# инструкцию del. Второй и третий метод task_1_2 и task_1_3 приб-   #
# лизительно эквивалентны по объему использованой памяти, но раз-   #
# личаются по времени исполнения, особенно если генерацию списка    #
# my_list вынести за пределы функции и передавать его в качестве    #
# параметра. Так же, следует отметить, что применение метода del    #
# позволяет оптимизировать память, но увеличивает время выполнения. #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


"""
    Затем я перезагрузил комп, который, кстати Win10 x64 Intel i-5 16Gb
    по мотивам лекции написал собственный измеритель памяти, и исследовал
    аналогичную задачу используя numpy и list comprehensions.  
"""


def decor(func):
    def wrapper(*args):
        m1 = memory_profiler.memory_usage()
        res = func(args[0])
        m2 = memory_profiler.memory_usage()
        memory_diff = m2[0] - m1[0]
        return res, memory_diff

    return wrapper


@decor
def task_1_4(lst):
    my_list = array([el for el in lst if el % 2 == 0])
    return mean(my_list)


res, memory_diff = task_1_4(list(range(10, 100000)))
print(f'Результат работы - {memory_diff} Mib')
run('task_1_4(list(range(10, 100000)))')
print(f'Результат работы - {asizeof.asizeof(task_1_4)}')


@decor
def task_1_5(lst):
    for el in lst:
        if el % 2 == 0:
            yield el


res, memory_diff = task_1_5(list(range(10, 100000)))
print(f'Результат работы - {memory_diff} Mib')
run('task_1_4(list(range(10, 100000)))')
print(f'Результат работы - {asizeof.asizeof(task_1_5)}')


""" task_1_4():
    Результат работы - 0.08984375 Mib
    100119 function calls in 0.262 seconds
"""
""" task_1_5():
    Результат работы - 0.00390625 Mib
    100119 function calls in 0.252 seconds
"""

# # # # # # # # # # # # # # # Аналитика # # # # # # # # # # # # # # #
# Выполнение задачи с помощью модуля numpy и генератора в плане     #
# времени выполнения дало сопоставимый результат, но в плане исполь-#
# зования ресурсов памяти, генератор оказался заметно менее прожор- #
# лив. Значения asizeof на всех примерах выдавало значение 0. Я     #
# сделал предположение, что поскольку я скармливал ему функцию, то, #
# после её завершения, возвращалась вся память. ¯\_(ツ)_/¯          #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
