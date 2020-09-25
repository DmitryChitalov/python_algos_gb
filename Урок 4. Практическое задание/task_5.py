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
Замер для порядкого номера 10:

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
10000    0.214    0.000    0.214    0.000 task_5.py:30(simple)
10000    0.184    0.000    0.234    0.000 task_5.py:50(sieve_eratosthenes)
    
Замер для порядкого номера 100:  

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
10000   30.385    0.003   30.385    0.003 task_5.py:30(simple)
10000    3.316    0.000    4.040    0.000 task_5.py:50(sieve_eratosthenes)

Замер для порядкого номера 1000:  

ncalls  tottime  percall  cumtime  percall filename:lineno(function)
  100   43.217    0.432   43.217    0.432 task_5.py:36(simple)
  100    0.424    0.004    0.510    0.005 task_5.py:56(sieve_eratosthenes)
  
Для поиска простого числа до 10, эффективней (немного) алгоритм через перебор делителей(сложность O(n**2)),
В остальных случаях алгоритм с использование «Решета Эратосфена» намного эффетивней( тут тоже цикл в цикле, но
во второй цикл с каждой итерацией мы заходим все реже(а после перебора первого десятка не заходим совсем),
поэтому сложность O(n log(log n)).Для определения сложности «Решета Эратосфена» прочитал статью в вики.
"""
import cProfile


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


def sieve_eratosthenes(idx: int):
    """
    функция работает до idx = 1_999_999
    """
    a = []
    control = {1: 2, 2: 4, 3: 7, 4: 9, 5: 12, 6: 14, 7: 18}
    coefficient = control.get(len(str(idx)))
    n = idx * coefficient
    for i in range(n + 1):
        a.append(i)

    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    a = set(a)
    a.remove(0)
    res = list(sorted(a))
    return res[idx - 1]


def main(index):
    for _ in range(100):
        simple(index)
        sieve_eratosthenes(index)


# i = int(input('Введите порядковый номер искомого простого числа: '))
# print(simple(i))
# print(sieve_eratosthenes(10))


cProfile.run('main(1000)')
