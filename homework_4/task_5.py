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

from timeit import Timer

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

# моя версия функции
def simple_2(i):
    if i == 1:
        return 2
    elif i == 2:
        return 3
    elif i == 3:
        return 5
    elif i == 4:
        return 7
    num = 8
    count = 5
    while True:
        if num % 2 != 0 and num % 3 != 0 and num % 5 != 0 and num % 7 != 0:
            simple = num
            count += 1
        num += 1
        if count > i:
            break
    return simple

t1 = Timer("simple(10)", "from __main__ import simple")
print("simple ", t1.timeit(number=1000))

t2 = Timer("simple_2(10)", "from __main__ import simple_2")
print("simple_2 ", t2.timeit(number=1000))

t3 = Timer("simple(100)", "from __main__ import simple")
print("simple ", t3.timeit(number=1000))

t4 = Timer("simple_2(100)", "from __main__ import simple_2")
print("simple_2 ", t4.timeit(number=1000))

t5 = Timer("simple(1000)", "from __main__ import simple")
print("simple ", t5.timeit(number=100))

t6 = Timer("simple_2(1000)", "from __main__ import simple_2")
print("simple_2 ", t6.timeit(number=100))

'''Результаты замеров:
simple  0.016040600000000002
simple_2  0.002964500000000002
simple  1.9519724999999999
simple_2  0.05229019999999984
simple  32.904510200000004
simple_2  0.05761439999999851'''

'''Время выполнения первой функции экспоненциалььно растет с увеличением передаваемого функции аргумента. Это связано 
с тем, что в функции исползуется вложенный цикл. Моя версия функции работает значительно быстрее и скорость ее работы 
менее зависима от передаваемого аргумента'''