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

from memory_profiler import memory_usage, profile
from timeit import default_timer
import random


def my_profiler(func):
    """Декоратор, объединяющий замеры времени и памяти"""

    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        t1 = default_timer()

        r = func(*args, **kwargs)

        m2 = memory_usage()
        t2 = default_timer()

        time_diff = t2 - t1
        mem_diff = m2[0] - m1[0]

        print(f"Выполнение заняло {time_diff} секунд и {mem_diff} Mib")

        return r

    return wrapper


"""Создание списка квадратор четных чисел"""


@my_profiler
def pgm():
    a = [random.randint(-100, 100) for _ in range(50000)]
    new_arr = []

    for item in a:
        if item % 2 == 0:
            new_arr.append(pow(item, 2))

    return new_arr


pgm()


@my_profiler
def pgm2():
    new_arr = [pow(i, 2) for i in [random.randint(-100, 100) for _ in range(50000)] if i % 2 == 0]
    return new_arr


pgm2()


@my_profiler
def pgm3():
    for item in range(50000):
        if item % 2 == 0:
            yield pow(item, 2)


pgm3()

"""Сумма последовательности из n элементов"""


@profile()
def pgm_21(n):
    def recursion(length, el=1.0):
        if length <= 0:
            return 0

        return el + recursion(length - 1, -el / 2)

    return recursion(n)


@profile()
def pgm_2(length):
    val = 0
    el = 1
    for i in range(length):
        val += el
        el = -el / 2

    return val


print(f"Сумма последовательности равна {pgm_2(5000)}")
print(f"Сумма последовательности равна {pgm_21(500)}")

"""
Аналитика 1-й задачи
1-й алгоритм

Результаты замеров:

Memory-profiler:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    54     19.1 MiB     19.1 MiB           1   @profile
    55                                         def pgm():
    56     20.6 MiB      1.5 MiB       50003       a = [random.randint(-100, 100) for _ in range(50000)]
    57     20.6 MiB      0.0 MiB           1       new_arr = []
    58                                         
    59     21.2 MiB      0.6 MiB       50001       for item in a:
    60     21.2 MiB      0.0 MiB       50000           if item % 2 == 0:
    61     21.2 MiB      0.0 MiB       25113               new_arr.append(pow(item, 2))
    62                                         
    63     21.2 MiB      0.0 MiB           1       return new_arr

My_profiler:
Выполнение заняло 0.13910070000000002 секунд и 1.2734375 Mib


Исходя из значений занимаемой памяти 1-го алгоритма, можно сказать,
что на больших списках объёем занимаемой памяти будет очень велик, причина этому,
что список необработанных чисел сначала генирируется, занимая память.



2-й алгоритм

Результаты замеров:

Memory-profiler:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    69     19.1 MiB     19.1 MiB           1   @profile
    70                                         def pgm2():
    71     19.3 MiB      0.2 MiB      100005       new_arr = [pow(i, 2) for i in [random.randint(-100, 100) for _ in range(50000)] if i % 2 == 0]
    72     19.1 MiB     0.0 MiB           1       return new_arr

My_profiler:
Выполнение заняло 0.14188539999999997 секунд и 0.23046875 Mib

В этом алгоритме список генерируется сразу же с обработанными числами, что сокращает использование памяти в 2 раза.


3-й алгоритм
My_profiler:
Выполнение заняло 0.10991130000000002 секунд и 0.0 Mib

В этом алгоритме испоьзуется конструкция yield, образающая генератор,
помогает избавиться от занимаемой алгоритмом памяти, так как генерирует новое число при каждом обращении к генератору.
Это самый легкий алгоритм.



Аналитика 2-й задачи

1-й алгоритм
My_profiler:
Выполнение заняло 0.10740930000000001 секунд и 0.6640625 Mib

Memory-profiler:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    89     19.1 MiB     19.1 MiB           1   @profile()
    90                                         def pgm_21(n):
    91     20.1 MiB      0.9 MiB         502       def recursion(length, el=1.0):
    92     20.1 MiB      0.1 MiB         501           if length <= 0:
    93     20.1 MiB      0.0 MiB           1               return 0
    94                                         
    95     20.1 MiB      0.0 MiB         500           return el + recursion(length - 1, -el / 2)
    96                                         
    97     20.1 MiB      0.0 MiB           1       return recursion(n)

В этом алгоритме использована рекурсия, а значит, что пока идут рекурсивные вызовы, то данные должны храниться в памяти,


2-й алгоритм:
My_profiler: Выполнение заняло 0.17176180000000002 секунд и 0.0 Mib
Memory_profiler:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   100     19.0 MiB     19.0 MiB           1   @profile()
   101                                         def pgm_2(length):
   102     19.0 MiB      0.0 MiB           1       val = 0
   103     19.0 MiB      0.0 MiB           1       el = 1
   104     19.1 MiB      0.0 MiB        5001       for i in range(length):
   105     19.1 MiB      0.0 MiB        5000           val += el
   106     19.1 MiB      0.0 MiB        5000           el = -el / 2
   107                                         
   108     19.1 MiB      0.0 MiB           1       return val
   
Этот алгоритм можно считать самым эффективным по занимаемой памяти, так как из-за отсуствие рекурсии она = 0.
Однако этот алгоритм немного проигрывает рекурсии по времени.
"""
