"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
from timeit import timeit
from random import randint
import cProfile


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


enter_num_100 = randint(10000, 1000000)
enter_num_1000 = randint(1000000, 10000000)
enter_num_10000 = randint(100000000, 10000000000000)

print('Работа функции revers')
print(
    timeit(
        "revers(enter_num_100)",
        setup='from __main__ import revers, enter_num_100',
        number=10000))
print(
    timeit(
        "revers(enter_num_1000)",
        setup='from __main__ import revers, enter_num_1000',
        number=10000))
print(
    timeit(
        "revers(enter_num_1000)",
        setup='from __main__ import revers, enter_num_1000',
        number=10000))


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


print('Работа функции revers_2')
print(
    timeit(
        "revers_2(enter_num_100)",
        setup='from __main__ import revers_2, enter_num_100',
        number=10000))
print(
    timeit(
        "revers_2(enter_num_1000)",
        setup='from __main__ import revers_2, enter_num_1000',
        number=10000))
print(
    timeit(
        "revers_2(enter_num_1000)",
        setup='from __main__ import revers_2, enter_num_1000',
        number=10000))


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


print('Работа функции revers_3')
print(
    timeit(
        "revers_3(enter_num_100)",
        setup='from __main__ import revers_3, enter_num_100',
        number=10000))
print(
    timeit(
        "revers_3(enter_num_1000)",
        setup='from __main__ import revers_3, enter_num_1000',
        number=10000))
print(
    timeit(
        "revers_3(enter_num_1000)",
        setup='from __main__ import revers_3, enter_num_1000',
        number=10000))


def main():
    enter_num_100 = randint(10000, 1000000)
    enter_num_1000 = randint(1000000, 10000000)
    enter_num_10000 = randint(100000000, 10000000000000)
    res1 = revers(enter_num_100)
    res2 = revers(enter_num_1000)
    res3 = revers(enter_num_10000)
    res1 = revers_2(enter_num_100)
    res2 = revers_2(enter_num_1000)
    res3 = revers_2(enter_num_10000)
    res1 = revers_3(enter_num_100)
    res2 = revers_3(enter_num_1000)
    res3 = revers_3(enter_num_10000)


cProfile.run('main()')

# Вывод: профилировка иногда менее информативна и подходит не всегда, в таких случаях лучше использовать timeit
