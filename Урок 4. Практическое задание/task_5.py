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

def eratosfen(number, l=100000):
    a = [el for el in range(l+1)]
    a[1] = 0
    i = 2
    while i <= l:
        if a[i] != 0:
            j = i + i
            while j <= l:
                a[j] = 0
                j += i
        i += 1
    # a = set(a)
    # a.remove(0)
    return [el for el in a if el!=0][number-1]

i = int(input('Введите порядковый номер искомого простого числа: '))
print(f'Искомое число равно {simple(i)}')
print(f'Затраты врени составили: '
      f'{timeit("simple(i)", setup="from __main__ import simple, i", number=10)}')
print(f'Искомое число равно {eratosfen(i)}')
print(f'Затраты врени составили: '
      f'{timeit("eratosfen(i)", setup="from __main__ import eratosfen, i", number=10)}')

# При работе алгоритма Эратосфена, после 300 числе эратосфен уже становистя на много выгоднее по времени