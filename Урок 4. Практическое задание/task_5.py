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
from math import log

def simple(i):
    """Без использования «Решета Эратосфена»"""
    # Сложность (n*log(n))^2
    count = 1
    n = 2
    while count <= i:                              # n*log(n)
        t = 1
        is_simple = True
        while t <= n:                              # n*log(n)
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


# Решето Эратосфена
# n*log(n)

def erat(needed_simple_number):
    if needed_simple_number <= 0:
        return 0

    max_number = int(needed_simple_number * (log(needed_simple_number) + 2))

    a = [x for x in range(max_number + 1)]      # n
    a[0] = 0
    a[1] = 0

    found_simple_numbers = 0
    i = 2
    while i <= max_number:                      # n
        if a[i] != 0:
            found_simple_numbers += 1

            if found_simple_numbers >= needed_simple_number:
                break

            j = i + i
            while j <= max_number:              # log(n)
                a[j] = 0
                j = j + i
        i += 1

    return i



Num = 100

i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
print(erat(i))

print("Time no erat - ", timeit('simple(i)', setup='from __main__ import simple, i', number=Num))
print("Time erat    - ", timeit('erat(i)',   setup='from __main__ import erat, i',   number=Num))


# Решето Эратосфена эффективнее как по сложности (более низкая),
# так и эмперически (меньшее время исполнения)

