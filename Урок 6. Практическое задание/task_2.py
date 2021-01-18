"""
Задание 1.
Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-5 ваших разных скриптов! Сделать их разные реализации.
Можно взять задачи с курса Основ или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ) БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
from timeit import default_timer
from memory_profiler import memory_usage


def check_memory(func):
    def memory_time(*args):
        memory_start = memory_usage()
        func(args[0])
        memory_end = memory_usage()

        print(f'memory_start - {memory_start}, memory_end - {memory_end}, diff = {memory_end[0] - memory_start[0]}')
    return memory_time


@check_memory
def simple(i):
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
    print(n)


@check_memory
def sieve_of_Eratosthenes(k):
    n = 10000
    a = [v for v in range(n)]
    a[1] = 0
    i = 2
    while i < n:
        if a[i] != 0:
            j = i + i
            while j < n:
                a[j] = 0
                j = j + i
        i += 1
    a = [v for v in a if v != 0]
    print(a[k-1])


i = 1000
time_start = default_timer()
simple(i)
time_end = default_timer()
print(f'diff = {time_end - time_start}')

time_start = default_timer()
sieve_of_Eratosthenes(i)
time_end = default_timer()
print(f'diff = {time_end - time_start}')

"""
memory_start - [12.765625], memory_end - [12.76953125], diff = 0.00390625
diff = 0.581360161

memory_start - [12.7890625], memory_end - [12.99609375], diff = 0.20703125
diff = 0.2124845860000001

Решето Эратосфена является быстрым решением по времени, но занимает немного памяти, хотя оно не превышает нормы.
Оба решения являются эффективными по использованию памяти
"""