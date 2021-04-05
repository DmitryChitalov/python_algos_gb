"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика)
"""
from timememit import timememit
from numpy import arange, log, sin, cos, sqrt
from array import array
import math
import sys

args = iter(sys.argv)
next(args)
ARG1 = next(args, None)


# Сравним требования по памяти для трех реализаций
# "решета Эратосфена", через array, numpy и на
# "чистом" python
def upper_prime(n):
    ln = log(n)
    return int(n*(ln + log(ln)))


# через numpy
@timememit
def eratosthenes_numpy(n):
    # разница только в инициализации массива
    sieve = arange(upper_prime(n))
    k = 2
    for _ in range(n - 1):
        # и заполнении решета
        sieve[::k] = 0
        while sieve[k] == 0:
            k += 1
    return k


# через array
@timememit
def eratosthenes_array(n):
    size = upper_prime(n)
    sieve = array('i', range(size))
    k = 2
    for _ in range(n - 1):
        for i in range(k, size, k):
            sieve[i] = 0
        while sieve[k] == 0:
            k += 1
    return k


# на чистом python
@timememit
def eratosthenes(n):
    size = upper_prime(n)
    sieve = list(range(size))
    k = 2
    for _ in range(n - 1):
        for i in range(k, size, k):
            sieve[i] = 0
        while sieve[k] == 0:
            k += 1
    return k


n = 100000



if ARG1 is None:
    print(f'prime({n}) = {eratosthenes(n)}')
    print(f'prime({n}) = {eratosthenes(n)}')
    print(f'prime({n}) = {eratosthenes(n)}')
    print(f'prime({n}) = {eratosthenes(n)}')
    print(f'prime({n}) = {eratosthenes_numpy(n)}')
    print(f'prime({n}) = {eratosthenes_numpy(n)}')
    print(f'prime({n}) = {eratosthenes_numpy(n)}')
    print(f'prime({n}) = {eratosthenes_numpy(n)}')
    print(f'prime({n}) = {eratosthenes_array(n)}')
    print(f'prime({n}) = {eratosthenes_array(n)}')
    print(f'prime({n}) = {eratosthenes_array(n)}')
    print(f'prime({n}) = {eratosthenes_array(n)}')
# ---
# eratosthenes: 0.6396 s, 0.656250 MiB
# prime(100000) = 1299709
# eratosthenes: 0.5894 s, 10.886719 MiB
# prime(100000) = 1299709
# eratosthenes: 0.5845 s, 0.238281 MiB
# prime(100000) = 1299709
# eratosthenes: 0.5792 s, 0.238281 MiB
# prime(100000) = 1299709
# eratosthenes_array: 0.5666 s, 0.000000 MiB
# prime(100000) = 1299709
# eratosthenes_array: 0.5675 s, 0.000000 MiB
# prime(100000) = 1299709
# eratosthenes_array: 0.5665 s, 0.000000 MiB
# prime(100000) = 1299709
# eratosthenes_array: 0.5690 s, 0.000000 MiB
# prime(100000) = 1299709
# eratosthenes_numpy: 0.5143 s, 0.000000 MiB
# prime(100000) = 1299709
# eratosthenes_numpy: 0.5149 s, 0.000000 MiB
# prime(100000) = 1299709
# eratosthenes_numpy: 0.5138 s, 0.000000 MiB
# prime(100000) = 1299709
# eratosthenes_numpy: 0.5152 s, 0.000000 MiB
# prime(100000) = 1299709
# ---
#
# Теперь поменяем вызовы местами.
# Ключ коммандной строки показывает, что замеры
# нужно делать сразу после запуска, иначе
# будут нули
if ARG1 == 'array':
    print(f'prime({n}) = {eratosthenes_array(n)}')
    print(f'prime({n}) = {eratosthenes_array(n)}')
    print(f'prime({n}) = {eratosthenes_array(n)}')
    print(f'prime({n}) = {eratosthenes_array(n)}')
    print(f'prime({n}) = {eratosthenes_numpy(n)}')
    print(f'prime({n}) = {eratosthenes_numpy(n)}')
    print(f'prime({n}) = {eratosthenes_numpy(n)}')
    print(f'prime({n}) = {eratosthenes_numpy(n)}')
    print(f'prime({n}) = {eratosthenes(n)}')
    print(f'prime({n}) = {eratosthenes(n)}')
    print(f'prime({n}) = {eratosthenes(n)}')
    print(f'prime({n}) = {eratosthenes(n)}')
# ---
# eratosthenes_array: 0.5791 s, 0.781250 MiB
# prime(100000) = 1299709
# eratosthenes_array: 0.5782 s, 4.636719 MiB
# prime(100000) = 1299709
# eratosthenes_array: 0.5912 s, 0.000000 MiB
# prime(100000) = 1299709
# eratosthenes_array: 0.5735 s, 0.000000 MiB
# prime(100000) = 1299709
# eratosthenes_numpy: 0.5275 s, 0.066406 MiB
# prime(100000) = 1299709
# eratosthenes_numpy: 0.5225 s, 5.152344 MiB
# prime(100000) = 1299709
# eratosthenes_numpy: 0.5150 s, 0.000000 MiB
# prime(100000) = 1299709
# eratosthenes_numpy: 0.5153 s, 0.000000 MiB
# prime(100000) = 1299709
# eratosthenes: 0.5854 s, 0.675781 MiB
# prime(100000) = 1299709
# eratosthenes: 0.5867 s, 0.246094 MiB
# prime(100000) = 1299709
# eratosthenes: 0.5843 s, 0.246094 MiB
# prime(100000) = 1299709
# eratosthenes: 0.5867 s, 0.246094 MiB
# prime(100000) = 1299709
# ---
# Этот пример помогает нам понять результаты прошлого
# примера. Алгоритм "array" выделяет 1 блок 5M,
# "numpy" -- 1 блок 10M, "list" -- 1 блок по 10M
# и еще множество мелких блоков.
# Поэтому если расположить вызовы в порядке возрастания
# потребления памяти, мы видим ее выделение на каждой
# группе вызовов. Если же расположить в обратном порядке,
# то выделение происходит только на первой группе,
# на остальных -- нули.

# Что же касается array, то в этой задаче он показывает
# двукратную экономию памяти по сравнению с numpy и python,
# при этом не теряя в производительности.
# Однако заменить numpy он, конечно, не может
# Идеология numpy не сводится к экономии памяти,
# т.к. эта библиотека создавалась для ускорения
# вычисления сложных формул путем векторизации.
# Поэтому огромные массивы numpy являются платой
# за возможность выполнять быстрые С-функции.


@timememit
def formula_array():
    xx = array('d', range(n))
    yy = array('d', range(n))
    for i, x in enumerate(xx):
        yy[i] = math.sqrt(math.sin(x)**2 + math.cos(x)**2)
    return yy


@timememit
def formula_numpy():
    xx = arange(n)
    yy = sqrt(sin(xx)**2 + cos(xx)**2)
    return yy


if ARG1 == "math":
    formula_array()
    formula_numpy()

# ---
# formula_array: 0.1974 s, 1.714844 MiB
# formula_numpy: 0.1160 s, 1.769531 MiB
# ---

# То есть на сложных формулах array ожидаемо проигрывает numpy
# по времени из за накладных расходов на циклы и переменные python,
# при этом разница в потреблении памяти сокращается
# по мере усложнения вычислений.
#
# "Серебряной пулей" в данном вопросе мне кажутся библиотеки,
# компилирующие в бинарный код типа cython и numba, однако их
# использование накладывает существенные ограничения на этап
# развертывания приложения и не всегда допустимо.
