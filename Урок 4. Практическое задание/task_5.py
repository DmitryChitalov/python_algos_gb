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


def strainer(i):
    a = [True] * i**2
    for n in range(2, int(i**2)):
        for j in range(n * 2, i**2, n):
            a[j] = False
    b = [n for n in range(2, i**2) if a[n]]
    return b[i-1]


i = int(input('Введите порядковый номер искомого простого числа: '))

print(f'Через простой алгоритм: {simple(i)}, через решето: {strainer(i)}')
print('10:')
print(timeit('simple(i)', setup='from __main__ import simple, i', number=10))
print(timeit('strainer(i)', setup='from __main__ import strainer, i',  number=10))
print('100:')
print(timeit('simple(i)', setup='from __main__ import simple, i', number=100))
print(timeit('strainer(i)', setup='from __main__ import strainer, i',  number=100))
print('1000:')
print(timeit('simple(i)', setup='from __main__ import simple, i', number=100))
print(timeit('strainer(i)', setup='from __main__ import strainer, i',  number=100))

""" Сложность простого алгоритма О(n^2), сложность решета O(n^2 + n), поэтому решето дольше.
Обычное решето выполняет поиск всех простых чисел до указанного, а задача стоит найти порядковое число.
Для этого требуется брать набор чисел с большим запасом, что бы нужное число 100% вошло в массив рассматриваемых чисел.
Из-за этого увеличивается кол-во итераций, в связи с чем увеличивается и время выполнения кода (практически в 2 раза) """