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


def simple_num(s):
    n = s * 100
    simple_list = [el for el in range(n+1)]
    simple_list[1] = 0
    i = 2
    while i <= n:
        if simple_list[i] != 0:
            m = i * 2
            while m <= n:
                simple_list[m] = 0
                m += i
        i += 1
    simple_list = sorted(list(set(simple_list)))
    simple_list.remove(0)
    return simple_list[s-1]


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
print(timeit('simple(i)', 'from __main__ import simple, i', number=100))
print(simple_num(i))
print(timeit('simple_num(i)', 'from __main__ import simple_num, i', number=100))


"""
Введите порядковый номер искомого простого числа: 10
- перебор 0.0025850000000000595
- решето  0.05855409999999983

Введите порядковый номер искомого простого числа: 100
- перебор 0.3271069000000002
- решето  0.6876226000000001

Введите порядковый номер искомого простого числа: 1000
- перебор 71.0092968
- решето  8.222473499999992


Алгоритм решета Эратосфена более эфективен для поиска простого числа с большим порядковым номером.
"""
