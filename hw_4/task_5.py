"""
Задание 5.**

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснвование рез-ам
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


def not_simple(n):
    len_arr = 100
    if n > 9592:
        len_arr = 1000000
    elif n > 1229:
        len_arr = 100000
    elif n > 168:
        len_arr = 10000
    elif n > 25:
        len_arr = 1000

    a = []
    for i in range(len_arr + 1):
        a.append(i)

    a[1] = 0
    i = 2

    while i <= len_arr:
        if a[i] != 0:
            j = i + i
            while j <= len_arr:
                a[j] = 0
                j = j + i
        i += 1

    # a = [el for el in a if el != 0]
    a = set(a)
    a.remove(0)
    a = sorted(list(a))
    return a[n-1]


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
print(not_simple(i))
print(timeit("simple(i)", globals=globals(), number=100))
print(timeit("not_simple(i)", globals=globals(), number=100))

'''
Сложность без использования «Решета Эратосфена» = O(n^2)
Сложность c использованием «Решета Эратосфена» = O(n log(log n))
На малых значениях решение без использования быстрее, но с увеличением n
оба решения выравниваются, и далее уже решение с использованием «Решета Эратосфена»
выигрывает по времени
При n = 10, number=100
    simple     = 0.0019160000000000288
    not_simple = 0.0031423000000003753
При n = 100, number=100
    simple     = 0.23810299999999973
    not_simple = 0.038114199999999876
При n = 1000, number=100
    simple     = 41.097867699999995
    not_simple = 0.41354229999999603
'''

