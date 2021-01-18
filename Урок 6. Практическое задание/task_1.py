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

Ответ:
В первом примере сравниваются три функции для поиска простого числа.
Первая функция оптимизированна по памяти, т.к. не использует списка, но имеет
меньшую скорость работы в сравнении с двумя другими.

Во втором примере рассмотрены два разных алгоритма сортировки.
Сортировка слиянием работает быстрей, но из-за того, что функция рекурсивная,
требуется O(n) дополнителньной памяти, т.е. уход от рекурсии может дать дополнительную
экономию памяти.
"""
from memory_profiler import memory_usage
from heapq import merge
from random import randint
import math
import time


def wrapper(func):
    def wrapped(*args, **kwargs):
        t0 = time.perf_counter()
        m0 = memory_usage()
        name = func.__name__
        result = func(*args, **kwargs)
        print(f'Использование памяти {name}: {memory_usage()[0] - m0[0]}')
        print(f'Время работы {name}: {time.perf_counter() - t0}')
        return result
    return wrapped


# Первый пример
@wrapper
def get_prime_numbers(count):
    prime_numbers = 2
    next_number = 3

    while count - 1:
        for i in range(2, int(math.sqrt(next_number)) + 1):
            if next_number % i == 0:
                break
        else:
            prime_numbers = next_number
            count -= 1
        next_number += 1

    return prime_numbers


@wrapper
def eratosthenes_sieve1(num):
    n = 3
    primes = []
    s = list(range(n))
    s[0] = s[1] = 0
    sl = 0
    while 1:
        for i in s[sl+1:]:
            if s[i] != 0:
                if i not in primes:
                    primes.append(i)
                for j in range(i ** 2, n, (2 * i if i != 2 else i)):
                    s[j] = 0
        if num > len(primes):
            s = s + list(range(len(s), n*2+1))
            n = len(s)
        else:
            return primes[num-1]


@wrapper
def eratosthenes_sieve2(num):
    if num == 1:
        return 2
    n = int(num ** 1.302) + 1
    primes = []
    s = list(range(n))
    s[0] = s[1] = 0
    for i in s:
        if s[i] != 0:
            primes.append(i)
            for j in range(i ** 2, n, (2 * i if i != 2 else i)):
                s[j] = 0
    return primes[num-1]


# Второй пример
@wrapper
def selection_sort3(data):
    for i, e in enumerate(data):
        mn = min(range(i, len(data)), key=data.__getitem__)
        data[i], data[mn] = data[mn], e
    return data


@wrapper
def merge_sort(data):
    def merge_sort2(m):
        if len(m) <= 1:
            return m

        middle = len(m) // 2
        left = m[:middle]
        right = m[middle:]

        left = merge_sort2(left)
        right = merge_sort2(right)
        return list(merge(left, right))
    return merge_sort2(data)


if __name__ == '__main__':
    print(get_prime_numbers(1000), '\n')
    print(eratosthenes_sieve1(1000), '\n')
    print(eratosthenes_sieve2(1000), '\n')

    unsorted = [randint(1, 100) for _ in range(2000)]
    unsorted2 = unsorted.copy()
    selection_sort3(unsorted)
    merge_sort(unsorted2)

