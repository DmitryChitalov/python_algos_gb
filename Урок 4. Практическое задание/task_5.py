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

import timeit
import collections

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


# ------------------------------------------------------------


def eratosphen_enumerate(n: int):
    """ Generate an infinite sequence of prime numbers.
        """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def eratosphen(n: int):
    current_index = 1
    for current_value in eratosphen_enumerate(n):
        if current_index == n:
            return current_value
        current_index += 1


def print_test(n: int):
    print(timeit.timeit(f"simple({n})", globals=globals(), number=20))
    print(timeit.timeit(f"eratosphen({n})", globals=globals(), number=20))


print_test(10)
print_test(100)
print_test(1000)
print(simple(30))
print(eratosphen(30))

"""
simple 20 повторов n=10:      0.0005464999999999984
эратосфен 20 повторов n=10:   0.0003118999999999969
simple 20 повторов n=100:     0.10364699999999999
эратосфен 20 повторов n=100:  0.010697200000000018
simple 20 повторов n=1000:    12.3614253
эратосфен 20 повторов n=1000: 0.14775539999999943

Алгоритм Эратосфена намного более эффективен для случая больших простых чисел
# simple - O(n^2)
# eratosphen - O (n log (log n))
"""
