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


def er_simple(i):
    a = [el for el in range(10000)]
    a[1] = 0
    f = 2
    while f <= len(a) - 1:
        if a[f] != 0:
            j = f + f
            while j <= len(a) - 1:
                a[j] = 0
                j = j + f
        f += 1
    a = sorted(set(a))
    a.remove(0)
    return a[i - 1]


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
print(er_simple(i))

# При работе с timeit передавал параметры в функции напрямую, на данный момент 10 порядковый номер.
print(
    timeit(
        'simple(10)',
        setup='from __main__ import simple',
        number=100
    )
)

print(
    timeit(
        'er_simple(10)',
        setup='from __main__ import er_simple',
        number=100
    )
)

'''
Проведенные замеры показали, что небольших значениях передаваемых порядковых номеров (10, 100) быстрее выполняется
наивный алгоритм. Однако все меняется при передаче крупных значений порядковых номеров (1000), и быстрее ведет себя
алгоритм "Решето Эратосфена". 
'''