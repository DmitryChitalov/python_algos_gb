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
from sys import setrecursionlimit, getrecursionlimit
from random import randint


def get_uint(msg='', err=''):
    while True:
        res = input(('Enter Unsigned Int number: ', msg)[bool(msg)])
        if res != '':
            try:
                res = int(res)
            except ValueError:
                pass
            else:
                return res
        print(('This is not UInt, try again, please!', err)[bool(err)])


@profile
def find_primes_from_list(n):
    lst = [a for a in range(1, n + 1)]
    primes = []
    for el in lst:
        prime = True
        for div in range(2, (el, el // 2)[el > 4]):
            if not (el % div):
                prime = False
                break
        if prime and el - 1:
            primes.append(el)
    return primes


@profile
def find_primes_gen(n):
    def wrapper(arg):
        for el in range(1, n + 1):
            prime = True
            for div in range(2, (el, el // 2)[el > 4]):
                if not (el % div):
                    prime = False
                    break
            if prime and el - 1:
                yield el
    return list(wrapper(n))


max_num = get_uint()
find_primes_from_list(max_num)
list(find_primes_gen(max_num))


'''
Enter Unsigned Int number: 10000
Filename: /home/rt/Обучение/GB/Алгоритмы и структуры данных на Python. Базовый курс 110121/git/python_algos_gb/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    36     17.0 MiB     17.0 MiB           1   @profile
    37                                         def find_primes_from_list(n):
    38     17.6 MiB      0.6 MiB       10003       lst = [a for a in range(1, n + 1)]
    39     17.6 MiB      0.0 MiB           1       primes = []
    40     17.6 MiB      0.0 MiB       10001       for el in lst:
    41     17.6 MiB      0.0 MiB       10000           prime = True
    42     17.6 MiB      0.0 MiB     2907644           for div in range(2, (el, el // 2)[el > 4]):
    43     17.6 MiB      0.0 MiB     2906414               if not (el % div):
    44     17.6 MiB      0.0 MiB        8770                   prime = False
    45     17.6 MiB      0.0 MiB        8770                   break
    46     17.6 MiB      0.0 MiB       10000           if prime and el - 1:
    47     17.6 MiB      0.0 MiB        1229               primes.append(el)
    48     17.6 MiB      0.0 MiB           1       return primes


Filename: /home/rt/Обучение/GB/Алгоритмы и структуры данных на Python. Базовый курс 110121/git/python_algos_gb/Урок 6. Практическое задание/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    51     17.3 MiB     17.3 MiB           1   @profile
    52                                         def find_primes_gen(n):
    53     17.3 MiB      0.0 MiB           2       def wrapper(arg):
    54     17.3 MiB      0.0 MiB       10001           for el in range(1, n + 1):
    55     17.3 MiB      0.0 MiB       10000               prime = True
    56     17.3 MiB      0.0 MiB     2907644               for div in range(2, (el, el // 2)[el > 4]):
    57     17.3 MiB      0.0 MiB     2906414                   if not (el % div):
    58     17.3 MiB      0.0 MiB        8770                       prime = False
    59     17.3 MiB      0.0 MiB        8770                       break
    60     17.3 MiB      0.0 MiB       10000               if prime and el - 1:
    61     17.3 MiB      0.0 MiB        2458                   yield el
    62     17.3 MiB      0.0 MiB           1       return list(wrapper(n))


В первом варианте (строка 38) числовой ряд хранится в списке и на это тратится около 600 KiB памяти
Во втором варианте этих затрат удалось избежать
'''