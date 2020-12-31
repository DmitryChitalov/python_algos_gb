"""
Задание 5.*

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

1 Попробуйте решить эту же задачу,
применив алгоритм "Решето эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
2 Сравните алгоритмы по времени на разных порядковых номерах чисел:
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


def eratosfen(i):
    n = 2
    border = 10000
    sieve = [el for el in range(border)]
    sieve[1] = 0
    while n < border:
        if sieve[n] != 0:
            j = n + n
            while j < border:
                sieve[j] = 0
                j = j + n
        n += 1
    sieve_s = [el for el in sieve if el != 0]
    return sieve_s[i-1]

try:
    i = int(input('Введите порядковый номер искомого простого числа до 1229: \n'))
    print(simple(i))
    print(eratosfen(i))
except IndexError:
    print('Для поиска числа порядковый номер которого больше 1229 требуется увеличить значение переменной border')

print('simple()', timeit('simple(i)', setup='from __main__ import simple, i',  number=100))

print('eratosfen()', timeit('eratosfen(i)', setup='from __main__ import eratosfen, i', number=100))

"""
для i = 10:
simple() 0.0016217999999996735
eratosfen() 0.32125729999999963
для i = 100
simple() 0.19707430000000015
eratosfen() 0.3329097000000001
для i = 1000
simple() 30.9692631
eratosfen() 0.3287697000000023
Как видим с чем больше i, тем больше времни требуется функции simple для нахождения простого числа.
Для функции eratosfen требуется одинаковое время вне зависимости от значения i.
Это связано с тем что simple имеет сложность O(n**2). Сложность функции eratosfen логарифмическая,
время выполнения этой функции зависит от величины массива sieve.
"""