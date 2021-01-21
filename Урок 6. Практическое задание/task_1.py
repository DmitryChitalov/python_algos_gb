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

# Python 3.8.5, Windows x64
from memory_profiler import profile
from random import randrange
import os
import psutil
"""
Приведены три алгоритма в них определяется число,
которое встречается в массиве чаще всего.
"""

# Цикл, перебирающий словарь и считающий появления элемента
@profile
def func_1(array):
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'

# Добавление элемента в новый список и поиск в нем с помощью встроенной функции
@profile
def func_2(array):
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

# Использование функции max в одной строке
@profile
def func_3(array):
    number = max(array, key=array.count)
    return f'Чаще всего встречается число {number}, ' \
           f'оно появилось в массиве {array.count(number)} раз(а)'

array = [randrange(-100, 100) for i in range(10000)]
print(func_1(array))
print(func_2(array))
print(func_3(array))



"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    27     29.3 MiB     29.3 MiB           1   @profile
    28                                         def func_1(array):
    29     29.3 MiB      0.0 MiB           1       m = 0
    30     29.3 MiB      0.0 MiB           1       num = 0
    31     29.3 MiB      0.0 MiB       10001       for i in array:
    32     29.3 MiB      0.0 MiB       10000           count = array.count(i)
    33     29.3 MiB      0.0 MiB       10000           if count > m:
    34     29.3 MiB      0.0 MiB           3               m = count
    35     29.3 MiB      0.0 MiB           3               num = i
    36     29.3 MiB      0.0 MiB           1       return f'Чаще всего встречается число {num}, ' \
    37                                                    f'оно появилось в массиве {m} раз(а)'


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    40     29.3 MiB     29.3 MiB           1   @profile
    41                                         def func_2(array):
    42     29.3 MiB      0.0 MiB           1       new_array = []
    43     29.4 MiB      0.0 MiB       10001       for el in array:
    44     29.4 MiB      0.0 MiB       10000           count2 = array.count(el)
    45     29.4 MiB      0.1 MiB       10000           new_array.append(count2)
    46                                         
    47     29.4 MiB      0.0 MiB           1       max_2 = max(new_array)
    48     29.4 MiB      0.0 MiB           1       elem = array[new_array.index(max_2)]
    49     29.4 MiB      0.0 MiB           1       return f'Чаще всего встречается число {elem}, ' \
    50                                                    f'оно появилось в массиве {max_2} раз(а)'


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    53     29.4 MiB     29.4 MiB           1   @profile
    54                                         def func_3(array):
    55     29.4 MiB      0.0 MiB           1       number = max(array, key=array.count)
    56     29.4 MiB      0.0 MiB           1       return f'Чаще всего встречается число {number}, ' \
    57                                                    f'оно появилось в массиве {array.count(number)} раз(а)'


Вывод: Использование одной строки с функцией max сокращает количество 
использованного времени практически в два раза и в три по сравнению с циклом.
"""