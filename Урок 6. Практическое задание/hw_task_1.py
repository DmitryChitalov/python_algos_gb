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
from memory_profiler import profile
from timeit import timeit


@profile
def factorial_1(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num


@profile
def factorial_2(n, total=1):
    while True:
        if n == 1:
            return total
        n, total = n - 1, total * n


@profile
def factorial_3(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


print(timeit('factorial_1(20000)', 'from __main__ import factorial_1', number=1))
print(timeit('factorial_2(20000)', 'from __main__ import factorial_2', number=1))
print(timeit('factorial_3(20000)', 'from __main__ import factorial_3', number=1))

'''
factorial_1(20000)
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    27     18.8 MiB     18.8 MiB           1   @profile
    28                                         def factorial_1(n):
    29     18.8 MiB      0.0 MiB           1       num = 1
    30     19.1 MiB      0.0 MiB       20001       while n >= 1:
    31     19.1 MiB      0.2 MiB       20000           num = num * n
    32     19.1 MiB      0.0 MiB       20000           n = n - 1
    33     19.1 MiB      0.0 MiB           1       return num

3.7590149000000004 --> Время выполнения вычисления.
0.2 MiB --> прирост занимаемой памяти.
18.8 MiB до вызова функции.
19.1 MiB после окончания выполнения функции.
Принудительная очистка памяти не проводилась.


factorial_2(20000)
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    36     19.1 MiB     19.1 MiB           1   @profile
    37                                         def factorial_2(n, total=1):
    38                                             while True:
    39     19.3 MiB      0.0 MiB       20000           if n == 1:
    40     19.3 MiB      0.0 MiB           1               return total
    41     19.3 MiB      0.2 MiB       19999           n, total = n - 1, total * n

2.5088264999999996 --> Время выполнения вычисления.
0.2 MiB --> прирост занимаемой памяти.
19.1 MiB до вызова функции.
19.3 MiB после окончания выполнения функции.
Принудительная очистка памяти не проводилась.


factorial_3(20000)
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    44     19.3 MiB     19.3 MiB           1   @profile
    45                                         def factorial_3(n):
    46     19.3 MiB      0.0 MiB           1       result = 1
    47     19.4 MiB      0.0 MiB       20000       for i in range(2, n + 1):
    48     19.4 MiB      0.1 MiB       19999           result *= i
    49     19.4 MiB      0.0 MiB           1       return result


2.5176523 --> Время выполнения вычисления.
0.1 MiB --> прирост занимаемой памяти.
19.3 MiB до вызова функции.
19.4 MiB после окончания выполнения функции.
Принудительная очистка памяти не проводилась.

Вывод:
Сравнивая три варианта вычисления факториала числа 20000, функция factorial_3(n) имеет преимущество над остальными
функциями в объеме потребляемой памяти на 50% меньше, не смотря на тот факт, что время на выполнение функции
на 0.01 секунды больше в сравнении с функцией factorial_2(n)

Python 3.8.6
Windows 10, 64-разрядная операционная система, процессор x64
'''



