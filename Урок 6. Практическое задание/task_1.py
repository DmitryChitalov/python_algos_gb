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

# 1. Версия Python: 3.8.3
# 2. ОС: Windows 10 64-x

from memory_profiler import profile
from random import randint

# 1-я задача: определение минимального числа в массиве.
# через цикл
@profile
def func_min_val():
    my_list = list(range(100000))
    min_val = my_list[0]
    for el in my_list[1:len(my_list)]:
        if el < min_val:
            min_val = el
    return min_val


# через встроенную функцию
@profile
def func_min_2():
    my_list = list(range(100000))
    return min(my_list)


# if __name__ == "__main__":
#     func_min_val()
#     func_min_2()

"""
Для запуска программы в 1 вар выделено 17,6 Mib, во 2м варианте 17.9 MiB.
Среди данных вариантов - обе программы эффективно использует память.

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    28     17.6 MiB     17.6 MiB           1   @profile
    29                                         def func_min_val():
    30     19.4 MiB      1.9 MiB           1       my_list = list(range(100000))
    31     19.4 MiB      0.0 MiB           1       min_val = my_list[0]
    32     19.9 MiB      0.0 MiB      100000       for el in my_list[1:len(my_list)]:
    33     19.9 MiB      0.0 MiB       99999           if el < min_val:
    34                                                     min_val = el
    35     19.5 MiB     -0.4 MiB           1       return min_val

============================================================
    Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    39     17.9 MiB     17.9 MiB           1   @profile
    40                                         def func_min_2():
    41     19.5 MiB      1.6 MiB           1       my_list = list(range(100000))
    42     19.5 MiB      0.0 MiB           1       return min(my_list)

"""

# 2-я задача: определение максимального числа в массиве.


@profile
def func_max_1(n):
    my_list = []
    max_el = 0
    for _ in range(n):
        a = randint(0, 10000)
        my_list.append(a)
        if a > max_el:
            max_el = a
    print(f'Максимальный элемент - {max_el}')
    del my_list


# через встроенную функцию
@profile
def func_max_2():
    my_list = list(range(100000))
    return max(my_list)


# if __name__ == "__main__":
#     func_max_1(100000)
#     func_max_2()

"""

Для запуска программы в 1 вар выделено 17,6 Mib, во 2м варианте 17.7 MiB.
Среди данных вариантов - 1-я программа наиболее эффективно использует память.

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    85     17.6 MiB     17.6 MiB           1   @profile
    86                                         def func_max_1(n):
    87     17.6 MiB      0.0 MiB           1       my_list = []
    88     17.6 MiB      0.0 MiB           1       max_el = 0
    89     19.6 MiB   -241.2 MiB      100001       for _ in range(n):
    90     19.6 MiB   -241.2 MiB      100000           a = randint(0, 10000)
    91     19.6 MiB   -239.2 MiB      100000           my_list.append(a)
    92     19.6 MiB   -241.2 MiB      100000           if a > max_el:
    93     17.9 MiB      0.0 MiB          14               max_el = a
    94     19.6 MiB      0.0 MiB           1       print(f'Максимальный элемент - {max_el}')
    95     18.0 MiB     -1.6 MiB           1       del my_list



Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   101     17.7 MiB     17.7 MiB           1   @profile
   102                                         def func_max_2():
   103     19.4 MiB      1.8 MiB           1       my_list = list(range(100000))
   104     19.4 MiB      0.0 MiB           1       return max(my_list)
"""