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
"""
Оба алгоритма раьотабт примерно одинаково для 10 значений
[22.055715791999997, 22.020609942, 22.068423114999995]
[23.305740827999998, 23.294203812999996, 23.819416308]
Для 100 значений - работа  обоих алгоритмов не удовлетворительна, зависают на долгие минуты
 """

from timeit import repeat, default_timer



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



def simple_1(n):
    a = list(range(10 * n + 1))
    a[1] = 0
    i = 2
    while i <= 2 * n:
        if a[i] != 0:
            j = i + i
            while j <= n * 10:
                a[j] = 0
                j = j + i
        i += 1

    a = set(a)
    a.remove(0)
    return list(a)[n+1]



setup = 'from __main__ import simple, simple_1'

print(simple(5))
print(simple_1(5))

# print(repeat('simple(100)', setup, default_timer, 3))
# print(repeat('simple_1(100)', setup, default_timer, 3))
# print(timeit('simple_1(10)', setup))
"""21.884270959000002
13.300076817999997"""
