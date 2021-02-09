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


def resheto(n):
    i = 2
    nums = []
    end_elem = n * 10
    for item in range(n * 10):
        nums.append(item)

    nums[1] = 0
    while i < end_elem:
        if nums[i] != 0:
            j = i + i
            while j < end_elem:
                nums[j] = 0
                j = j + i
        i = i + 1

    res = []
    for item in nums:
        if item != 0:
            res.append(item)

    return res[n - 1]


i = 10
print(timeit("simple(i)", setup="from __main__ import simple, i", number=100))
print(
    timeit("resheto(i)", setup="from __main__ import resheto, i", number=100))
print()

i = 100
print(timeit("simple(i)", setup="from __main__ import simple, i", number=100))
print(
    timeit("resheto(i)", setup="from __main__ import resheto, i", number=100))
print()

i = 1000
print(timeit("simple(i)", setup="from __main__ import simple, i", number=100))
print(
    timeit("resheto(i)", setup="from __main__ import resheto, i", number=100))
print()

#
#
# 0.004391900000000004
# 0.007058800000000032
#
# 1.0913791000000002
# 0.13428360000000006
#
# 92.3649366
# 0.9123883999999975
#
# второй алгоритм эффективнее на больших числах
#
