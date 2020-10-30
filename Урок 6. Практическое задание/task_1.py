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

usr_number = 23245678019999


@profile
def revers_all(usr_number):
    def revers_number(number_str, i=0):
        return i if number_str == 0 else revers_number(number_str // 10, i * 10 + number_str % 10)
    print(f'{revers_number(usr_number)}')


@profile
def revers_number_2(number_str):
    return number_str[::-1]


if __name__ == '__main__':

    {revers_all(usr_number)}
    print(f'Перевернутое число 2: {revers_number_2(str(usr_number))}')

# print(timeit("revers_number()", setup="from __main__ import revers_number", number=1))
# print(timeit("revers_number2()", setup="from __main__ import revers_number2", number=1))

"""
Сделал реверс числа двумя способами
1. Рекурсивно.
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    27     15.7 MiB     15.7 MiB           1   @profile
    28                                         def revers_all(usr_number):
    29     15.7 MiB      0.0 MiB          16       def revers_number(number_str, i=0):
    30     15.7 MiB      0.0 MiB          15           return i if number_str == 0 else revers_number(number_str // 10, i * 10 + number_str % 10)
    31     15.7 MiB      0.0 MiB           1       print(f'{revers_number(usr_number)}')



=============================================================


2. Через срез
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    34     15.7 MiB     15.7 MiB           1   @profile
    35                                         def revers_number_2(number_str):
    36     15.7 MiB      0.0 MiB           1       return number_str[::-1]


Рекурсивно явно менее эффективный метод, т.к в 29 строке получилось 16 вхождений, в 30 строке 15  вхождений
 и для каждого вхождения использовалось по 17 MB памяти. 

"""