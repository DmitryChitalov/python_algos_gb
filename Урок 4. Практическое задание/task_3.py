"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

# Наиболее эффективным оказался алгоритм, использующий срез с обратным направлением.
# Минимальное количество вызовов, более эффективная работа встроенной ф-ции.

from cProfile import run
from timeit import timeit
from random import randint


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


if __name__ == '__main__':
    num_1000 = randint(1000000, 10000000)
    num_10000 = randint(100000000, 10000000000000)

    rep = 1000

    # ------------------Замеры timeit--------------------------------

    print('Рекурсивный reverse')
    print(
        timeit(
            "revers(num_1000)",
            setup='from __main__ import revers, num_1000',
            number=rep))
    print(
        timeit(
            "revers(num_10000)",
            setup='from __main__ import revers, num_10000',
            number=rep))

    print('Reverse через цикл')
    print(
        timeit(
            "revers_2(num_1000)",
            setup='from __main__ import revers_2, num_1000',
            number=rep))
    print(
        timeit(
            "revers_2(num_10000)",
            setup='from __main__ import revers_2, num_10000',
            number=rep))

    print('Reverse через срез')
    print(
        timeit(
            "revers_3(num_1000)",
            setup='from __main__ import revers_3, num_1000',
            number=rep))
    print(
        timeit(
            "revers_3(num_10000)",
            setup='from __main__ import revers_3, num_10000',
            number=rep))

    # ------------------cProfile--------------------------------

    print('Рекурсивный reverse')
    run('revers(num_10000)')

    print('Reverse через цикл')
    run('revers_2(num_10000)')

    print('Reverse через срез')
    run('revers_3(num_10000)')
