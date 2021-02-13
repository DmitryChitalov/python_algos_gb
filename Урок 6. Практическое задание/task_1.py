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
from math import log
from platform import architecture
from sys import version

print(f'Разрядность моей OS был 32 bit, а этой OS: {architecture()}')
print(f'Версия Python у меня - 3.8.5, а тут - {version}')


@profile(precision=4)
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


@profile(precision=4)
def sieve_eratosfen(nn):
    """С использованием «Решета Эратосфена»"""
    n = round(nn * log(nn)) * 2
    sieve = [True] * nn * nn
    k = 0
    for i in range(2, n):
        if sieve[i]:
            k += 1
            if k == nn:
                return i
            j = i * 2
            while j < n:
                sieve[j] = False
                j += i


i = int(input('Введите порядковый номер искомого простого числа: '))
print('Без использования «Решета Эратосфена»:')
print(simple(i))
print('C использованием «Решета Эратосфена»:')
print(sieve_eratosfen(i))

"""
Решение с использованием решета Эратосфена имеет меньшую сложность, 
чем наивный перебор, но требует больше памяти:

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    41  15.7266 MiB  15.7266 MiB           1   @profile(precision=4)
    42                                         def sieve_eratosfen(nn):
    43                                             ""С использованием «Решета Эратосфена»""
    44  15.7266 MiB   0.0000 MiB           1       n = round(nn * log(nn)) * 2
    45  15.8125 MiB   0.0859 MiB           1       sieve = [True] * nn * nn
    46  15.8125 MiB   0.0000 MiB           1       k = 0
    47  15.8125 MiB   0.0000 MiB         862       for i in range(2, n):
    48  15.8125 MiB   0.0000 MiB         862           if sieve[i]:
    49  15.8125 MiB   0.0000 MiB         150               k += 1
    50  15.8125 MiB   0.0000 MiB         150               if k == nn:
    51  15.8125 MiB   0.0000 MiB           1                   return i
    52  15.8125 MiB   0.0000 MiB         149               j = i * 2
    53  15.8125 MiB   0.0000 MiB        3196               while j < n:
    54  15.8125 MiB   0.0000 MiB        3047                   sieve[j] = False
    55  15.8125 MiB   0.0000 MiB        3047                   j += i
"""
