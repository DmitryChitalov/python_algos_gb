"""
Задание 5.*

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма
"""

# Результаты работы алгоритмов
#
# -----------------Наивный поиск------------------------
# 0.0005526999999999962
# 0.0675078
# 13.6316988
# -----------------Решето Эратосфена------------------------
# 0.0003024000000007021
# 0.005069100000000049
# 0.0871265999999995


from math import log
from timeit import timeit


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


def _sift(sieve):
    counter = 0
    end = sieve[-1]
    for num in sieve:
        if num < 2:
            continue

        counter += 1

        composite = num * 2
        while composite <= end:
            sieve[composite] = 0
            composite += num

    return counter


def prime_sieve(n):
    if n == 1:
        return 2

    # Оцениваем примерное количество простых чисел
    start, end = 0, int(n * (log(n) + log(log(n)))) + 1
    sieve = []
    prime_counter = 0

    while prime_counter < n:
        # Формируем "сито"
        for num in range(start, end):
            sieve.append(num)

        # Просеиавем. Если прощитались с размером решета - добавляем еще 10 ячеек,
        # пока не получим нужный порядок.
        start, end, prime_counter = end, end + 10, _sift(sieve)

    return [i for i in sieve if i > 1][n - 1]


if __name__ == '__main__':
    # i = int(input('Введите порядковый номер искомого простого числа: '))
    # print(simple(i))
    # print(prime_sieve(i))

    num_10 = 10
    num_100 = 100
    num_1000 = 1000

    rep = 10

    print('-----------------Наивный поиск------------------------')
    print(
        timeit(
            "simple(num_10)",
            setup='from __main__ import simple, num_10',
            number=rep))
    print(
        timeit(
            "simple(num_100)",
            setup='from __main__ import simple, num_100',
            number=rep))
    print(
        timeit(
            "simple(num_1000)",
            setup='from __main__ import simple, num_1000',
            number=rep))

    print('-----------------Решето Эратосфена------------------------')
    print(
        timeit(
            "prime_sieve(num_10)",
            setup='from __main__ import prime_sieve, _sift, num_10',
            number=rep))
    print(
        timeit(
            "prime_sieve(num_100)",
            setup='from __main__ import prime_sieve, _sift, num_100',
            number=rep))
    print(
        timeit(
            "prime_sieve(num_1000)",
            setup='from __main__ import prime_sieve, _sift, num_1000',
            number=rep))