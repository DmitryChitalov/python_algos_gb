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


def eratosfen(n):
    a = [i for i in range(10000)]
    a[1] = 0
    for i in a:
        if i > 1:
            for j in range(i + i, len(a), i):
                a[j] = 0
    b = [i for i in a if i != 0]
    return b[n - 1]


print(simple(10))
print(eratosfen(10))
print(simple(100))
print(eratosfen(100))
print(simple(1000))
print(eratosfen(1000))

print(
    f'Перебор до 10 : {timeit("simple(10)", globals=globals(),number=10)} сек.'
)
print(
    f'Решето Эратосфена 10 : {timeit("eratosfen(10)", globals=globals(),number=10)} сек.'
)
print(
    f'Перебор до 100 : {timeit("simple(100)", globals=globals(),number=10)} сек.'
)
print(
    f'Решето Эратосфена 100 : {timeit("eratosfen(100)", globals=globals(),number=10)} сек.'
)
print(
    f'Перебор до 1000 : {timeit("simple(1000)", globals=globals(),number=10)} сек.'
)
print(
    f'Решето Эратосфена 1000 : {timeit("eratosfen(1000)", globals=globals(),number=10)} сек.'
)

# На малых значениях пребор работает быстрее,
# но при больших значениях алгоритм Эратосфена выполняется значительно быстрее.
