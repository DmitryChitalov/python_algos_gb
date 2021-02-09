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
"""
    Номер простого числа   simple                   eratosthenes_simple             Соотношение
    9                      0.00017729999999982482   0.0002721999999995006           1 : 1,5
    98                     0.042791799999999824     0.0018667999999997242           23 : 1
    666                    2.7125637000000005       0.018019100000000066            150 : 1
    987                    4.814896400000001        0.024512099999999037            ~ 200 : 1
    1978                   23.105338500000002       0.06627049999999812             370 : 1
    
Как хорошо видно из замеров для небольших чисел алгоритм с использованием решета Эратосфена 
может даже слегка проигрывать предложенному решению.
Но чем больше запрошенное простое число тем существеннее разница во времени выполнения. 
Алгоритм с ипользованием решета выигрывает на несколько порядков.
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


def eratosthenes_simple(n):  # порядковый номер простого числа.
    sieve = list(range(n*10 + 1))  # ограничиваем решето. По идеи должны вписаться.
    sieve[1] = 0    # обнуляем первый элемент.
    simple_idx = 0
    for el in sieve:
        if el > 1:
            for j in range(el + el, len(sieve), el):
                sieve[j] = 0
            simple_idx += 1
        if n == simple_idx:
            return el


def timeit_check(num):
    print("Замер с помощью инструмента timeit ")
    print(f"simple {timeit('simple(n)', globals=globals(), number=num)} seconds")
    print(f"eratosthenes_simple {timeit('eratosthenes_simple(n)', globals=globals(), number=num)} seconds")


n = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(n))
print(eratosthenes_simple(n))

timeit_check(10)
# timeit_check(100)

