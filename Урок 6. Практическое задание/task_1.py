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
import platform
import random
import time
from functools import reduce
import memory_profiler


def time_memory(func):
    def wrapper(*args):
        t1 = time.process_time()
        m1 = memory_profiler.memory_usage()
        func(*args)
        t2 = time.process_time()
        m2 = memory_profiler.memory_usage()
        print(f"Выполнение заняло {t2 - t1} сек и {m2[0] - m1[0]} Mib")
    return wrapper


def multiply(num1, num2):
    return num1 * num2


@time_memory
def result_mult():
    numbers = [i for i in range(10000000) if i % 2 == 0]
    result = reduce(multiply, numbers)
    return result


@time_memory
def result_mult2():
    numbers = (i for i in range(10000000) if i % 2 == 0)
    result = reduce(multiply, numbers)
    return result


print(platform.platform())
result_mult()
result_mult2()

"""
Python 3.8 платформа macOS-10.16-x86_64-i386-64bit
В первой функции с помощью генераторного выражения создается список, что создает затраты памяти, но ускоряет работу.
Во второй функции генераторное выражение заменяем на генератор, список не создается, вычисления происходят по шаблону 
генератора. Это дает увеличение времени расченов, но снижает затраты памяти.
Выполнение заняло 1.1545409999999998 сек и 4.16015625 Mib
Выполнение заняло 1.199674 сек и 0.0 Mib  
"""


@memory_profiler.profile
@time_memory
def gen_password(synbol):
    my_lst = []
    for i in range(100):
        words = ''.join(random.choice(synbol) for _ in range(7))
        my_lst.append(words)
    return my_lst


@memory_profiler.profile
@time_memory
def gen_password2(synbol):
    my_lst = []
    for i in range(10000):
        words = ''.join(random.choice(synbol) for _ in range(70))
        my_lst.append(words)
    return my_lst


word = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

gen_password(word)
gen_password2(word)


"""
Функция генератора паролей, работает хорошо, просадок по памяти нет. При увеличении range значительно вырастет скорость 
работы, но память сильно не нагрузится.
Выполнение заняло 0.012225000000000374 сек и 0.0 Mib

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    31     17.2 MiB     17.2 MiB           1       def wrapper(*args):
    32     17.2 MiB      0.0 MiB           1           t1 = time.process_time()
    33     17.2 MiB      0.0 MiB           1           m1 = memory_profiler.memory_usage()
    34     17.2 MiB      0.0 MiB           1           func(*args)
    35     17.2 MiB      0.0 MiB           1           t2 = time.process_time()
    36     17.2 MiB      0.0 MiB           1           m2 = memory_profiler.memory_usage()
    37     17.2 MiB      0.0 MiB           1           print(f"Выполнение заняло {t2 - t1} сек и {m2[0] - m1[0]} Mib")
    
Выполнение заняло 7.604044999999999 сек и -0.078125 Mib

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    31     18.0 MiB     18.0 MiB           1       def wrapper(*args):
    32     18.0 MiB      0.0 MiB           1           t1 = time.process_time()
    33     18.0 MiB      0.0 MiB           1           m1 = memory_profiler.memory_usage()
    34     17.9 MiB     -0.1 MiB           1           func(*args)
    35     17.9 MiB      0.0 MiB           1           t2 = time.process_time()
    36     17.9 MiB      0.0 MiB           1           m2 = memory_profiler.memory_usage()
    37     17.9 MiB      0.0 MiB           1           print(f"Выполнение заняло {t2 - t1} сек и {m2[0] - m1[0]} Mib")
"""