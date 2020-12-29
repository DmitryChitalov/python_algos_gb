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
from math import log
import sys

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
            # print(n)
            if count == i:
                break
            count += 1
        n += 1
    return n
# сложность квадратичная - O(n**2)


def separator(i):
    """С использованием «Решета Эратосфена»"""
    m = i**2
    test_list = [a for a in range(m)]
    test_list[1] = 0
    n = 2
    while n <= m-1:
        if test_list[n] != 0:
            new_n = n*2
            while new_n <= m-1:
                test_list[new_n] = 0
                new_n = new_n+n
        n += 1
    test_list = sorted(list(set(test_list)))
    return test_list[i]
# сложность квадратичная - O(n**2), по большей части из-за формирования начального ряда возведением в квадрат и
# последующей необходимости прореживать весь этот ряд


def separator_2(i):
    """2 c использованием «Решета Эратосфена»"""
    # m = i *15# работает примерно до i=500000
    m = int(i*(log(i**2))) # на поиске 10'000'000-го простого числа у меня пямять на машине кончилась,
    # но милионное вполне себе ищет
    test_list = [a for a in range(m)]
    test_list[1] = 0
    n = 2
    while n <= m - 1:
        if test_list[n] != 0:
            new_n = n * 2
            while new_n <= m - 1:
                test_list[new_n] = 0
                new_n = new_n + n
        n += 1
    test_list = sorted(list(set(test_list)))
    return test_list[i]
# сложность логарифмическая O(log n) т.к, количество операций уменьшается на каждой итерации


def simple_rec(i, count = 1, n = 2):
    sys.setrecursionlimit(1700)
    if count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                return n
            count += 1
        n += 1
        return simple_rec(i, count, n)
# сложность квадратичная O(n**2)




if __name__ == '__main__':
    i = int(input('Введите порядковый номер искомого простого числа: '))
    print(simple(i))
    print(separator(i))
    print(separator_2(i))
    # print(simple_rec(i))
    print(
        timeit(
            'simple(i)',
            setup='from __main__ import simple, i',
            number=10))
    print(
        timeit(
            'separator(i)',
            setup='from __main__ import separator, i',
            number=10))
    print(
        timeit(
            'separator_2(i)',
            setup='from __main__ import separator_2, i',
            number=10))
    # print(
    #     timeit(
    #         'simple_rec(i)',
    #         setup='from __main__ import simple_rec, i',
    #         number=1))
    # sys.setrecursionlimit(10)

    """
    пока с решетом эратосфена скорость в среднем в 2 раза меньше
    10:
    0.0016544000000000558 --simple(10)
    0.0027448000000003248 --separator(10)
    100:
    0.19927629999999974 --simple(100)
    0.40792629999999974 --separator(100)
    1000:
    33.029426699999995 --simple(1000)
    58.3655702 --separator(1000)
    Судя по цифрам похоже на квадратичную сложнность в обоих случаях, причем наивный алгоритм работает быстрее, 
    скорее всего из-за того что в решете  я строю слишком длинный ряд
    
    Если сократить ряд (как separator_2) то скорость по решету становится на порядок выше:
    i=1000
    33.1243436 --simple(1000)
    59.885764099999996 --separator(1000)
    0.005768299999999726 --separator_2(1000)
    Более того я таки дождался замеров по варианту separator_2:
    i=10000000
    n=179424673
    time= 259.8837869
    на предыдущих вариантах я даже пробовать не стал 10-миллионое искать)
    
    Так же этот один из тех случаев когда рекурсия даже без мемоизации работает быстрее цикла, 
    но глубина сыграла свою роль, и последнее число при стандартной глубине рекурсии i = 168:
    0.19558269999999967 -simple(100)
    0.40170629999999985 --separator(100)
    0.00036719999999990094 --separator_2(100)
    0.0021407999999998317 --simple_rec(100)
    
    Все равно вариант с решетом Эратосфена при разумной организации ряда оказался быстрее на порядок даже рекурсивного, 
    и позволяет искать гораздо большие значения простых чисел.
    Сложности:
    simple O(n**2)
    separator O(n**2)
    separator_2 O(log n)
    simple_rec O(n**2)
      
    """