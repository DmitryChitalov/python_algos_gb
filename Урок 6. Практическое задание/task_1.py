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


import random, time
from memory_profiler import profile


def time_dif(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args)
        print(f"Time to complete function {func.__name__} is: {time.time() - start_time}")
    return wrapper


def list_gen(length):
    for i in range(length):
        yield random.randint(0, 5000)


# Поиск минимума в массиве, сложность O(n2)
@profile
def min_str_on2():
    ex_list = [el for el in list_gen(2000)]
    min = ex_list[0]
    for i in range(1, len(ex_list)):
        for j in range(i + 1, len(ex_list)):
            if ex_list[j] < min:
                min = ex_list[j]
    del ex_list
    return min


# Поиск минимума в массиве, сложность O(n)
@time_dif
@profile
def min_str_on():
    ex_list = list(range(500000))
    min_value = ex_list[0]
    for el in ex_list:
        if min_value > el:
            min_value = el
    del ex_list
    return min_value


@time_dif
@profile
def euclid(a, b):
    sa = a
    sb = b
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


@time_dif
@profile
def erathosfenes_basic(n):
    a = [i for i in range(n + 1)]
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    a = set(a)
    a.remove(0)
    a = list(a)
    return a


#min_str_on2()
#min_str_on()
euclid(154542, 1657)
#erathosfenes_basic(150000)

"""
ОС - W10 64-bit
Python 3.8
Сравнил два алгоритма из первого урока.
В случае с О(n) сложностью сделал создание списка обычным способом.
Ихначально выделилось 18MiB.
Для списка потом дополнительно 19.2MiB
Потом удалил его и эта память высвободилась.

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    47     18.6 MiB     18.6 MiB           1   @profile
    48                                         def min_str_on():
    49     37.9 MiB     19.2 MiB           1       ex_list = list(range(500000))
    50     37.9 MiB      0.0 MiB           1       min_value = ex_list[0]
    51     37.9 MiB      0.0 MiB      500001       for el in ex_list:
    52     37.9 MiB      0.0 MiB      500000           if min_value > el:
    53                                                     min_value = el
    54     18.8 MiB    -19.1 MiB           1       del ex_list
    55     18.8 MiB      0.0 MiB           1       return min_value 

В случае с O(n2) воспользовался генератором.
Изначально выделилось 18.7MiB
А для списка дополнительно не выделилось памяти - хватило изначальной.
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    35     18.7 MiB     18.7 MiB           1   @profile
    36                                         def min_str_on2():
    37     18.8 MiB      0.0 MiB        1403       ex_list = [el for el in list_gen(1400)]
    38     18.8 MiB      0.0 MiB           1       min = ex_list[0]
    39     18.8 MiB      0.0 MiB        1400       for i in range(1, len(ex_list)):
    40     18.8 MiB      0.0 MiB      979300           for j in range(i + 1, len(ex_list)):
    41     18.8 MiB      0.0 MiB      977901               if ex_list[j] < min:
    42     18.8 MiB      0.0 MiB           8                   min = ex_list[j]
    43     18.8 MiB      0.0 MiB           1       del ex_list
    44     18.8 MiB      0.0 MiB           1       return min
    
    
И, судя по всему, для больших значений списка профайлер работает не совсем корректно.
Не думаю, что для списка он выделял почти 40 ГБ памяти
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    35     18.6 MiB     18.6 MiB           1   @profile
    36                                         def min_str_on2():
    37     18.6 MiB      0.0 MiB        2003       ex_list = [el for el in list_gen(2000)]
    38     18.6 MiB      0.0 MiB           1       min = ex_list[0]
    39     18.7 MiB    -65.8 MiB        2000       for i in range(1, len(ex_list)):
    40     18.7 MiB -36971.0 MiB     1999000           for j in range(i + 1, len(ex_list)):
    41     18.7 MiB -36905.3 MiB     1997001               if ex_list[j] < min:
    42     18.6 MiB      0.0 MiB          10                   min = ex_list[j]
    43     18.6 MiB     -0.1 MiB           1       return min


Алгорит Эвклида не требует дополнительного большого объема памяти - изначально 18.6 MiB
Дальше все Increment по нулям:
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    68     18.6 MiB     18.6 MiB           1   @time_dif
    69                                         @profile
    70                                         def euclid(a, b):
    71     18.6 MiB      0.0 MiB           1       sa = a
    72     18.6 MiB      0.0 MiB           1       sb = b
    73     18.6 MiB      0.0 MiB         115       while a != b:
    74     18.6 MiB      0.0 MiB         114           if a > b:
    75     18.6 MiB      0.0 MiB         104               a -= b
    76                                                 else:
    77     18.6 MiB      0.0 MiB          10               b -= a
    78     18.6 MiB      0.0 MiB           1       return a
      
Модифицированное решето Эратосфена:
Изначально 18.7MiB
Потом для списка выделили порядка 7MiB.
Потом при преобразовании переменных высвобождается порядка 1.4 MiB и 0.5 MiB
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    81     18.7 MiB     18.7 MiB           1   @time_dif
    82                                         @profile
    83                                         def erathosfenes_basic(n):
    84     25.4 MiB  -9391.1 MiB      150004       a = [i for i in range(n + 1)]
    85     25.3 MiB     -0.1 MiB           1       a[1] = 0
    86     25.3 MiB      0.0 MiB           1       i = 2
    87     25.3 MiB      0.0 MiB      150000       while i <= n:
    88     25.3 MiB      0.0 MiB      149999           if a[i] != 0:
    89     25.3 MiB      0.0 MiB       13848               j = i + i
    90     25.3 MiB      0.0 MiB      405022               while j <= n:
    91     25.3 MiB      0.0 MiB      391174                   a[j] = 0
    92     25.3 MiB      0.0 MiB      391174                   j = j + i
    93     25.3 MiB      0.0 MiB      149999           i += 1
    94     24.0 MiB     -1.4 MiB           1       a = set(a)
    95     24.0 MiB      0.0 MiB           1       a.remove(0)
    96     23.4 MiB     -0.5 MiB           1       a = list(a)
    97     23.4 MiB      0.0 MiB           1       return a
"""