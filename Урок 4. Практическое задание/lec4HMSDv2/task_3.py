"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
from timeit import timeit
import cProfile


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


enter_num = 1234567899876543211244645457457257275242458452

print(
    timeit(
        'revers(enter_num, 0)',
        setup='from __main__ import revers, enter_num',
        number=10000))

print(
    timeit(
        'revers_2(enter_num, 0)',
        setup='from __main__ import revers_2, enter_num',
        number=10000))

print(
    timeit(
        'revers_3(enter_num)',
        setup='from __main__ import revers_3, enter_num',
        number=10000))

cProfile.run('revers(enter_num,0)')
cProfile.run('revers_2(enter_num,0)')
cProfile.run('revers_3(enter_num)')

# Функция работающая через встроенные функции в 10ки раз боллее эффективная.
# CProfile выдает всегда 0. Написал в чат.. Странно.
