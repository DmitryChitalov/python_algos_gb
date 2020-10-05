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
from numpy import array
from pympler import asizeof
from functools import reduce


@profile
def func1():
    print('func1')
    numbers = [i for i in range(1, 50000)]
    print(asizeof.asizeof(numbers))
    result = reduce(lambda x, y: x * y, numbers)
    return result


@profile
def func2():
    print('func2')
    numbers = (i for i in range(1, 50000))
    print(asizeof.asizeof(numbers))
    result = reduce(lambda x, y: x * y, numbers)
    return result


@profile
def func3():
    print('func3')
    numbers = array([i for i in range(1, 50000)])
    print(asizeof.asizeof(numbers))
    result = reduce(lambda x, y: x * y, numbers)
    return result


print(func1())
print(func2())
print(func3())

"""
Генераторное выражение:
Line #    Mem usage    Increment   Line Contents
================================================
    22     22.5 MiB     22.5 MiB   @profile
    23                             def func1():
    24     22.5 MiB      0.0 MiB       print('func1')
    25     23.8 MiB      0.1 MiB       numbers = [i for i in range(1, 50000)]
    26     23.7 MiB      0.0 MiB       print(asizeof.asizeof(numbers))
    27     24.2 MiB      0.1 MiB       result = reduce(lambda x, y: x * y, numbers)
    28     24.2 MiB      0.0 MiB       return result
    
@profile показывает что генераторное выражение занимает 1.3 MiB
asizeof 1003232 байта


Генератор:
Line #    Mem usage    Increment   Line Contents
================================================
    31     23.1 MiB     23.1 MiB   @profile
    32                             def func2():
    33     23.1 MiB      0.0 MiB       print('func2')
    34     23.8 MiB      0.0 MiB       numbers = (i for i in range(1, 50000))
    35     23.1 MiB      0.0 MiB       print(asizeof.asizeof(numbers))
    36     23.8 MiB      0.1 MiB       result = reduce(lambda x, y: x * y, numbers)
    37     23.8 MiB      0.0 MiB       return result
    
@profile показывает что генератор занимает 0.7 MiB
asizeof 240 байта


Массив numpy:
Line #    Mem usage    Increment   Line Contents
================================================
    40     23.4 MiB     23.4 MiB   @profile
    41                             def func3():
    42     23.4 MiB      0.0 MiB       print('func3')
    43     24.4 MiB      0.2 MiB       numbers = array([i for i in range(1, 50000)])
    44     23.9 MiB      0.0 MiB       print(asizeof.asizeof(numbers))
    45     23.9 MiB      0.0 MiB       result = reduce(lambda x, y: x * y, numbers)
    46     23.9 MiB      0.0 MiB       return result
    
@profile показывает что генераторное выражение занимает 1 MiB
asizeof 200048 байта

Анализ:
Лучше всего экономит память генератор,
больше всего памяти занимает генераторное выражение,
использование array из библиотеки numpy экономит память
"""