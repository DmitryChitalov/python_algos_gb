"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
"""Из трех реализаций самая эффективная - slice - реверс на месте, т.к. имеет константую сложность O(1)
У цикла сложность O(n) и он на втором месте
И самое долгое - рекурсия
В cProfile цифры все 0, т.к. задача простая, но в рекурсии видно, что кол-во вызовов функции 
ncalls - меняется в зависимости от длины числа, переданного функции."""

from timeit import timeit
from random import randint
import cProfile

num_1000 = randint(1000000, 10000000)


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


functions = ["revers(num_1000)", "revers_2(num_1000)", "revers_3(num_1000)"]
setup_data = "from __main__ import revers, revers_2, revers_3, num_1000"

for fn in functions:
    print(f'Время выполнения функции {fn}',
          timeit(fn, setup=setup_data, number=10000))

print()

cProfile.run('revers(num_1000)')
cProfile.run('revers_2(num_1000)')
cProfile.run('revers_3(num_1000)')
