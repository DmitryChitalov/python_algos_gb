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
from functools import reduce
from numpy import array
from pympler import asizeof


@profile
def func_1():
    numbers = [el for el in range(1, 200000 + 1) if not el % 2]
    print(f'asizeof Генераторное выражение: {asizeof.asizeof(numbers)} байт')
    result = reduce(lambda x, y: x * y, numbers)
    return result


@profile
def func_2():
    numbers = (el for el in range(1, 200000 + 1) if not el % 2)
    print(f'asizeof Генератор: {asizeof.asizeof(numbers)} байт')
    result = reduce(lambda x, y: x * y, numbers)
    return result


@profile
def func_3():
    numbers = array([el for el in range(1, 200000 + 1) if not el % 2])
    print(f'asizeof Numpy array: {asizeof.asizeof(numbers)} байт')
    result = reduce(lambda x, y: x * y, numbers)
    return result


print(func_1())
print(func_2())
print(func_3())
"""
Версия Python 3.8
Разрядность ОС х64

Результаты func_1() - Генераторное выражение:
Line #    Mem usage    Increment   Line Contents
================================================
    22     35.8 MiB     35.8 MiB   @profile
    23                             def func_1():
    24     37.9 MiB      0.2 MiB       numbers = [el for el in range(1, 200000 + 1) if not el % 2]
    25     38.1 MiB      0.2 MiB       print(f'asizeof Генераторное выражение: {asizeof.asizeof(numbers)}')
    26     39.4 MiB      0.2 MiB       result = reduce(lambda x, y: x * y, numbers)
    27     39.2 MiB      0.0 MiB       return result

Результаты func_2() - Генератор:   
Line #    Mem usage    Increment   Line Contents
================================================
    30     36.9 MiB     36.9 MiB   @profile
    31                             def func_2():
    32     37.8 MiB      0.0 MiB       numbers = (el for el in range(1, 200000 + 1) if not el % 2)
    33     36.9 MiB      0.0 MiB       print(f'asizeof Генератор: {asizeof.asizeof(numbers)}')
    34     37.8 MiB      0.1 MiB       result = reduce(lambda x, y: x * y, numbers)
    35     37.7 MiB      0.0 MiB       return result

Результаты func_3() - Numpy:
Line #    Mem usage    Increment   Line Contents
================================================
    38     36.8 MiB     36.8 MiB   @profile
    39                             def func_3():
    40     38.3 MiB      0.0 MiB       numbers = array([el for el in range(1, 200000 + 1) if not el % 2])
    41     37.7 MiB      0.0 MiB       print(f'asizeof Numpy array: {asizeof.asizeof(numbers)}')
    42     37.7 MiB      0.0 MiB       result = reduce(lambda x, y: x * y, numbers)
    43     37.7 MiB      0.0 MiB       return result

Наблюдения по результатам @profile:
    Т.к. у меня столбец Increment показывал неверные цифры я ориентировался только на столбец Mem usage.
    По нему видно, что Генераторное выражение занимает 2,1 MiB
                                                 Numpy 1,5 MiB
                                             Генератор 0,9 MiB
    Вывод: 
        Для экономии места лучше всего использовать генератор, так же
        не плохим вариантом будет использование Numpy. А создание объекта через генераторное выражение или
        обычный цикл приведет к наибольшому размеру этого объекта.

Наблюдения по результатам asizeof:
    Генераторное выражение: 2012232 байт
    Numpy array:            400048 байт
    Генератор:              240 байт
    
    Вывод:
        Фун-я asizeof показывает аналогичную зависимость. Меньше всего места в памяти занимают генераторы, чуть больше
        объекты, созданные с помощью Numpy array и больше всего места занимает генераторное выражение и сюда же можно
        отнести создание объекта через обычнй цикл.

Замечание:
    В качесте экономии места при использование генераторных выражений можно удалять ссылки, как только ссылок на объект
    не останется, встроенный сборщик мусора его удалит.
"""
