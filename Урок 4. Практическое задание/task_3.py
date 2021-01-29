"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

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


my_nums = randint(10000, 100000)
print('--------First solution--------')
run('revers(my_nums)')
print(
    timeit(
        'revers(my_nums)',
        setup='from __main__ import revers, my_nums',
        number=10000))
print('--------Second solution--------')
run('revers_2(my_nums)')
print(
    timeit(
        'revers_2(my_nums)',
        setup='from __main__ import revers_2, my_nums',
        number=10000))
print('--------Third solution--------')
run('revers_3(my_nums)')
print(
    timeit(
        'revers_3(my_nums)',
        setup='from __main__ import revers_3, my_nums',
        number=10000))

"""
С учетом уже выполненных задач результаты получились предсказуемыми.
Самое медленное решение -- с рекурсией.
На втором месте цикл. Самый быстрый -- срез.
"""
