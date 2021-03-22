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
import math


def simple(i):  # O(N^2)
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
    """C использованием «Решета Эратосфена»"""
    # С примерным расчётом границы массива. На i = 1 000 000 алгоритм работает.
    # поэтапная реализация оказалась для меня пока что слишком сложной, я постараюсь разобраться в ней в будущем
    number = round(1.2 * i * math.log(i, math.e)) + 2
    result = list(range(number + 1))
    result[1] = 0
    idx = 2
    while idx <= number:
        if result[idx]:
            new_idx = 2 * idx
            while new_idx <= number:
                result[new_idx] = 0
                new_idx += idx
        idx += 1
    result = set(result)
    result.remove(0)
    result = sorted(list(result))
    return result[i - 1]


def simple_upgrade(number):
    """Улучшенный наивный алгоритм"""
    num = 2
    result = [2]
    i = 1
    while i < number:
        if not num % 2:
            num += 1
            continue
        flag = True
        for elem in result:
            if not num % elem:
                flag = False
                break
        if flag:
            result.append(num)
            i += 1
        num += 1
    return result[-1]


test = (10, 100, 1000)

print('\nФункция simple:')
for item in test:
    print(f'simple: {simple(item)}')
    print(timeit('simple(item)', globals=globals(), number=100))

    # simple: 29
    # 0.0012116000000000002
    # simple: 541
    # 0.1420899
    # simple: 7919
    # 23.3926704

print('\nФункция simple_upgrade:')
for item in test:
    print(f'simple_upgrade: {simple_upgrade(item)}')
    print(timeit('simple_upgrade(item)', globals=globals(), number=100))

    # simple_upgrade: 29
    # 0.0003562999999999761
    # simple_upgrade: 541
    # 0.015976200000000773
    # simple_upgrade: 7919
    # 1.484258999999998

print('\nФункция sieve:')
for item in test:
    print(f'sieve: {sieve(item)}')
    print(timeit('sieve(item)', globals=globals(), number=100))

    # sieve: 29
    # 0.000509699999998503
    # sieve: 541
    # 0.01025849999999906
    # sieve: 7919
    # 0.17504950000000008


# Замеры показывают, что алгоритм с решетом Эратосфена значительно эффективнее при большом i.
# Сложность наивного и улучшенного наивного алгоритмов близка к квадратичной, но скорость работы улучшенного
# наивного алгоритма растёт гораздо медленнее и при малом значении i он будет быстрее, чем алгоритм с решетом,
# однако уже при i = 100 решето становится эффективнее.
# Сложность алгоритма решето Эратосфена O(n log(log n))
