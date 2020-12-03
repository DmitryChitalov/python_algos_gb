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
from random import randint
import math
import timeit


def timer_decor(func_name):
    def wrapper(arg):
        start_time = time.time()
        func_name(arg)
        end_time = time.time()
        timer = end_time - start_time
        print("Функция ", func_name, ". Затраченное время = ", timer)

    return wrapper


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


@profile
def resheto(n):
    if n > 10:
        koef = n // int(math.log10(n))
    else:
        koef = n
    arrsize = n * koef
    arr = list([i for i in range(arrsize + 1)])
    i = 2
    k = 0
    while (k < n) and (i <= arrsize):
        if arr[i] != 0:
            k += 1
            j = i + i
            while j <= arrsize:
                arr[j] = 0
                j = j + i
        i += 1
    return arr[i - 1]


@profile
def func_4():
    res = max(array, key=array.count)
    k = array.count(res)
    return f'Чаще всего встречается число {res}, ' \
           f'оно появилось в массиве {k} раз(а)'


@profile
def func_3():
    new_array = {}
    k = 0
    res = ""
    for el in array:
        if new_array.get(el):
            new_array[el] = int(new_array.get(el)) + 1
            if new_array.get(el) > k:
                k = new_array.get(el)
                res = el
        else:
            new_array[el] = 1
    del new_array
    return f'Чаще всего встречается число {res}, ' \
           f'оно появилось в массиве {k} раз(а)'


@profile
def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    del new_array
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

@profile
def my_func():
    a = [1] * (10**6)
    b = [2] * (2 * 10**7)
    del b
    return a

i = int(input('Введите порядковый номер искомого простого числа: '))
t1 = timeit.default_timer()
print("Simple", simple(i))
print("{} Seconds needed for Simple".format(timeit.default_timer() - t1))
t1 = timeit.default_timer()
print("resheto", resheto(i))
print("{} Seconds needed for resheto".format(timeit.default_timer() - t1))

array = [randint(0, 1000) for i in range(100000)]
t1 = timeit.default_timer()
print("func_2", func_2())
print("{} Seconds needed for func_2".format(timeit.default_timer() - t1))

t1 = timeit.default_timer()
print("func_3", func_3())
print("{} Seconds needed for func_3".format(timeit.default_timer() - t1))

t1 = timeit.default_timer()
print("func_4", func_4())
print("{} Seconds needed for func_4".format(timeit.default_timer() - t1))

t1 = timeit.default_timer()
my_func()
print("{} Seconds needed for func_4".format(timeit.default_timer() - t1))

# Выводы. Очень важно следить за использованием памяти в коде. Особенно когда речь идёт о массивах с числами высокой разрядности.
# Важно удалять неиспользуемые емкие элементы, которые не требуются в дальнейшем коде.
# также по возможности использовать например генераторы вместо хранения в массиве.
# Дополнительно стоит учитывать типы данных, например tuple более предпочтительный чем list.

