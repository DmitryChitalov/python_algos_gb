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

Ответ: Эффективность второго алгоритма будет тем выше, чем большее по порядку число мы попытаемся найти.
Третья функция более верная относительно задания (не имеет верхнего предела для решета), но не оптимизированна.
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


def eratosthenes_sieve(num):
    n = 10000
    primes = []
    s = list(range(n))
    s[0] = s[1] = 0
    for i in s:
        if s[i] != 0:
            primes.append(i)
            for j in range(i ** 2, n, (2 * i if i != 2 else i)):
                s[j] = 0
    return primes[num-1]


# Очень ресурсозатратная реализация реализация без верхнего предела, но результат времени интересный получается
def func(num):
    n = 3
    primes = []
    s = list(range(n))
    s[0] = s[1] = 0
    while 1:
        for i in s:
            if s[i] != 0:
                if i not in primes:
                    primes.append(i)
                for j in range(i ** 2, n, (2 * i if i != 2 else i)):
                    s[j] = 0
        if num > len(primes):
            s = s + list(range(len(s), n**2+1))
            n = len(s)
        else:
            return primes[num-1]


if __name__ == '__main__':
    print('Для 10го простого числа:')
    print(timeit('simple(10)', number=10, globals=globals()))
    print(timeit('eratosthenes_sieve(10)', number=10, globals=globals()))
    print(timeit('func(10)', number=10, globals=globals()))
    print('\nДля 100го простого числа:')
    print(timeit('simple(100)', number=10, globals=globals()))
    print(timeit('eratosthenes_sieve(100)', number=10, globals=globals()))
    print(timeit('func(100)', number=10, globals=globals()))
    print('\nДля 1000го простого числа:')
    print(timeit('simple(1000)', number=10, globals=globals()))
    print(timeit('eratosthenes_sieve(1000)', number=10, globals=globals()))
    print(timeit('func(1000)', number=10, globals=globals()))
