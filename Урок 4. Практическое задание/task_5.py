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


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))

def sieve_of_eratosthenes(i):
    n = 2
    l = 10000
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < 1:
        if sieve[n] != 0:
            m = n*2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1
    return [p for p in sieve if p != 0][i-1]

print(
    timeit(
        "simple(i)",
        setup='from __main__ import simple, i',
        number=100))
print(
    timeit(
        "sieve_of_eratosthenes(i)",
        setup='from __main__ import sieve_of_eratosthenes, i',
        number=100))

"""
Результаты замеров 10-го
0.0022914000000002765 - simple
0.10388129999999984 - sieve_of_eratosthenes
Результаты замеров 100-го
0.2546469 - simple
0.0959190999999997 - sieve_of_eratosthenes
Результаты замеров 1000-го
47.6955993 - simple
0.0945718000000042 - sieve_of_eratosthenes

Таким образом, решето Эратосфена имеет преимущество при обработке больших запросов,
но сильно уступает при меньших
"""