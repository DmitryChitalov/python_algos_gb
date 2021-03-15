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


def era(n):
    sieve = set(range(2, n * 100))
    sieve_out = []
    count = 0
    while count != n:
        prime = min(sieve)
        sieve_out.append(prime)
        # print(prime, end="\t")
        sieve -= set(range(prime, n * 100 + 1, prime))
        count += 1
    return sieve_out[-1]


print(simple(10000))
print(era(10000))

i = 10
print('simple:' + str(i))
print(timeit('simple(i), i', globals=globals(), number=100))
print('era:' + str(i))
print(timeit('era(i), i', globals=globals(), number=100))

i = 100
print()
print('simple:' + str(i))
print(timeit('simple(i), i', globals=globals(), number=100))
print('era:' + str(i))
print(timeit('era(i), i', globals=globals(), number=100))

i = 10000
print()
print('simple:' + str(i))
print(timeit('simple(i), i', globals=globals(), number=1))
print('era:' + str(i))
print(timeit('era(i), i', globals=globals(), number=1))

"""
Простой алгоритм более эффективен для i 100
simple:10       0.0025308999999999887
era:10          0.017489900000000003

simple:100      0.2578995
era:100         0.7846922
 
simple:10000    60.54182
era:10000       51.237527400000005
simple:10000    57.4875186
era:10000       48.5958028

Алгоритм решета Эратосфена более эффективен для больших i (>1000)


"""
