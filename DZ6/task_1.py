"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-5 ваших разных скриптов!.
Сделать их разные реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from memory_profiler import profile, memory_usage
from timeit import default_timer


@profile
def func_1(nums):
    t1 = default_timer()
    m1 = memory_usage()
    print(m1)

    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    #    return new_arr

    t2 = default_timer()
    m2 = memory_usage()

    time_diff = t2 - t1
    memory_diff = m2[0] - m1[0]
    print(f'Выполнение заняло {time_diff} сек и {memory_diff} MIB памяти.')
    del (new_arr)


@profile
def func_2(nums):
    t1 = default_timer()
    m1 = memory_usage()
    print(m1)

    new_arr = nums[::2]
    #    return new_arr

    t2 = default_timer()
    m2 = memory_usage()

    time_diff = t2 - t1
    memory_diff = m2[0] - m1[0]
    print(f'Выполнение заняло {time_diff} сек и {memory_diff} MIB памяти.')
    del (new_arr)


@profile
def func_3(nums):
    t1 = default_timer()
    m1 = memory_usage()
    print(m1)

    new_arr = [i for i in nums if not i % 2]
    #    return new_arr

    t2 = default_timer()
    m2 = memory_usage()

    time_diff = t2 - t1
    memory_diff = m2[0] - m1[0]
    print(f'Выполнение заняло {time_diff} сек и {memory_diff} MIB памяти.')
    del (new_arr)


@profile
def func_4(nums):
    t1 = default_timer()
    m1 = memory_usage()
    print(m1)

    new_arr = [i for k, i in enumerate(nums) if not k % 2]
    #    return new_arr

    t2 = default_timer()
    m2 = memory_usage()

    time_diff = t2 - t1
    memory_diff = m2[0] - m1[0]
    print(f'Выполнение заняло {time_diff} сек и {memory_diff} MIB памяти.')
    del (new_arr)


nums = [i for i in range(100000)]

func_1(nums)
func_2(nums)
func_3(nums)
func_4(nums)

"""
Для запуска программы было выделено 23.8 MiB.
При создании списка "new_arr" выделяется разное колличество памяти, в зависимости от способа.
Самым быстрым и не затратным по памяти является второй способ.
После выполнения программы каждым из способов удалил список "new_arr" , тем самым
освобождая память.
[23.83984375]
Выполнение заняло 24.3979289 сек и 1.5078125 MIB памяти.
Filename: C:\Диск D\Программирование\Курс Алгоритмы и структуры данных на Python базовый курс\6\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    27     23.8 MiB     23.8 MiB           1   @profile
    28                                         def func_1(nums):
    29     23.8 MiB      0.0 MiB           1       t1 = default_timer()
    30     23.8 MiB      0.0 MiB           1       m1 = memory_usage()
    31     23.8 MiB      0.0 MiB           1       print(m1)
    32                                         
    33     23.8 MiB      0.0 MiB           1       new_arr = []
    34     25.3 MiB      0.0 MiB      100001       for i in range(len(nums)):
    35     25.3 MiB      1.5 MiB      100000           if nums[i] % 2 == 0:
    36     25.3 MiB      0.0 MiB       50000               new_arr.append(i)
    37                                             #    return new_arr
    38                                         
    39     25.3 MiB      0.0 MiB           1       t2 = default_timer()
    40     25.3 MiB      0.0 MiB           1       m2 = memory_usage()
    41                                         
    42     25.3 MiB      0.0 MiB           1       time_diff = t2 - t1
    43     25.3 MiB      0.0 MiB           1       memory_diff = m2[0] - m1[0]
    44     25.3 MiB      0.0 MiB           1       print(f'Выполнение заняло {time_diff} сек и {memory_diff} MIB памяти.')
    45     24.1 MiB     -1.2 MiB           1       del (new_arr)


[24.09765625]
Выполнение заняло 0.10265629999999959 сек и 0.0 MIB памяти.
Filename: C:\Диск D\Программирование\Курс Алгоритмы и структуры данных на Python базовый курс\6\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    48     24.1 MiB     24.1 MiB           1   @profile
    49                                         def func_2(nums):
    50     24.1 MiB      0.0 MiB           1       t1 = default_timer()
    51     24.1 MiB      0.0 MiB           1       m1 = memory_usage()
    52     24.1 MiB      0.0 MiB           1       print(m1)
    53                                         
    54     24.1 MiB      0.0 MiB           1       new_arr = nums[::2]
    55                                             #    return new_arr
    56                                         
    57     24.1 MiB      0.0 MiB           1       t2 = default_timer()
    58     24.1 MiB      0.0 MiB           1       m2 = memory_usage()
    59                                         
    60     24.1 MiB      0.0 MiB           1       time_diff = t2 - t1
    61     24.1 MiB      0.0 MiB           1       memory_diff = m2[0] - m1[0]
    62     24.1 MiB      0.0 MiB           1       print(f'Выполнение заняло {time_diff} сек и {memory_diff} MIB памяти.')
    63     23.5 MiB     -0.6 MiB           1       del (new_arr)


[23.53125]
Выполнение заняло 9.834880499999997 сек и 0.41796875 MIB памяти.
Filename: C:\Диск D\Программирование\Курс Алгоритмы и структуры данных на Python базовый курс\6\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    66     23.5 MiB     23.5 MiB           1   @profile
    67                                         def func_3(nums):
    68     23.5 MiB      0.0 MiB           1       t1 = default_timer()
    69     23.5 MiB      0.0 MiB           1       m1 = memory_usage()
    70     23.5 MiB      0.0 MiB           1       print(m1)
    71                                         
    72     23.9 MiB      0.4 MiB      100003       new_arr = [i for i in nums if not i % 2]
    73                                             #    return new_arr
    74                                         
    75     23.9 MiB      0.0 MiB           1       t2 = default_timer()
    76     23.9 MiB      0.0 MiB           1       m2 = memory_usage()
    77                                         
    78     23.9 MiB      0.0 MiB           1       time_diff = t2 - t1
    79     23.9 MiB      0.0 MiB           1       memory_diff = m2[0] - m1[0]
    80     23.9 MiB      0.0 MiB           1       print(f'Выполнение заняло {time_diff} сек и {memory_diff} MIB памяти.')
    81     23.9 MiB      0.0 MiB           1       del (new_arr)


[23.94921875]
Выполнение заняло 9.884816299999997 сек и 0.0 MIB памяти.
Filename: C:\Диск D\Программирование\Курс Алгоритмы и структуры данных на Python базовый курс\6\task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    84     23.9 MiB     23.9 MiB           1   @profile
    85                                         def func_4(nums):
    86     23.9 MiB      0.0 MiB           1       t1 = default_timer()
    87     23.9 MiB      0.0 MiB           1       m1 = memory_usage()
    88     23.9 MiB      0.0 MiB           1       print(m1)
    89                                         
    90     23.9 MiB      0.0 MiB      100003       new_arr = [i for k, i in enumerate(nums) if not k % 2]
    91                                             #    return new_arr
    92                                         
    93     23.9 MiB      0.0 MiB           1       t2 = default_timer()
    94     23.9 MiB      0.0 MiB           1       m2 = memory_usage()
    95                                         
    96     23.9 MiB      0.0 MiB           1       time_diff = t2 - t1
    97     23.9 MiB      0.0 MiB           1       memory_diff = m2[0] - m1[0]
    98     23.9 MiB      0.0 MiB           1       print(f'Выполнение заняло {time_diff} сек и {memory_diff} MIB памяти.')
    99     23.9 MiB      0.0 MiB           1       del (new_arr)



Process finished with exit code 0

"""