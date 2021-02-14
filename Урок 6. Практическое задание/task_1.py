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

list = [element for element in range(1, 100000)]


@profile()
def invers_list(list):
    buff_list = []
    for element in range(len(list) - 1, -1, -1):
        buff_list.append(list[element])
    return buff_list


@profile()
def invers_list_include_revers(list):
    return list.reverse()


@profile()
def invers(list):
    return [list[element] for element in range(len(list) - 1, -1, -1)]




rez_list = invers_list(list)
rez = invers(list)
rez_list_1 = invers_list_include_revers(list)


"""
invers_list() 
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    21     23.5 MiB     23.5 MiB           1   @profile()
    22                                         def invers_list(list):
    23     23.5 MiB      0.0 MiB           1       buff_list = []
    24     24.5 MiB      0.0 MiB      100000       for element in range(len(list) - 1, -1, -1):
    25     24.5 MiB      1.0 MiB       99999           buff_list.append(list[element])
    26     24.5 MiB      0.0 MiB           1       return buff_list


Filename: /home/ping/GeekBrainsRepo/Repository/python_algos_gb/Урок 6. Практическое задание/task_1.py
invers(list)
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    34     24.5 MiB     24.5 MiB           1   @profile()
    35                                         def invers(list):
    36     25.3 MiB      0.8 MiB      100002       return [list[element] for element in range(len(list) - 1, -1, -1)]


Filename: /home/ping/GeekBrainsRepo/Repository/python_algos_gb/Урок 6. Практическое задание/task_1.py
invers_list_include_revers(list)
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    29     25.3 MiB     25.3 MiB           1   @profile()
    30                                         def invers_list_include_revers(list):
    31     25.3 MiB      0.0 MiB           1       return list.rever
    
    
При запуске invers_list() было выделено памяти   23.5 MiB  в ходе выполнения функция использовала еще 1.0 MiB и закончла выполнение 24.5 MiB (самая медленная версияя),
invers() при запуске было выделено 24.5 MiB памяти в ходе работы было использовано еще 0.8 MiB памяти за все время исполнения затрачено 25.3 MiB более быстрый вариант
и меньше использует дополнительно памяти но если сравнить с invers_list() затратил в итоге на 0.8 mib  больше.
invers_list_include_revers(list) при запуске использовала 25.3 MiB во время работы не использовала дополнительной памяти. 
по общему объему затраченой памяти сравнима с invers(). Думаю invers_list_include_revers(list) свмая быстрая из трех.

за скорость нужно платить памятью.
 """