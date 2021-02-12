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
Введите порядковый номер искомого простого числа: 200
1223
1223
0.011809799999999981
0.012393199999999993
Введите порядковый номер искомого простого числа: 1000
7919
7919
0.37481810000000015
0.38043159999999965
Введите порядковый номер искомого простого числа: 5000
48611
48611
12.101429399999997
10.5097856
Введите порядковый номер искомого простого числа: 10000
104729
104729
52.797262399999994
43.80760430000001
Алгоритм на основе решета сравним по производительности на небольших значениях, и начинает выигрывать 
 на больших
Сложность алгоритма оценивается как O(n * log(n)) 
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


def not_so_simple(in_n):
    scr_arr = []
    prime_ind = 1
    prime = 2
    for i in range(in_n * in_n + 1):
        scr_arr.append(i)
        scr_arr[i] = 0
    i = 2
    while prime_ind <= (in_n):
        if scr_arr[i] == 0:
            prime = i
            if prime_ind == in_n:
                break
            prime_ind = prime_ind + 1
            j = i * i
            while j <= in_n * in_n:
                if scr_arr[j] == 0:
                    scr_arr[j] = 1
                j = j + i
        i += 1
    return prime


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
print(not_so_simple(i))
print(
    timeit(
        "simple(i)",
        setup='from __main__ import simple, i',
        number=1))

print(
    timeit(
        "not_so_simple(i)",
        setup='from __main__ import not_so_simple, i',
        number=1))
