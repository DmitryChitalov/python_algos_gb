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
import timeit


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


def sieve_of_Eratosthenes(k):
    n = 10000
    a = [v for v in range(n)]
    a[1] = 0
    i = 2
    while i < n:
        if a[i] != 0:
            j = i + i
            while j < n:
                a[j] = 0
                j = j + i
        i += 1
    a = [v for v in a if v != 0]
    return a[k-1]


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
print(sieve_of_Eratosthenes(i))

print(timeit.timeit("simple(i)", setup="from __main__ import simple, i", number=1000))
print(timeit.timeit("sieve_of_Eratosthenes(i)", setup="from __main__ import sieve_of_Eratosthenes, i", number=1000))

"""
Результат для поиска 10-го простого числа 1000 раз:
0.022509315000000196
3.355318378

Результат для поиска 100-го простого числа 1000 раз:
2.0681758930000003
3.3571097580000002

Результат для поиска 1000-го простого числа 1000 раз:
343.00991880
3.10003229098

Для поиска большого по индексу простого числа быстрее работает функция реализ через решето,
на малых позициях эффективно работает и по нативному алгоритму 
"""