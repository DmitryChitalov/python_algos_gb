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
import random

array = [random.randint(1, 6) for num in range(1, 10000)]


@profile
def func_1():
    t1 = default_timer()
    m1 = memory_usage()
    print(m1)

    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    print(f'Чаще всего встречается число {num}, ' \
          f'оно появилось в массиве {m} раз(а)')

    t2 = default_timer()
    m2 = memory_usage()

    time_diff = t2 - t1
    memory_diff = m2[0] - m1[0]
    print(f'Выполнение заняло {time_diff} сек и {memory_diff} MIB памяти.')


@profile
def func_2():
    t1 = default_timer()
    m1 = memory_usage()
    print(m1)

    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    print(f'Чаще всего встречается число {elem}, ' \
          f'оно появилось в массиве {max_2} раз(а)')

    t2 = default_timer()
    m2 = memory_usage()

    time_diff = t2 - t1
    memory_diff = m2[0] - m1[0]
    print(f'Выполнение заняло {time_diff} сек и {memory_diff} MIB памяти.')


func_1()
func_2()

"""
Для запуска программы было выделено 19,3 MiB.
При поиске наиболее встречающегося числа в списке 'array' выделяется разное колличество памяти, в зависимости от способа.
Самым быстрым и не затратным по памяти является первый способ.

[19.33203125]
Чаще всего встречается число 4, оно появилось в массиве 1692 раз(а)
Выполнение заняло 5.546612 сек и 0.0078125 MIB памяти.
Filename: C:\Диск D\Программирование\Курс Алгоритмы и структуры данных на Python базовый курс\6\task_1_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    30     19.3 MiB     19.3 MiB           1   @profile
    31                                         def func_1():
    32     19.3 MiB      0.0 MiB           1       t1 = default_timer()
    33     19.3 MiB      0.0 MiB           1       m1 = memory_usage()
    34     19.3 MiB      0.0 MiB           1       print(m1)
    35                                         
    36     19.3 MiB      0.0 MiB           1       m = 0
    37     19.3 MiB      0.0 MiB           1       num = 0
    38     19.3 MiB      0.0 MiB       10000       for i in array:
    39     19.3 MiB      0.0 MiB        9999           count = array.count(i)
    40     19.3 MiB      0.0 MiB        9999           if count > m:
    41     19.3 MiB      0.0 MiB           2               m = count
    42     19.3 MiB      0.0 MiB           2               num = i
    43     19.3 MiB      0.0 MiB           2       print(f'Чаще всего встречается число {num}, ' \
    44     19.3 MiB      0.0 MiB           1             f'оно появилось в массиве {m} раз(а)')
    45                                         
    46     19.3 MiB      0.0 MiB           1       t2 = default_timer()
    47     19.3 MiB      0.0 MiB           1       m2 = memory_usage()
    48                                         
    49     19.3 MiB      0.0 MiB           1       time_diff = t2 - t1
    50     19.3 MiB      0.0 MiB           1       memory_diff = m2[0] - m1[0]
    51     19.3 MiB      0.0 MiB           1       print(f'Выполнение заняло {time_diff} сек и {memory_diff} MIB памяти.')


[19.33984375]
Чаще всего встречается число 4, оно появилось в массиве 1692 раз(а)
Выполнение заняло 5.7747478999999995 сек и 0.3203125 MIB памяти.
Filename: C:\Диск D\Программирование\Курс Алгоритмы и структуры данных на Python базовый курс\6\task_1_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    54     19.3 MiB     19.3 MiB           1   @profile
    55                                         def func_2():
    56     19.3 MiB      0.0 MiB           1       t1 = default_timer()
    57     19.3 MiB      0.0 MiB           1       m1 = memory_usage()
    58     19.3 MiB      0.0 MiB           1       print(m1)
    59                                         
    60     19.3 MiB      0.0 MiB           1       new_array = []
    61     19.7 MiB      0.0 MiB       10000       for el in array:
    62     19.7 MiB      0.0 MiB        9999           count2 = array.count(el)
    63     19.7 MiB      0.3 MiB        9999           new_array.append(count2)
    64                                         
    65     19.7 MiB      0.0 MiB           1       max_2 = max(new_array)
    66     19.7 MiB      0.0 MiB           1       elem = array[new_array.index(max_2)]
    67     19.7 MiB      0.0 MiB           2       print(f'Чаще всего встречается число {elem}, ' \
    68     19.7 MiB      0.0 MiB           1             f'оно появилось в массиве {max_2} раз(а)')
    69                                         
    70     19.7 MiB      0.0 MiB           1       t2 = default_timer()
    71     19.7 MiB      0.0 MiB           1       m2 = memory_usage()
    72                                         
    73     19.7 MiB      0.0 MiB           1       time_diff = t2 - t1
    74     19.7 MiB      0.0 MiB           1       memory_diff = m2[0] - m1[0]
    75     19.7 MiB      0.0 MiB           1       print(f'Выполнение заняло {time_diff} сек и {memory_diff} MIB памяти.')



Process finished with exit code 0
"""
