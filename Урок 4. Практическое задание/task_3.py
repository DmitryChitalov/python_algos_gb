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
num_100 = randint(10000, 1000000)


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


print('Результат 1й ф-ии: ',
      timeit(
        "revers(num_100)",
        setup='from __main__ import revers, num_100',
        number=10000))

print('Результат 2й ф-ии: ',
      timeit(
        "revers_2(num_100)",
        setup='from __main__ import revers_2, num_100',
        number=10000))

print('Результат 3й ф-ии: ',
      timeit(
        "revers_3(num_100)",
        setup='from __main__ import revers_3, num_100',
        number=10000))

'''cProfile'''
def main():
    revers(num_100)
    revers_2(num_100)
    revers_3(num_100)


cProfile.run('main()')

print('Вывод: наиболее эффективным вариантом будет обратный срез строки, тк мы пользуемся встроенной функцией '
      ' работы со строкой, а она работает быстрее')
