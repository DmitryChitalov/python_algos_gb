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

def sieve(i):
    simple = [2, 3]
    n = 4
    while i > len(simple):
        if n & 1 and n % 3 != 0:
            for num in simple:
                if n % num == 0 and n != num:
                    break
            else:
                simple.append(n)
        n += 1
    return simple[-1]

# i = int(input('Введите порядковый номер искомого простого числа: '))
# print(simple(i))
# print(sieve(i))

stmts = ('simple', 'sieve')
nums = (10, 100)
for stmt in stmts:
    for num in nums:
        print(f'Алгоритм {stmt} для n={num}:')
        print(timeit(f"{stmt}({num})",
                     setup=f'from __main__ import {stmt}',
                        number=10000))

"""
Алгоритм simple для n=10:
0.22714343600091524
Алгоритм simple для n=100:
24.11967660099981
Алгоритм sieve для n=10:
0.07456370900035836
Алгоритм sieve для n=100:
3.6103270380008325

Алгоритм "Решето Эратосфена" показывает производительность тем лучше,
чем больше запрошенный индекс числа, относительно наивного перебора.
Оба алгоритма имеют квадратичную сложность, но при использовании
"Решета" кол-во итераций циклов растёт значительно медленнее, чем в
наивном алгоритме.
"""