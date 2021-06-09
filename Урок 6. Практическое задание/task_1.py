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


# Функции возвращают сумму ряда 1/n^2 для первых n элементов

@profile()
def my_func():
    series = [1 / i ** 2 for i in range(1, 100000)]
    sum = 0
    for i in range(len(series)):
        sum += series[i]
    return sum


"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    20     19.1 MiB     19.1 MiB           1   @profile()
    21                                         def my_func():
    22     23.6 MiB      4.5 MiB      100002       series = [1 / i ** 2 for i in range(1, 100000)]
    23     23.6 MiB      0.0 MiB           1       sum = 0
    24     23.6 MiB      0.0 MiB      100000       for i in range(len(series)):
    25     23.6 MiB      0.0 MiB       99999           sum += series[i]
    26     23.6 MiB      0.0 MiB           1       return sum
"""


@profile()
def my_func_1():
    series = [1 / i ** 2 for i in range(1, 100000)]
    sum = 0
    for i in range(len(series)):
        sum += series[i]
    del series
    return sum


"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    40     19.4 MiB     19.4 MiB           1   @profile()
    41                                         def my_func_1():
    42     23.5 MiB      4.1 MiB      100002       series = [1/i**2 for i in range(1, 100000)]
    43     23.5 MiB      0.0 MiB           1       sum = 0
    44     23.5 MiB      0.0 MiB      100000       for i in range(len(series)):
    45     23.5 MiB      0.0 MiB       99999           sum += series[i]
    46     19.7 MiB     -3.8 MiB           1       del series
    47     19.7 MiB      0.0 MiB           1       return sum
"""


@profile()
def my_func_2():
    sum = 0
    for i in range(1, 100000):
        sum += 1 / i ** 2

"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    68     20.9 MiB     20.9 MiB           1   @profile()
    69                                         def my_func_2():
    70                                             #return sum([1 / i ** 2 for i in range(1, 100000)])
    71     20.9 MiB      0.0 MiB           1       sum = 0
    72     20.9 MiB      0.0 MiB      100000       for i in range(1, 100000):
    73     20.9 MiB      0.0 MiB       99999           sum += 1 / i ** 2
"""

my_func()
my_func_1()
my_func_2()

"""
ВЫВОДЫ: удаление массива перед завершением функции позволило высвободить память.
Полный отказ от массива сократил код и уменьшил максимально используемый 
функцией размер памяти, однако, сами элементы ряда в итоге нигде не хранятся,
что в реальных задачах может быть неудобно
"""
