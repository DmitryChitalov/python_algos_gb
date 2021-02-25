"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from random import randint
from functools import reduce
from memory_profiler import profile


@profile
def list_min_v2(list):
    min_value = list[0]
    for i in list:
        if i < min_value:
            min_value = i
    return min_value


list1 = [randint(0, 100) for i in range(200000)]
print(list_min_v2(list1))

"""
Поиск минимальнго элемента в массиве 
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    29     17.7 MiB     17.7 MiB           1   @profile
    30                                         def list_min_v2(list):
    31     17.7 MiB      0.0 MiB           1       min_value = list[0]
    32     17.7 MiB      0.0 MiB         201       for i in list:
    33     17.7 MiB      0.0 MiB         200           if i < min_value:
    34     17.7 MiB      0.0 MiB           4               min_value = i
    35     17.7 MiB      0.0 MiB           1       return min_value
Память выделяется сразу при создании массива. Далее при сравнении новая память уже не требуется    
"""
@profile
def list_min_v1(list):
    for i in list:
        is_min = True
        for j in list:
            if i > j:
                is_min = False
        if is_min:
            return i
list1 = [randint(0, 100) for i in range(200)]
print(list_min_v1(list1))
"""
Поиск минимальнго элемента в массиве 
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    53     17.7 MiB     17.7 MiB           1   @profile
    54                                         def list_min_v1(list):
    55     17.7 MiB      0.0 MiB         106       for i in list:
    56     17.7 MiB      0.0 MiB         106           is_min = True
    57     17.7 MiB      0.0 MiB       21306           for j in list:
    58     17.7 MiB      0.0 MiB       21200               if i > j:
    59     17.7 MiB      0.0 MiB        9548                   is_min = False
    60     17.7 MiB      0.0 MiB         106           if is_min:
    61     17.7 MiB      0.0 MiB           1               return i
Память выделяется сразу при создании массива. Далее при сравнении новая память уже не требуется.
По сравнению с первой реализацией, этот вариант требует столько же памяти, но работает медленнее
С точки зрения использования памяти пример оказался не показательным.
"""