"""Введите порядковый номер искомого простого числа: 100
Filename: C:/Users/HappyMan/PycharmProjects/python_algos_gb/Урок 6. Практическое задание/Lec6HMSD/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    35     16.1 MiB     16.1 MiB           1   @profile
    36                                         def simple(i):
    37                                             ""Без использования «Решета Эратосфена»""
    38     16.1 MiB      0.0 MiB           1       count = 1
    39     16.1 MiB      0.0 MiB           1       n = 2
    40     16.1 MiB      0.0 MiB         540       while count <= i:
    41     16.1 MiB      0.0 MiB         540           t = 1
    42     16.1 MiB      0.0 MiB         540           is_simple = True
    43     16.1 MiB      0.0 MiB       25724           while t <= n:
    44     16.1 MiB      0.0 MiB       25624               if n % t == 0 and t != 1 and t != n:
    45     16.1 MiB      0.0 MiB         440                   is_simple = False
    46     16.1 MiB      0.0 MiB         440                   break
    47     16.1 MiB      0.0 MiB       25184               t += 1
    48     16.1 MiB      0.0 MiB         540           if is_simple:
    49     16.1 MiB      0.0 MiB         100               if count == i:
    50     16.1 MiB      0.0 MiB           1                   break
    51     16.1 MiB      0.0 MiB          99               count += 1
    52     16.1 MiB      0.0 MiB         539           n += 1
    53     16.1 MiB      0.0 MiB           1       return n


Simple 541
2.2805850999999997 Seconds needed for Simple
Filename: C:/Users/HappyMan/PycharmProjects/python_algos_gb/Урок 6. Практическое задание/Lec6HMSD/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    56     16.2 MiB     16.2 MiB           1   @profile
    57                                         def resheto(n):
    58     16.2 MiB      0.0 MiB           1       if n > 10:
    59     16.2 MiB      0.0 MiB           1           koef = n // int(math.log10(n))
    60                                             else:
    61                                                 koef = n
    62     16.2 MiB      0.0 MiB           1       arrsize = n * koef
    63     16.3 MiB      0.1 MiB        5004       arr = list([i for i in range(arrsize + 1)])
    64     16.3 MiB      0.0 MiB           1       i = 2
    65     16.3 MiB      0.0 MiB           1       k = 0
    66     16.3 MiB      0.0 MiB         541       while (k < n) and (i <= arrsize):
    67     16.3 MiB      0.0 MiB         540           if arr[i] != 0:
    68     16.3 MiB      0.0 MiB         100               k += 1
    69     16.3 MiB      0.0 MiB         100               j = i + i
    70     16.3 MiB      0.0 MiB       10482               while j <= arrsize:
    71     16.3 MiB      0.0 MiB       10382                   arr[j] = 0
    72     16.3 MiB      0.0 MiB       10382                   j = j + i
    73     16.3 MiB      0.0 MiB         540           i += 1
    74     16.3 MiB      0.0 MiB           1       return arr[i - 1]


resheto 541
1.1252611999999997 Seconds needed for resheto
Filename: C:/Users/HappyMan/PycharmProjects/python_algos_gb/Урок 6. Практическое задание/Lec6HMSD/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   103     17.9 MiB     17.9 MiB           1   @profile
   104                                         def func_2():
   105     17.9 MiB      0.0 MiB           1       new_array = []
   106     18.4 MiB   -709.9 MiB      100001       for el in array:
   107     18.4 MiB   -709.9 MiB      100000           count2 = array.count(el)
   108     18.4 MiB   -709.4 MiB      100000           new_array.append(count2)
   109                                         
   110     18.4 MiB      0.0 MiB           1       max_2 = max(new_array)
   111     18.4 MiB      0.0 MiB           1       elem = array[new_array.index(max_2)]
   112     17.9 MiB     -0.5 MiB           1       del new_array
   113     17.9 MiB      0.0 MiB           1       return f'Чаще всего встречается число {elem}, ' \
   114                                                    f'оно появилось в массиве {max_2} раз(а)'


func_2 Чаще всего встречается число 352, оно появилось в массиве 129 раз(а)
199.0878575 Seconds needed for func_2
Filename: C:/Users/HappyMan/PycharmProjects/python_algos_gb/Урок 6. Практическое задание/Lec6HMSD/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    85     17.9 MiB     17.9 MiB           1   @profile
    86                                         def func_3():
    87     17.9 MiB      0.0 MiB           1       new_array = {}
    88     17.9 MiB      0.0 MiB           1       k = 0
    89     17.9 MiB      0.0 MiB           1       res = ""
    90     17.9 MiB -14284.5 MiB      100001       for el in array:
    91     17.9 MiB -14284.3 MiB      100000           if new_array.get(el):
    92     17.9 MiB -14238.4 MiB       98999               new_array[el] = int(new_array.get(el)) + 1
    93     17.9 MiB -14238.4 MiB       98999               if new_array.get(el) > k:
    94     17.9 MiB    -17.8 MiB         128                   k = new_array.get(el)
    95     17.9 MiB    -17.8 MiB         128                   res = el
    96                                                 else:
    97     17.9 MiB    -46.1 MiB        1001               new_array[el] = 1
    98     17.7 MiB     -0.1 MiB           1       del new_array
    99     17.7 MiB      0.0 MiB           1       return f'Чаще всего встречается число {res}, ' \
   100                                                    f'оно появилось в массиве {k} раз(а)'


func_3 Чаще всего встречается число 352, оно появилось в массиве 129 раз(а)
11.843756499999984 Seconds needed for func_3
Filename: C:/Users/HappyMan/PycharmProjects/python_algos_gb/Урок 6. Практическое задание/Lec6HMSD/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    77     17.7 MiB     17.7 MiB           1   @profile
    78                                         def func_4():
    79     17.7 MiB      0.0 MiB           1       res = max(array, key=array.count)
    80     17.7 MiB      0.0 MiB           1       k = array.count(res)
    81     17.7 MiB      0.0 MiB           1       return f'Чаще всего встречается число {res}, ' \
    82                                                    f'оно появилось в массиве {k} раз(а)'


func_4 Чаще всего встречается число 352, оно появилось в массиве 129 раз(а)
183.9741877 Seconds needed for func_4
Filename: C:/Users/HappyMan/PycharmProjects/python_algos_gb/Урок 6. Практическое задание/Lec6HMSD/task_1.py

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   116     17.7 MiB     17.7 MiB           1   @profile
   117                                         def my_func():
   118     21.5 MiB      3.8 MiB           1       a = [1] * (10**6)
   119     97.8 MiB     76.3 MiB           1       b = [2] * (2 * 10**7)
   120     21.5 MiB    -76.3 MiB           1       del b
   121     21.5 MiB      0.0 MiB           1       return a



Process finished with exit code 0
"""