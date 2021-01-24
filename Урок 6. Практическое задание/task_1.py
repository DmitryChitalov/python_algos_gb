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


@profile
def my_simple_search(num):
    n = 10000
    my_list = []
    for i in range(n + 1):
        my_list.append(i)
    my_list[1] = 0
    i = 2
    while i <= n:
        if my_list[i] != 0:
            j = i + i
            while j <= n:
                my_list[j] = 0
                j = j + i
        i += 1
    my_set = set(my_list)
    my_set.remove(0)
    my_list = list(my_set)
    # del my_set
    my_list.sort()
    return my_list[num - 1]



num = int(input('Введите порядковый номер искомого простого числа: '))
print(my_simple_search(num))


'''
Python 3.8.5 win10 x64
на примере задачи с решетом эратосфена

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    42     18.8 MiB     18.8 MiB           1   @profile
    43                                         def my_simple_search(num):
    44     18.8 MiB      0.0 MiB           1       n = 10000
    45     18.8 MiB      0.0 MiB           1       my_list = []
    46     19.3 MiB      0.0 MiB       10002       for i in range(n + 1):
    47     19.3 MiB      0.5 MiB       10001           my_list.append(i)     # добавление в пустой список=> увеличение памяти
    48     19.3 MiB      0.0 MiB           1       my_list[1] = 0
    49     19.3 MiB      0.0 MiB           1       i = 2
    50     19.3 MiB      0.0 MiB       10000       while i <= n:
    51     19.3 MiB      0.0 MiB        9999           if my_list[i] != 0:
    52     19.3 MiB      0.0 MiB        1229               j = i + i
    53     19.3 MiB      0.0 MiB       24300               while j <= n:
    54     19.3 MiB      0.0 MiB       23071                   my_list[j] = 0
    55     19.3 MiB      0.0 MiB       23071                   j = j + i
    56     19.3 MiB      0.0 MiB        9999           i += 1
    57     19.4 MiB      0.1 MiB           1       my_set = set(my_list)  # снова увеличение в этот раз на создание множества
    58     19.4 MiB      0.0 MiB           1       my_set.remove(0)
    59     19.4 MiB      0.0 MiB           1       my_list = list(my_set)
    60     19.4 MiB      0.0 MiB           1       my_list.sort()
    61     19.4 MiB      0.0 MiB           1       return my_list[num - 1]


4409

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    20     18.7 MiB     18.7 MiB           1   @profile
    21                                         def my_simple_search(num):
    22     18.7 MiB      0.0 MiB           1       n = 10000
    23     18.7 MiB      0.0 MiB           1       my_list = []
    24     19.2 MiB      0.0 MiB       10002       for i in range(n + 1):
    25     19.2 MiB      0.4 MiB       10001           my_list.append(i)
    26     19.2 MiB      0.0 MiB           1       my_list[1] = 0
    27     19.2 MiB      0.0 MiB           1       i = 2
    28     19.2 MiB      0.0 MiB       10000       while i <= n:
    29     19.2 MiB      0.0 MiB        9999           if my_list[i] != 0:
    30     19.2 MiB      0.0 MiB        1229               j = i + i
    31     19.2 MiB      0.0 MiB       24300               while j <= n:
    32     19.2 MiB      0.0 MiB       23071                   my_list[j] = 0
    33     19.2 MiB      0.0 MiB       23071                   j = j + i
    34     19.2 MiB      0.0 MiB        9999           i += 1
    35     19.3 MiB      0.1 MiB           1       my_set = set(my_list)
    36     19.3 MiB      0.0 MiB           1       my_set.remove(0)
    37     19.3 MiB      0.0 MiB           1       my_list = list(my_set)
    38     19.0 MiB     -0.2 MiB           1       del my_set  # удаляем неиспользуемое более множество тем самым освобождая память
    39     19.0 MiB      0.0 MiB           1       my_list.sort()
    40     19.0 MiB      0.0 MiB           1       return my_list[num - 1]


4409
Process finished with exit code 0
'''


