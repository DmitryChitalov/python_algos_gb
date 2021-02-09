"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""

from random import randint
from timeit import timeit
from cProfile import run


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


var_num = randint(1, 2 ** 999)

# Начало тестов

print(timeit("revers(var_num)", setup="from __main__ import revers,var_num", number=10000))
run("revers(var_num)")

print(
    timeit("revers_2(var_num)", setup="from __main__ import revers_2,var_num", number=10000))
run('revers_2(var_num)')

print(
    timeit("revers_3(var_num)", setup="from __main__ import revers_3,var_num", number=10000))
run('revers_3(var_num)')

'''
    Судя по резултатам замеров которые показывают функции,
    можно сделать вывод, что самой оптимально является функция 3
'''
