"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import cProfile
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


number = randint(100000000000000000000000000, 1000000000000000000000000000000000000)
print(number)


def main():
    revers(number)
    revers_2(number)
    revers_3(number)


print(timeit('revers(number)', 'from __main__ import revers, number', number=10000))
print(timeit('revers_2(number)', 'from __main__ import revers_2, number', number=10000))
print(timeit('revers_3(number)', 'from __main__ import revers_3, number', number=10000))
cProfile.run('main()')

"""Вторая быстрее первой за счет исключения рекурсии, 
третья быстрее второй за счет использования встроенных методов преобразования.
"""
