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


def erat(i_ind):
    a = []
    n = i_ind
    n = n * 10
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
    res = []
    for rec in a:
        if rec != 0:
            res.append(rec)
    return res[i_ind - 1]


print('simple(10)', simple(10))
print('erat(10)', erat(10))
print('simple(100)', simple(100))
print('erat(100)', erat(100))
print('simple(1000)', simple(1000))
print('erat(1000)', erat(1000))

print('simple(10)', timeit('simple(10)', setup='from __main__ import simple', number=100))
print('simple(100)', timeit('simple(100)', setup='from __main__ import simple', number=100))
print('simple(1000)', timeit('simple(1000)', setup='from __main__ import simple', number=100))

print('erat(10)', timeit('erat(10)', setup='from __main__ import erat', number=100))
print('erat(100)', timeit('erat(100)', setup='from __main__ import erat', number=100))
print('erat(1000)', timeit('erat(1000)', setup='from __main__ import erat', number=100))

'''Как и следовало ожидать на малых диапазонах первый алгоритм быстрее.(подобное часто можно встретить при обсуждении
    ефективности алгоритмов. Когда не самых эфективынх алгоритм на малых диапазонах работает эфективнее.
    Но как стоит диапазону перевалить уже за пару десятков как "решето" уходит в перед
    Алгоритм перебор имеет сложность O(n**2)
    Решето имеет сложность O(n*log(n)),    
    Вывод: алгоритм "Решето эратосфена" намного эффективнее, чем
    алгоритм перебор делителей. - но только если мы говорим о диапазонах свыша пару десятков
'''
