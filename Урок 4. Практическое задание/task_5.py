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
import cProfile

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

def resheto_erastofena(k):
    a = []
    n = 10000
    for i in range(n + 1):
        a.append(i)
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    res = list(filter(lambda x: x > 0, a))
    return res[k - 1]


i = int(input('Введите порядковый номер искомого простого числа: '))
print(timeit("simple(i)", setup="from __main__ import simple, i", number=100))
print(timeit("resheto_erastofena(i)", setup="from __main__ import resheto_erastofena, i", number=100))


cProfile.run(f'simple({i})')
cProfile.run(f'resheto_erastofena({i})')

"""
Введите порядковый номер искомого простого числа: 10
0.003768100000000274
0.6938287000000001

Введите порядковый номер искомого простого числа: 100
0.5088965999999999
0.7411186000000001

Введите порядковый номер искомого простого числа: 500
13.5819113
0.6090075999999982

Введите порядковый номер искомого простого числа: 1000
47.1502317
0.5697839999999985


алгоритм "Решето эратосфена" значительно выигрывает на больших значениях, т.к. скорость его работы O(N logN),
а скорость работы простого поиска O(N^2)
"""