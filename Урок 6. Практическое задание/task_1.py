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

python 3.8.2
Windows 10 64 bit
"""

from memory_profiler import profile
from timeit import timeit
from random import randint


nums = [randint(10, 100) for _ in range(10)]


# @profile

@profile
def revers_number(number_str, i):
    return i if number_str == 0 else revers_number(number_str // 10, i * 10 + number_str % 10)


@profile
def revers_number_2(number_str):
    return number_str[::-1]


if __name__ == '__main__':
    usr_number = 232323 ** 23
    print(f'Перевернутое число 1: {revers_number(usr_number, 0)}')
    print(f'Перевернутое число 2: {revers_number_2(str(usr_number))}')

# print(timeit("revers_number()", setup="from __main__ import revers_number", number=1))
# print(timeit("revers_number2()", setup="from __main__ import revers_number2", number=1))

"""
Сделал реверс числа двумя способами
1. Рекурсивно.
Получили 125 вхождений 
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    30     17.0 MiB     17.0 MiB         125   @profile
    31                                         def revers_number(number_str, i):
    32     17.0 MiB      0.0 MiB         125       return i if number_str == 0 else revers_number(number_str // 10, i * 10 + number_str % 10)


Перевернутое число 1: 7664311565374818870731874848654098143686662301019698768930101496910239232969553949786698340384765900897293523990989849990362
Filename: D:/GitHub/python_algos_gb/Урок 6. Практическое задание/task_1.py

=============================================================


2. Через срез
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    35     17.0 MiB     17.0 MiB           1   @profile
    36                                         def revers_number_2(number_str):
    37     17.0 MiB      0.0 MiB           1       return number_str[::-1]


Рекурсивно явно менее эффективный метод, т.к было 125 вхождений и для каждого вхождения использовалось по 17 MB памяти. 

"""