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
import timeit


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


i = 100
print(simple(i))

print(
    timeit.timeit('simple(i)', 'from __main__ import simple, i', number=10))
print(
    timeit.timeit('simple(i)', 'from __main__ import simple, i', number=100))
print(
    timeit.timeit('simple(i)', 'from __main__ import simple, i', number=1000))


# По ссылке алгоритм расчитывает натуральные числа до указанного числа
# что не подходит по условию задачи
def eratosfen(n):
    """Адаптированное решето под условие задачи, что на ввод получаем
    порядковый номер простого числа
    Сложность - O(n**2)
    """
    simples = [2]
    next_num = simples[0] + 1
    while len(simples) < n:
        for i in simples:
            if next_num % i == 0:
                next_num += 1
                break
        else:
            simples.append(next_num)
            next_num += 1
    return simples[-1]


print(eratosfen(i))
print(
    timeit.timeit('eratosfen(i)', 'from __main__ import eratosfen, i',
                  number=10))
print(
    timeit.timeit('eratosfen(i)', 'from __main__ import eratosfen, i',
                  number=100))
print(
    timeit.timeit('eratosfen(i)', 'from __main__ import eratosfen, i',
                  number=1000))


def classic_eratosfen(n):
    """применение решета Эратосфена на массив чисел длинной n"""
    numbers = [True] * n
    numbers[0] = numbers[1] = False
    for i in range(2, n):
        if numbers[i]:
            for k in range(2 * i, n, i):
                numbers[k] = False
    return numbers


print(classic_eratosfen(i))
