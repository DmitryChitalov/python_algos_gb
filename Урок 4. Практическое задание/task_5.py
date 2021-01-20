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


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))


def my_simple_search(num):
    n = 10000
    my_list = []
    for i in range(n + 1):
        my_list.append(i)
    my_list[1] = 0
    i = 2
    while i <= n:
        if my_list[i] != 0:
            j = i + i
            while j <= n:
                my_list[j] = 0
                j = j + i
        i += 1
    my_set = set(my_list)
    my_set.remove(0)
    my_list = list(my_set)
    my_list.sort()
    return my_list[num - 1]


num = int(input('Введите порядковый номер искомого простого числа: '))
print(my_simple_search(num))

print('Без применения "решета Эратосфена":')
print(timeit("simple(i)", setup="from __main__ import simple, i", number=100))

print('С применением "решета Эратосфена":')
print(timeit("my_simple_search(num)", setup="from __main__ import my_simple_search, num", number=100))

"""
С применением решета эратосфена поиск любого числа вне зависимости от его позиции(порядкового номера)
время выполнения будет примерно одинаковым. У простого же метода есть преимущество в скорости выполнения на малых 
числах порядкового номера, но с его увеличением время выполнения значительно увеличивается
"""