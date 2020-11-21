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


def solutions_1(i):
    lst = [2, 3]
    count = 4
    while len(lst) < i:
        for n in lst:
            if count % n == 0:
                break
        else:
            lst.append(count)
        count += 1
    return lst[-1]


def solutions_2(i):
    lst = [2, 3]
    count = 5

    while len(lst) < i:
        if all(map(lambda x: count % x, lst)):
            lst.append(count)
        count += 2
    return count - 2


def solutions_3(i):
    lst = [2, 3]
    count = 5

    while len(lst) < i:
        if all(map(lambda x: count % x, filter(lambda x: x * x <= count, lst))):
            lst.append(count)
        count += 2
    return count - 2


i = 1000

print('simple:')
print(timeit("simple(100)", setup='from __main__ import simple', number=10))
print('solutions_1:')
print(timeit("solutions_1(100)", setup='from __main__ import solutions_1', number=10))
print('solutions_2:')
print(timeit("solutions_2(100)", setup='from __main__ import solutions_2', number=10))
print('solutions_3:')
print(timeit("solutions_3(100)", setup='from __main__ import solutions_3', number=10))

"""
Эротосфен в дощечке дырки делал в местах состовных чисел, есть алгоритм нахождения до задонного числа.
Придумать как реализовать это, к нашей задаче, нахождение i-го посчету простого числа, у меня не вышло.
Смог ускорить ваше решение:
- solutions_1, сам написал, получилось самым быстрым (сам не ожидал :-) ),
- solutions_2 и _3 подсмотренные частично в интернете, они получились по медленне, но все равно быстрее.
"""


