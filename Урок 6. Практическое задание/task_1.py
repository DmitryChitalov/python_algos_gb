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

"""

# Python 3.8 // MacOS x86_64 разрядность
from memory_profiler import profile


@profile
def my_div():
    my_list = list(range(300001))
    maximum = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > maximum:
            maximum = my_list[i]
    print(maximum)


@profile
def my_div2():
    my_list = list(range(300000))
    print(max(my_list))


@profile
def eratosthenes(n):
    if n < 4:
        return

    a = [i for i in range(n + 1)]
    a[1] = 0
    b = []

    for i in range(2, n + 1):
        for j in range(i * 2, n + 1, i):
            if a[j] != 0:
                a[j] = 0
                b.append(j)

    print(" ".join(str(x) for x in b))


@profile
def eratosthenes2(n):
    a = [i for i in range(1, n + 1)]
    b = []
    num = 2
    i = 0
    a.remove(1)

    while num < a[-1]:
        while len(
                a) > i:
            if a[i] % num == 0 and a[i] != num:
                b.append(a[i])
                a.pop(i)
            i += 1
        i = 0

        for j in range(len(a)):
            if a[j] > num:
                num = a[j]
                break
    return b

# my_div2()
# my_div()
# my_div2()


eratosthenes(int(5000))
eratosthenes2(int(5000))

"""
### eratosthenes ###

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    45     13.4 MiB     13.4 MiB           1   @profile
    46                                         def eratosthenes(n):
    47     13.4 MiB      0.0 MiB           1       if n < 4:
    48                                                 return
    49                                         
    50     13.5 MiB      0.1 MiB        5004       a = [i for i in range(n + 1)]
    51     13.5 MiB      0.0 MiB           1       a[1] = 0
    52     13.5 MiB      0.0 MiB           1       b = []
    53                                         
    54     13.6 MiB      0.0 MiB        5000       for i in range(2, n + 1):
    55     13.6 MiB      0.0 MiB       38376           for j in range(i * 2, n + 1, i):
    56     13.6 MiB      0.0 MiB       33377               if a[j] != 0:
    57     13.6 MiB      0.0 MiB        4330                   a[j] = 0
    58     13.6 MiB      0.1 MiB        4330                   b.append(j)
    59                                         
    60     13.8 MiB      0.3 MiB        8663       print(" ".join(str(x) for x in b))


Filename: /Users/German/Documents/ПРОГРАММИРОВАНИЕ/07 Алгоритмы Python/python_algos_gb/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    63     13.9 MiB     13.9 MiB           1   @profile
    64                                         def eratosthenes2(n):
    65     13.9 MiB      0.0 MiB        5003       a = [i for i in range(1, n + 1)]
    66     13.9 MiB      0.0 MiB           1       b = []
    67     13.9 MiB      0.0 MiB           1       num = 2
    68     13.9 MiB      0.0 MiB           1       i = 0
    69     13.9 MiB      0.0 MiB           1       a.remove(1)
    70                                         
    71     13.9 MiB      0.0 MiB         669       while num < a[-1]:
    72     13.9 MiB      0.0 MiB     1359621           while len(
    73     13.9 MiB      0.0 MiB      906414                   a) > i:
    74     13.9 MiB      0.0 MiB      452539               if a[i] % num == 0 and a[i] != num:
    75     13.9 MiB      0.0 MiB        4330                   b.append(a[i])
    76     13.9 MiB      0.0 MiB        4330                   a.pop(i)
    77     13.9 MiB      0.0 MiB      452539               i += 1
    78     13.9 MiB      0.0 MiB         668           i = 0
    79                                         
    80     13.9 MiB      0.0 MiB      224114           for j in range(len(a)):
    81     13.9 MiB      0.0 MiB      224114               if a[j] > num:
    82     13.9 MiB      0.0 MiB         668                   num = a[j]
    83     13.9 MiB      0.0 MiB         668                   break
    84     13.9 MiB      0.0 MiB           1       return b
    
Сделан запуск функции Решето Эратосфена по двум вариантам решений
В первом варианте в процессе выделялась память под созадние списка, последующие присоединения 
и создание строки вывода результата
Во втором варианте выделения памяти под решение особо не произошло
Однако количество операций значительно выросло, как и время выполнения
Получается что второй вариант по памяти оптимальнее, а по времени - дольше


### maximum - не оч интересный пример и аналитика... ###

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    22     13.3 MiB     13.3 MiB           1   @profile
    23                                         def my_div():
    24     24.9 MiB     11.6 MiB           1       my_list = list(range(300001))
    25     24.9 MiB      0.0 MiB           1       maximum = my_list[0]
    26     24.9 MiB      0.0 MiB      300001       for i in range(1, len(my_list)):
    27     24.9 MiB      0.0 MiB      300000           if my_list[i] > maximum:
    28     24.9 MiB      0.0 MiB      300000               maximum = my_list[i]
    29     24.9 MiB      0.0 MiB           1       print(maximum)

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    32     19.5 MiB     19.5 MiB           1   @profile
    33                                         def my_div2():
    34     24.8 MiB      5.3 MiB           1       my_list = list(range(300000))
    35     24.8 MiB      0.0 MiB           1       print(max(my_list))

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    32     19.7 MiB     19.7 MiB           1   @profile
    33                                         def my_div2():
    34     24.8 MiB      5.1 MiB           1       my_list = list(range(300000))
    35     24.8 MiB      0.0 MiB           1       print(max(my_list))

    
Взяты два решения одной задачи - встроенный поиск максимума (включалась дважды) и через циклы
Для запуска было выделено 13.3MiB на запуске первого скрипта 
Затем список по которому проводилось выполнение скрипта занял еще 11.6 MiB 
После выполнения использование памяти снизилось до 19.5 и затем поднялось до 24.8 при использовании памяти
для списка
И при повторном запуске объем использованной памяти был 19.7 + затем опять взялась память на список 5.1

Если сделать первым запуск my_div2 то ситуация с выделением памяти под список будет такой же (результат @profile 
приведен ниже). И также будет идти результат по выделению памяти на запуски

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    32     13.5 MiB     13.5 MiB           1   @profile
    33                                         def my_div2():
    34     25.1 MiB     11.6 MiB           1       my_list = list(range(300000))
    35     25.1 MiB      0.0 MiB           1       print(max(my_list))

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    22     19.7 MiB     19.7 MiB           1   @profile
    23                                         def my_div():
    24     24.9 MiB      5.3 MiB           1       my_list = list(range(300001))
    25     24.9 MiB      0.0 MiB           1       maximum = my_list[0]
    26     24.9 MiB      0.0 MiB      300001       for i in range(1, len(my_list)):
    27     24.9 MiB      0.0 MiB      300000           if my_list[i] > maximum:
    28     24.9 MiB      0.0 MiB      300000               maximum = my_list[i]
    29     24.9 MiB      0.0 MiB           1       print(maximum)

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    32     19.9 MiB     19.9 MiB           1   @profile
    33                                         def my_div2():
    34     24.9 MiB      5.0 MiB           1       my_list = list(range(300000))
    35     24.9 MiB      0.0 MiB           1       print(max(my_list))

"""