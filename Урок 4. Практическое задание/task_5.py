"""
Задание 5.**

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснвование рез-ам
"""

import timeit as t


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


def erato(n):
    i = 2
    last_elem = n * 10
    all_num = [z for z in range(last_elem)]
    all_num[1] = 0
    while i < last_elem:
        if all_num[i] != 0:
            check = i * 2
            while check < last_elem:
                all_num[check] = 0
                check = check + i
        i = i + 1
    return [x for x in all_num if x != 0][n - 1]


i1 = 10
i2 = 100
i3 = 1000

print()
print(f'{i1}')
print("Вариант без решета Эратосфена:")
print(t.timeit("simple(i1)", globals=globals(), number=50))
print("Вариант с решетом Эратосфена:")
print(t.timeit("erato(i1)", globals=globals(), number=50))
print()
print(f'{i2}')
print("Вариант без решета Эратосфена:")
print(t.timeit("simple(i2)", globals=globals(), number=50))
print("Вариант с решетом Эратосфена:")
print(t.timeit("erato(i2)", globals=globals(), number=50))
print()
print(f'{i3}')
print("Вариант без решета Эратосфена:")
print(t.timeit("simple(i3)", globals=globals(), number=50))
print("Вариант с решетом Эратосфена:")
print(t.timeit("erato(i3)", globals=globals(), number=50))

"""
Сложность первой функции O(n^2)
Сложность второй функции O(n log n)
Второй вариант более оптимален для поиска натурального числа
"""
