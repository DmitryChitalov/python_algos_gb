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
import sys
from memory_profiler import profile
import hashlib


@profile
def resheto_erastofena(k):
    a = []
    n = 10000
    for i in range(n + 1):
        a.append(i)
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    res = list(filter(lambda x: x > 0, a))[k-1]
    return res


@profile
def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n

resheto_erastofena(10)
simple(10)
"""
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    21     18.8 MiB     18.8 MiB           1   @profile
    22                                         def resheto_erastofena(k):
    23     18.8 MiB      0.0 MiB           1       a = []
    24     18.8 MiB      0.0 MiB           1       n = 10000
    25     19.2 MiB      0.0 MiB       10002       for i in range(n + 1):
    26     19.2 MiB      0.3 MiB       10001           a.append(i)
    27     19.2 MiB      0.0 MiB           1       a[1] = 0
    28     19.2 MiB      0.0 MiB           1       i = 2
    29     19.2 MiB      0.0 MiB       10000       while i <= n:
    30     19.2 MiB      0.0 MiB        9999           if a[i] != 0:
    31     19.2 MiB      0.0 MiB        1229               j = i + i
    32     19.2 MiB      0.0 MiB       24300               while j <= n:
    33     19.2 MiB      0.0 MiB       23071                   a[j] = 0
    34     19.2 MiB      0.0 MiB       23071                   j = j + i
    35     19.2 MiB      0.0 MiB        9999           i += 1
    36     19.2 MiB      0.0 MiB       20003       res = list(filter(lambda x: x > 0, a))[k-1]
    37     19.2 MiB      0.0 MiB           1       return res

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    40     19.2 MiB     19.2 MiB           1   @profile
    41                                         def simple(i):
    42                                             "Без использования «Решета Эратосфена»"
    43     19.2 MiB      0.0 MiB           1       count = 1
    44     19.2 MiB      0.0 MiB           1       n = 2
    45     19.2 MiB      0.0 MiB          28       while count <= i:
    46     19.2 MiB      0.0 MiB          28           t = 1
    47     19.2 MiB      0.0 MiB          28           is_simple = True
    48     19.2 MiB      0.0 MiB         182           while t <= n:
    49     19.2 MiB      0.0 MiB         172               if n % t == 0 and t != 1 and t != n:
    50     19.2 MiB      0.0 MiB          18                   is_simple = False
    51     19.2 MiB      0.0 MiB          18                   break
    52     19.2 MiB      0.0 MiB         154               t += 1
    53     19.2 MiB      0.0 MiB          28           if is_simple:
    54     19.2 MiB      0.0 MiB          10               if count == i:
    55     19.2 MiB      0.0 MiB           1                   break
    56     19.2 MiB      0.0 MiB           9               count += 1
    57     19.2 MiB      0.0 MiB          27           n += 1
    58     19.2 MiB      0.0 MiB           1       return n
    
При использовании двух алгоритмов был замечен прирост используемой памяти только в функции с использованием
«Решета Эратосфена». Это обусловлено тем, что мы заранее резервируем место для данных с запасом. По моему
мнению, это является узким местом этого алгоритма, что делает его не универсальным. 
"""