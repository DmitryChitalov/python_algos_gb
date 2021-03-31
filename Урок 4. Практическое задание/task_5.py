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
# Понятно, что некорректно сравнивать алгоритм на голом питоне
# с алгоритмом на numpy, однако если есть инструмент,
# специально созданный для математических задач, почему бы
# им не воспользоваться. К тому же на numpy алгоритм формулируется
# предельно лаконично и понятно
from numpy import log, arange


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


# Оценка верхнего значения n-го простого числа
def upper_prime(n):
    ln = log(n)
    return n*(ln + log(ln))


# К сожалению, в numpy нет встроенного метода
# нахождения первого ненулевого элемента.
def first_nonzero(x):
    idx = x.view(bool).argmax() // x.itemsize
    return idx if x[idx] else -1


def eratosthenes(n):
    # определяем размер "решета" и заполняем натуральным рядом
    sieve = arange(upper_prime(n))
    sieve[0:2] = 0
    # повторяем, пока не дойдем до n
    for _ in range(n - 1):
        k = first_nonzero(sieve)
        # "вычеркиваем" каждый к-й элемент
        sieve[::k] = 0
    return first_nonzero(sieve)


print(timeit("print(simple(10000))", number=1, globals=globals()))
print(timeit("print(eratosthenes(10000))", number=1, globals=globals()))
# output:
# ---
# 104729
# 42.7186805739766
# 104729
# 0.1595245740027167
